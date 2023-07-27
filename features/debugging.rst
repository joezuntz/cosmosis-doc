Debugging
----------

CosmoSIS has a number of tools to help you debug problems with your analyses.


The Test Sampler
================

The first thing to try when debugging an MCMC failure is the test sampler - try to see if you can recreate the problem when running on a single parameter set.  Then you can switch on the options below for more information about the error.

You can set the parameter::

    [test]
    fatal_errors = T

to get more output on any error in the test sampler.

Parameter file options
======================

You can set several options in the CosmoSIS parameter file to find problems more easily:

.. code-block:: ini

    [runtime]
    verbosity = debug

    [pipeline]
    debug=T

Setting the verbosity to its maximum debug setting will print out lots of general information

Setting :code:`debug=T` will, after an error, print out a log of all the values saved to the CosmoSIS data block - if you are getting an error saying that some value has not been found in the block then this can be useful to figure out why.

Note that this setting prints out a lot of text *after* any other errors are reported, so you may need to scroll up past it to look for any other messages.

Python errors
=============

If you are finding a crash in a Python function then you can use the :code:`--pdb` flag on the command line to enter the `Python Debugger <https://docs.python.org/2/library/pdb.html#debugger-commands//>`_. When the program crashes you will be dropped into an interactive debugger shell and you can print the values of parameters or run functions to try to determine the source of the error::

    cosmosis my_params.ini --pdb

To do this in the test sampler you may need to set the parameter :code:`fatal_errors=T`  in the :code:`[test]` section of the parameter file.

This option doesn't work when running in parallel.

The STOP standard-library module
================================

The standard lib has a module called "stop", which you can use to pause your pipeline whenever it is reached and put you into the python debugger:

.. code-block:: ini

    [stop]
    file = cosmosis-standard-library/utility/stop/stop.py

You can then explore what data is in the block interactively.

Compiling in debug mode
=======================

You can compile all CosmoSIS code in debug mode to make finding errors in compiled code easier.  To do so, run these commands in the main directory::

    export COSMOSIS_DEBUG=1
    make clean
    make

Crashes in C/C++/Fortran code
=============================

If you are seeing a crash in C/C++/Fortran code you can use this command line flag  to try to track it down::

    cosmosis my_params.ini --segfaults

On a crash this should print out a traceback revealing in which function the error ocurred.


Special Samplers
================

CosmoSIS has several samplers that explore the parameter space in ways that help debug or compare to other code.

The *apriori* sampler samples points from throughout the prior.   It can be useful if your error is only triggered by extreme parameters.

The *list* sampler takes a list of parameter sets to evaluate one by one.  It can be useful if you have a set of possible parameters that might cause errors, or which you want to compare to another code.

The *star* sampler samples a set of 1D parameters slices in each parameter direction through the central point.  It can be useful to compare to the output of another code.



Memory monitoring
=================

If your code seems to be running out of memory, you can help track things down using this flag::

    cosmosis my_params.ini --mem 3

This will print a memory report every 3 seconds, telling you how much memory cosmosis has used (the physical memory).

This requires the ``psutil`` python module, which you can install with pip.

Profiling
=========

If your code is taking a long time to run, you can profile it to find out which functions are slow::

    cosmosis my_params.ini --profile profile.stats

This will print out a record of the time taken in each function, and also save it to profile.stats so you can explore it more later.

See the `Python Profiler documentation <https://docs.python.org/3/library/profile.html>`_ for more details of how to interpret the results.

