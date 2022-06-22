import os.path
from typing import Any, Dict, Optional, Tuple
from pace.util.mpi import MPI

from pace.util import TilePartitioner
from pace.dsl.dace.dace_config import DaceConfig, DaCeOrchestration

import yaml


################################################
# Distributed compilation


def determine_compiling_ranks(config: DaceConfig) -> Tuple[bool, Any]:
    is_compiling = False
    rank = config.my_rank
    size = config.rank_size

    if int(size / 6) == 0:
        is_compiling = True
    elif rank % int(size / 6) == rank:
        is_compiling = True

    return is_compiling


def unblock_waiting_tiles(comm, sdfg_path: str) -> None:
    if comm and comm.Get_size() > 1:
        for tile in range(1, 6):
            tilesize = comm.Get_size() / 6
            comm.send(sdfg_path, dest=tile * tilesize + comm.Get_rank())


def top_tile_rank_from_decomposition_string(string, partitioner):
    """
    Return the rank number on the correct subtile position by matching
    the decomposition string and the position given by the partitionner
        e.g.: return rank for "00" for bottom left subtile
    """
    tilesize = partitioner.total_ranks / 6
    if tilesize == 1:
        return 0
    for rank in range(partitioner.total_ranks):
        if (
            string == "00"
            and partitioner.tile.on_tile_bottom(rank)
            and partitioner.tile.on_tile_left(rank)
        ):
            return rank % tilesize
        if (
            string == "10"
            and partitioner.tile.on_tile_bottom(rank)
            and not partitioner.tile.on_tile_left(rank)
            and not partitioner.tile.on_tile_right(rank)
        ):
            return rank % tilesize
        if (
            string == "20"
            and partitioner.tile.on_tile_bottom(rank)
            and partitioner.tile.on_tile_right(rank)
        ):
            return rank % tilesize
        if (
            string == "01"
            and not partitioner.tile.on_tile_bottom(rank)
            and not partitioner.tile.on_tile_top(rank)
            and partitioner.tile.on_tile_left(rank)
        ):
            return rank % tilesize
        if (
            string == "11"
            and not partitioner.tile.on_tile_bottom(rank)
            and not partitioner.tile.on_tile_top(rank)
            and not partitioner.tile.on_tile_left(rank)
            and not partitioner.tile.on_tile_right(rank)
        ):
            return rank % tilesize
        if (
            string == "21"
            and not partitioner.tile.on_tile_bottom(rank)
            and not partitioner.tile.on_tile_top(rank)
            and partitioner.tile.on_tile_right(rank)
        ):
            return rank % tilesize
        if (
            string == "02"
            and partitioner.tile.on_tile_top(rank)
            and partitioner.tile.on_tile_left(rank)
        ):
            return rank % tilesize
        if (
            string == "12"
            and partitioner.tile.on_tile_top(rank)
            and not partitioner.tile.on_tile_left(rank)
            and not partitioner.tile.on_tile_right(rank)
        ):
            return rank % tilesize
        if (
            string == "22"
            and partitioner.tile.on_tile_top(rank)
            and partitioner.tile.on_tile_right(rank)
        ):
            return rank % tilesize

    return None


def top_tile_rank_to_decomposition_string(rank: int, partitioner: TilePartitioner):
    """
    Return the decomposition string for the correct subtile position by matching
     osition given by the partitionner
        e.g.: return "00" for ranl at bottom left subtile
    """
    if partitioner.tile.on_tile_bottom(rank):
        if partitioner.tile.on_tile_left(rank):
            return "00"
        if partitioner.tile.on_tile_right(rank):
            return "20"
        else:
            return "10"
    if partitioner.tile.on_tile_top(rank):
        if partitioner.tile.on_tile_left(rank):
            return "02"
        if partitioner.tile.on_tile_right(rank):
            return "22"
        else:
            return "12"
    else:
        if partitioner.tile.on_tile_left(rank):
            return "01"
        if partitioner.tile.on_tile_right(rank):
            return "21"
        else:
            return "11"


def read_target_rank(
    rank: int,
    partitioner: TilePartitioner,
    config: DaceConfig,
    layout_filepath=None,
) -> int:
    if not layout_filepath:
        return -1
    top_tile_rank = top_tile_equivalent(rank, config.rank_size)
    with open(layout_filepath) as decomposition:
        parsed_file = yaml.safe_load(decomposition)
        read_rank = int(
            parsed_file[
                top_tile_rank_to_decomposition_string(top_tile_rank, partitioner)
            ]
        )
        MPI.COMM_WORLD.Barrier()  # with open() is not very multi-node friendly
        return read_rank


def top_tile_equivalent(rank, size):
    tilesize = size / 6
    return rank % tilesize


################################################

################################################
# SDFG load (both .sdfg file and build directory containing .so)

""" The below helpers use a dirty "once" global flag to allow for reentry many
    calls as those are called from function in a recursive pattern.
"""


def write_decomposition(
    partitioner: TilePartitioner,
):
    from gt4py import config as gt_config

    path = f"{gt_config.cache_settings['root_path']}/.layout/"
    config_path = path + "decomposition.yml"
    os.makedirs(path, exist_ok=True)
    decomposition: Dict[Any, Any] = {}
    for string in ["00", "10", "20", "01", "11", "21", "02", "12", "22"]:
        target_rank = top_tile_rank_from_decomposition_string(string, partitioner)
        if target_rank is not None:
            decomposition.setdefault(string, int(target_rank))

    with open(config_path, "w") as outfile:
        yaml.dump(decomposition, outfile)


def get_sdfg_path(
    daceprog_name: str, config: DaceConfig, sdfg_file_path: Optional[str] = None
) -> Optional[str]:
    """Build an SDFG path from the qualified program name or it's direct path to .sdfg

    Args:
        program_name: qualified name in the form module_qualname if module is not locals
        sdfg_file_path: absolute path to a .sdfg file
    """

    # TODO: check DaceConfig for cache.strategy == name

    # Guarding against bad usage of this function
    if config.get_orchestrate() != DaCeOrchestration.Run:
        return None

    # Case of a .sdfg file given by the user to be compiled
    if sdfg_file_path is not None:
        if not os.path.isfile(sdfg_file_path):
            raise RuntimeError(
                f"SDFG filepath {sdfg_file_path} cannot be found or is not a file"
            )
        return sdfg_file_path

    # Case of loading a precompiled .so - lookup using GT_CACHE
    import os

    from gt4py import config as gt_config

    if config.rank_size > 1:
        rank = config.my_rank
        rank_str = f"_{config.target_rank:06d}"
    else:
        rank = "N/A"
        rank_str = ""

    sdfg_dir_path = (
        f"{gt_config.cache_settings['root_path']}"
        f"/.gt_cache{rank_str}/dacecache/{daceprog_name}"
    )
    if not os.path.isdir(sdfg_dir_path):
        raise RuntimeError(f"Precompiled SDFG is missing at {sdfg_dir_path}")

    print(f"[DaCe Config] Rank {rank} loading SDFG {sdfg_dir_path}")

    return sdfg_dir_path


def set_distributed_caches(config: "DaceConfig"):
    """In Run mode, check required file then point current rank cache to source cache"""

    # Execute specific initialization per orchestration state
    orchestration_mode = config.get_orchestrate()

    # Check that we have all the file we need to early out in case
    # of issues.
    if orchestration_mode == DaCeOrchestration.Run:
        import os

        from gt4py import config as gt_config

        # Check our cache exist
        if config.rank_size > 1:
            rank = config.target_rank
            rank_str = f"_{config.target_rank:06d}"
        else:
            rank = "N/A"
            rank_str = ""
        cache_filepath = f"{gt_config.cache_settings['root_path']}/.gt_cache{rank_str}"
        if not os.path.exists(cache_filepath):
            raise RuntimeError(
                f"{orchestration_mode} error: Could not find caches for rank "
                f"{rank} at {cache_filepath}"
            )

        # All, good set this rank cache to the source cache
        gt_config.cache_settings["dir_name"] = f".gt_cache{rank_str}"
        print(
            f"[{orchestration_mode}] Rank {rank} "
            f"reading cache {gt_config.cache_settings['dir_name']}"
        )
