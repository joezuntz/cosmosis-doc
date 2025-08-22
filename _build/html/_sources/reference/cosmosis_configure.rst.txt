Command line flags for cosmosis-configure
-----------------------------------------

The :code:`cosmosis-configure` tool sets up your shell environment for building CosmoSIS and the standard library.

**Important**: This script must be sourced, not executed::

    source cosmosis-configure
    
    # NOT: cosmosis-configure

Purpose
=======

The configure script sets up environment variables needed to compile CosmoSIS modules and the standard library. It configures:

* Compiler settings and flags
* Library paths for dependencies  
* Build system variables
* Paths to CosmoSIS tools and utilities

This is required before building any CosmoSIS modules or before using :code:`make` in the CosmoSIS standard library.

Usage
=====

Source the configure script in your shell::

    source cosmosis-configure

You can also pass additional configuration options::

    source cosmosis-configure --compiler=gcc
    source cosmosis-configure --debug

The script will set up your environment and print a confirmation message when complete.

Configuration Options
=====================

The configure script supports various options to customize the build environment:

* Compiler selection
* Debug vs optimized builds  
* Custom library paths
* Platform-specific settings

Run with :code:`--help` to see all available options::

    python -m cosmosis.configure --help

Environment Variables Set
=========================

After sourcing the configure script, several environment variables will be set:

* **CC, CXX, FC**: Compiler commands
* **CFLAGS, CXXFLAGS, FFLAGS**: Compiler flags
* **LDFLAGS**: Linker flags  
* **COSMOSIS_SRC_DIR**: Path to CosmoSIS source
* **Various library paths**: For GSL, CFITSIO, FFTW, etc.

Note
====

You need to source this script in each new shell session where you plan to build CosmoSIS code. Many users add the source command to their :code:`.bashrc` or similar shell startup file.