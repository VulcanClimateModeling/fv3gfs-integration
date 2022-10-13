# Pace

Pace is an implementation of the FV3GFS / SHiELD atmospheric model developed by NOAA/GFDL using the GT4Py domain-specific language in Python. The model can be run on a laptop using Python-based backend or on thousands of heterogeneous compute nodes of a large supercomputer.

The top-level directory contains the main components of pace such as the dynamical core, the physical parameterizations and utilities.

**WARNING** This repo is under active development - supported features and procedures can change rapidly and without notice.

This git repository is laid out as a mono-repo, containing multiple independent projects. Because of this, it is important not to introduce unintended dependencies between projects. The graph below indicates a project depends on another by an arrow pointing from the parent project to its dependency. For example, the tests for fv3core should be able to run with only files contained under the fv3core and util projects, and should not access any files in the driver or physics packages. Only the top-level tests in Pace are allowed to read all files.

![Graph of interdependencies of Pace modules, generated from dependences.dot](./dependencies.svg)

## Building the docker image

While it is possible to install and build pace bare-metal, we can ensure all system libraries are installed with the correct versions by using a Docker container to test and develop pace.

First, you will need to update the git submodules so that any dependencies are cloned and at the correct version:
```shell
git submodule update --init --recursive
```

Then build the `pace` docker image at the top level.
```shell
make build
```

## Building bare-metal

Pace requires gcc > 9.2, MPI, and Python 3.8 on your system, and CUDA is required to run with a GPU backend. You will also need the headers of the boost libraries in your `$PATH` (boost itself does not need to be installed).

```shell
cd /BOOST/LOCATION
wget https://boostorg.jfrog.io/artifactory/main/release/1.79.0/source/boost_1_79_0.tar.gz
tar -xzf boost_1_79_0.tar.gz
mkdir -p boost_1_79_0/include
mv boost_1_79_0/boost boost_1_79_0/include/
export BOOST_ROOT=BOOST/LOCATION/boost_1_79_0
```

When cloning Pace you will need to update the repository's submodules as well:
```shell
$ git clone --recursive https://github.com/ai2cm/pace.git
```
or if you have already cloned the repository:
```
$ git submodule update --init --recursive
```

We recommend creating a python `venv` or conda environment specifically for Pace.

```shell
$ python3 -m venv venv_name
$ source venv_name/bin/activate
```

Inside of your pace `venv` or conda environment pip install the Python requirements, GT4Py, and Pace:
```shell
$ pip3 install -r requirements_dev.txt -c constraints.txt
```

Shell scripts to install Pace on specific machines such as Gaea can be found in `examples/build_scripts/`.

You can now run and develop Pace directly. After downloading the test data the Pace tests can be run with pytest using the same test arguments as inside the container.

## Running an example test case

### Bare-metal
With the environment activated, you can run an example baroclinic test case with the following command:
```shell
mpirun -n 6 python3 -m pace.driver.run driver/examples/configs/baroclinic_c12.yaml

# or with oversubscribe if you do not have at least 6 cores
mpirun -n 6 --oversubscribe python3 -m pace.driver.run driver/examples/configs/baroclinic_c12.yaml
```

### Inside docker
```shell
make dev
mpirun --mca btl_vader_single_copy_mechanism none -n 6 python3 -m pace.driver.run /pace/driver/examples/configs/baroclinic_c12.yaml
```

After the run completes, you will see an output direcotry `output.zarr`. An example to visualize the output is provided in `driver/examples/plot_output.py`. See the [driver example](driver/examples/README.md) section for more details.

## Running translate tests

See the [translate tests README](stencils/pace/stencils/testing/README.md) for more information.
