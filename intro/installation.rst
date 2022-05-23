Installing CosmoSIS
-------------------

Pip (core package only, no cosmology content)
=============================================

If you only need CosmoSIS for its core sampling tools and datablock, and don't need the cosmological likelihoods, then you can install those with pip::

    pip install cosmosis

If you get an error including the phrase ``--single-version-externally-managed not recognized`` then you should first upgrade your setuptools package like this::

    pip install -U setuptools wheel

and then try again.

Conda-Forge (from scratch) on Linux and Intel Macs
==================================================

This is the easiest way to get the full CosmoSIS package. It downloads everything you need.  If the ``conda`` command works on your computer already, use the instructions for an existing installation (next section) instead. 

Otherwise first run one of these commands to download the installer:

On Linux::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh

On Intel Macs::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh



Then, whichever you do, run these commands to install everything and download the standard library::

    chmod +x Miniforge3.sh
    ./Miniforge3.sh -b -p ./env 
    source ./env/bin/activate
    conda install -y python=3.9 cosmosis cosmosis-build-standard-library
    source cosmosis-configure
    cosmosis-build-standard-library main


This will make a new directory cosmosis-standard-library with the cosmology packages in. Explore that directory to start using CosmoSIS.

Whenever you start a fresh terminal shell you need to run these commands to get set up again::

    conda activate ./env
    source cosmosis-configure


Conda-Forge (from scratch) on M1 (Silicon) Macs
===============================================

We don't yet have the conda version auto-building on Silicon/M1 macs yet.  Instead you can get almost everything through conda and compile the final steps yourself::

    conda create -c conda-forge -p ./env astropy camb cfitsio bzip2 llvm-openmp python=3.9 gsl fftw libblas liblapack fitsio cython scikit-learn fast-pt openmpi zeus-mcmc pyyaml emcee numpy scipy matplotlib pybind11 emcee dynesty mpi4py


    conda activate ./env
    export CC=clang CXX=clang++ FC=gfortran

    pip install cosmosis cobaya

    source cosmosis-configure

    git clone https://github.com/joezuntz/cosmosis-standard-library
    cd cosmosis-standard-library

    # this will probably fail the first time - we are looking into this
    make
    # just run it again:
    make

Whenever you start a fresh terminal shell you need to run these commands to get set up again::

    conda activate ./env
    source cosmosis-configure
    export CC=clang CXX=clang++ FC=gfortran




Conda-Forge (existing installation)
===================================

If you already have conda installed on your computer, then you can create a new environment and install cosmosis tools in it with::

    conda create -p ./env -c conda-forge python==3.9 cosmosis cosmosis-build-standard-library
    conda activate ./env
    source cosmosis-configure
    cosmosis-build-standard-library

This will make a new directory cosmosis-standard-library with the cosmology packages in.

Whenever you start a fresh terminal shell you need to run these commands to get set up again::

    conda activate ./env
    source cosmosis-configure

NERSC
=====

There is a globally-accessible CosmoSIS installation for the NERSC machine Cori.  You can access it by running::

    source $CFS/des/zuntz/cosmosis-global/setup-cosmosis-nersc

This will set all the necessary environment variables; you can then clone the cosmosis-standard-library and the make command should work::

    git clone https://github.com/joezuntz/cosmosis-standard-library
    cd cosmosis-standard-library
    make

You need source the setup script each time you want to use the system, including in batch scripts and interactive jobs.

If you need your own python environment to install new dependencies, you can do that with::

    conda create -p ./env --clone $CFS/des/zuntz/cosmosis-global/env

That will make a new environment in the ./env directory, which you can start using by doing::

    source $CFS/des/zuntz/cosmosis-global/setup-cosmosis-nersc ./env

You can then pip or conda install things in your new environment.

If your dependency may be generally useful please open an issue and we can install it centrally also: https://github.com/joezuntz/cosmosis/issues/

Installing manually on clusters and supercomputers
==================================================

The conda-forge version above often works on larger machines, though not always. Give it a go first (and test to see if multi-node jobs work).

If not, you will need these dependencies, which many systems will have already:

* `gcc/g++/gfortran 6 <https://gcc.gnu.org/>`_ or above
* MPI compilers
* `gsl 1.16 <http://ftpmirror.gnu.org/gsl/>`_ or above
* `cfitsio 3.30 <http://heasarc.gsfc.nasa.gov/fitsio/fitsio.html>`_ or above
* `FFTW 3 <http://www.fftw.org/download.html>`_ 
* `lapack <http://www.netlib.org/lapack/>`_ (except on MacOS)
* `git <https://git-scm.com/downloads>`_ 
* `python 3.6 or above <https://www.python.org/downloads/>`_

First, export these environment variables:

* ``GSL_INC`` the path to GSL header files
* ``GSL_LIB`` the path to GSL library files
* ``CFITSIO_INC`` the path to CFTSIO header files
* ``CFITSIO_LIB`` the path to CFTSIO library files
* ``FFTW_LIBRARY`` the path to FFTW header files
* ``FFTW_INCLUDE_DIR`` the path to FFTW library files
* ``LAPACK_LINK`` whatever command line you need to link to LAPACK
* ``CXX`` Command for your C++ compiler
* ``CC`` Command for your C compiler
* ``FC`` Command for your Fortran compiler
* ``MPIFC`` Command for your MPI Fortran compiler
* ``COSMOSIS_ALT_COMPILERS=1``

and run::

    python -m venv ./env
    source env/bin/activate
    pip install cosmosis camb astropy fitsio cython scikit-learn fast-pt

Then clone and build the standard library repository::

    source cosomosis-configure
    git clone https://github.com/joezuntz/cosmosis-standard-library
    cd cosmosis-standard-library
    make

Please `open an issue <https://github.com/joezuntz/cosmosis/issues/new>`_ if you have installation problems.

The ``cosmosis-configure`` command can also set you up to use HomeBrew to install things: ``source cosmosis-configure --brew``
