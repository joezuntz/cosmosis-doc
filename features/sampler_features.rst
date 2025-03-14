Sampler Features
=================

CosmoSIS has several features that can help you out in building and running pipelines




Derived Parameters
------------------

Often you want to sample in one parameter but plot results in a different, derived parameter.

In CosmoSIS, you add a listing of any parameters you want in the :code:`extra_output` parameter:

.. code-block:: ini

    [pipeline]
    extra_output = distances/age

This will add a new output column, containing the value found in the :code:`age` value in the :code:`distances` section of the datablock.  If it is not found, :code:`NaN` will be shown.

If the value you want is a vector, then you need to find out first how long the vector is, and then specify that with a :code:`#` in the parameter, for example:

.. code-block:: ini

    [pipeline]
    extra_output = data_vector/2pt_theory#457

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

The Fisher, Grid, Metropolis, Multinest, Polychord, and Star samplers can take advantage of fast/slow sampling.


Resuming Sampling
-----------------

Several samplers can resume sampling if they are interrupted for some reason.

The Zeus, Emcee, Multinest, Polychord, Nautilus, and Metropolis samplers can be told to resume like this:

.. code-block:: ini

    [runtime]
    resume = T


The Multinest and Polychord need to be told an output file root to enable this:

.. code-block:: ini

    [multinest]
    multinest_outfile_root = ./directory_to_save_progress

    [polychord]
    polychord_outfile_root = ./directory_to_save_progress


If a sampler is interrupted then simply re-run the same command again to resume sampling.  If no old sampling information is found then the job will start afresh (so it is fine to put ``resume=T`` on the first run).



Sampler Chaining
----------------

You can specify a sequence of samplers in the ``sampler`` parameters in the ``[runtime]`` section to run one pipeline after the other; each imports a set of basic information from the previous one.  For example, you could do this:

.. code-block:: ini

    [runtime]
    sampler = maxlike  fisher  emcee

to:
- find the best-fitting point
- compute the fisher matrix approximation to the covariance at that point
- initialise emcee walkers from that covariance

Currently only a best-fit estimate and covariance estimate are passed to the next sampler; if you can think of more then please open an issue.

Starting points
---------------

Several samplers share a common set of parameters that are used to control the starting point of the algorithm.  They are:
- maxlike
- minuit
- zeus
- emcee
- fisher
- test

All these samplers can take the following parameters:

- `start_method`: takes one of the following values to determine how to start the chain
    - `chain-sample` - choose a random sample from a previous chain file (weighted if the chain has weights)
    - `chain-maxpost` - choose the maximum-posterior point from a previous chain file
    - `chain-maxlike` - choose the maximum-likelihood point from a previous chain file
    - `chain` - decide from the above three options based on the file contents and requirements
    - `chain-last` - choose the last point from a previous chain file
    - `prior` - chooise a random point from the prior distribution
    - `cov` - load the specified covariance matrix and choose a random point from the multivariate Gaussian defined by it
- `start_input`: for the choices of `start_method` the begin from an input file, this is the name of the file to read.

All of these methods are superseded if using sampler chaining (see above) and the previous sampler has recorded a best-fitting point.
