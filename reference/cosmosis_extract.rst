Command line flags for cosmosis-extract
---------------------------------------

The :code:`cosmosis-extract` tool extracts the original parameter files that were used to generate a CosmoSIS chain from the chain output file.

You can view command line flags for cosmosis-extract using the command::

    cosmosis-extract --help

Purpose
=======

When CosmoSIS runs, it saves copies of the parameter files used (params.ini, values.ini, priors.ini) in the header of the output chain file as comments. The :code:`cosmosis-extract` tool reads these embedded files and saves them as separate .ini files.

This is useful for:

* Reproducing previous results
* Understanding exactly what parameters were used for a particular run
* Debugging parameter settings
* Creating starting points for new analyses

Usage
=====

Extract parameter files from a chain::

    cosmosis-extract chain_file.txt output_prefix

This will create three files:

* :code:`output_prefix_params.ini` - The main parameter file
* :code:`output_prefix_values.ini` - The values/ranges file  
* :code:`output_prefix_priors.ini` - The priors file

Arguments
=========

* **chain**: Name of the chain file to read from
* **prefix**: Prefix for the output files that will be created

Example
=======

::

    cosmosis-extract output/demo1.txt recovered_demo1

This will create:

* :code:`recovered_demo1_params.ini`
* :code:`recovered_demo1_values.ini` 
* :code:`recovered_demo1_priors.ini`

You can then use these files to re-run the same analysis::

    cosmosis recovered_demo1_params.ini