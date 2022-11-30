import dataclasses

import pace.util
from pace.util import NullProfiler, Profiler

from .collector import (
    AbstractPerformanceCollector,
    NullPerformanceCollector,
    PerformanceCollector,
)
from pace.util._optional_imports import cupy as cp


@dataclasses.dataclass
class PerformanceConfig:
    collect_performance: bool = False
    collect_cProfile: bool = False
    experiment_name: str = "test"

    def build(self, comm: pace.util.Comm) -> AbstractPerformanceCollector:
        if self.collect_performance:
            return PerformanceCollector(experiment_name=self.experiment_name, comm=comm)
        else:
            return NullPerformanceCollector()

    def build_profiler(self):
        if self.collect_cProfile:
            return Profiler()
        else:
            return NullProfiler()

    @classmethod
    def start_cuda_profiler(cls):
        if cp is not None:
            cp.cuda.profiler.start()

    @classmethod
    def stop_cuda_profiler(cls):
        if cp is not None:
            cp.cuda.profiler.stop()

    @classmethod
    def mark_cuda_profiler(cls, message: str):
        if cp is not None:
            cp.cuda.nvtx.Mark(message)
