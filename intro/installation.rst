Installing CosmoSIS
-------------------

Pip
===

If you only need CosmoSIS for its core sampling tools and datablock, and don't need the cosmological likelihoods, then you can install those with pip::

    pip install cosmosis


Conda-Forge (from scratch)
==========================

This is the easiest way to get the full CosmoSIS package. It downloads everything you need.  If the ``conda`` command works on your computer already, use the instructions for an existing installation (next section) instead. 

Otherwise first run one of these commands to download the installer:

On Linux::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh

On Intel Macs::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh

On Silicon Macs::

    wget -O Miniforge3.sh  https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh


    chmod +x Miniforge3.sh
    ./Miniforge3.sh -b -p ./env 
    source ./env/bin/activate
    conda install -y python=3.9 cosmosis cosmosis-build-standard-library
    source cosmosis-configure
    cosmosis-build-standard-library


This will make a new directory cosmosis-standard-library with the cosmology packages in.

Whenever you start a fresh terminal shell you need to run these commands to get set up again::

    conda activate ./env
    source cosmosis-configure



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

    git clone https://github.com/joezuntz/cosmosis-standard-library
    cd cosmosis-standard-library
    make

Please `open an issue <https://github.com/joezuntz/cosmosis/issues/new>`_ if you have installation problems.