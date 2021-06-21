Special Features
=================

CosmoSIS has several features that can help you out in building and running pipelines


Fast / Slow Sampling
--------------------

Some sampling methods can take advantage of a *speed hierarchy* in parameter spaces: in many models it is faster to re-calculate likelihoods if only certain ("fast") parameters are changed, by caching calculations that use *only* the other "slow" parameters.

CosmoSIS implements this by splitting the pipeline into a slow part and a fast part.  You can tell it where to make that split, and it will do everything else for you, and report on the speed-up.

You can activate fast/slow sampling using these parameters:

.. code-block:: ini

    [pipeline]
    ; This enables fast/slow sampling
    fast_slow = T

    ; This selects the first fast module.  If it is not specified
    ; one will be chosen automatically
    first_fast_module = name_of_module

The Fisher, Grid, Metropolis, Polychord, and Star samplers can take advantage of fast/slow sampling.


Resuming Sampling
-----------------

Several samplers can resume sampling if they are interrupted for some reason.

The Zeus, Emcee, and Metropolis samplers can be told to resume like this:

.. code-block:: ini

    [runtime]
    resume = T


and the Multinest and Polychord samplers can be resumed like this:

.. code-block:: ini

    [multinest]
    multinest_outfile_root = ./directory_to_save_progress
    resume = T

    [polychord]
    polychord_outfile_root = ./directory_to_save_progress
    resume = T


If a sampler is interrupted then simply re-run the same command again to resume sampling.  If no old sampling information is found then the job will start afresh (so it is fine to put ``resume=T`` on the first run).


Parameter Features
------------------

CosmoSIS has several features for modifying the values read from parameter and other files.


Command Line Environment Variables
**********************************

Parameter files in CosmoSIS can replace environment variables used in parameter files with their vaules.  Use curly brackets like this to do so:

.. code-block:: ini

    [runtime]
    sampler = ${SAMPLER}

In this case the sampler will be chosen depending on the environment variable ``$SAMPLER``.

Variables that are not found in the environment will not be replaced, so you should explicitly set empty values if that is what you want.


Default Parameters & Interpolation
**********************************

Files in the ``ini`` format have a standard feature that you can use in CosmoSIS: you can use the values of variables inside other variables.  For example, if you have a filename that you use repeatedly through a section, then you can specify it once and re-used it elsewhere.

They also have a special section called ``DEFAULT`` whose parameters are available throughout the file.  You can combine these like so:

.. code-block:: ini

    [DEFAULT]
    data_directory = path/to/data_file.fits

    ...

    [number_density]
    data_file = %(data_directory)s/number_density.fits

    ...

    [likelihood]
    data_file = %(data_directory)s/data.fits




Including other parameters files
********************************

CosmoSIS parameter files can use this command to incorporate another file into their contents:

.. code-block:: ini

    ...
    %include path_to_other.ini
    ...

This has the effect of "pasting" in the other file into the current one.  If you use a parameter in an ini file twice the later value will take precedence, so you depending where you put the include directive you can override previous parameters.

The path is looked up relative to the current working directory, not to the first parameter file.


Command Line Overrides
**********************


It can be useful to override parameters specified in the configuration files on the command line - this can let you launch a variety of different runs with the same file.  The :code:`-p` and :code:`-v` flags let you override parameters in the main (params.ini) and values files respectively.

You can override any number of parameters in the main parameter file like this::

    cosmosis params.ini -p section1.name1=value  section2.name2=value ...

For example, this command would change the sampler being used to emcee instead of its current value::

    cosmosis params.ini -p runtime.sampler=test

The :code:`-v` command is used exactly the same way but for the values file, for example, this would change one of the parameter ranges in demo 5::

    cosmosis demos/demo5.ini  -v cosmological_parameters.omega_m="0.2 0.3 0.5"

Note the quotations marks above, which are needed when there are spaces in the parameter value. 


