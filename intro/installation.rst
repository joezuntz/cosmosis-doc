Installing CosmoSIS
-------------------

Pip
===

If you only need CosmoSIS for its core sampling tools and datablock, and don't need the cosmological likelihoods, then you can install those with pip::

    pip install cosmosis


Conda-Forge
===========

The easiest way to install the full CosmoSIS package is with conda-forge.

You can create a new environment and install cosmosis tools in it with::

    conda create -p ./env -c conda-forge cosmosis cosmosis-build-standard-library
    conda activate ./env
    source cosmosis-configure
    cosmosis-build-standard-library

This will make a new directory cosmosis-standard-library with the cosmology packages in.

Whenever you start a fresh terminal shell you need to run these commands to get set up again::

    conda activate ./env
    source cosmosis-configure

