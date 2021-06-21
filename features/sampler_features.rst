Sampler Features
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

Currently only a best-fit estimate and covariance estimate are passed to the next sampler; please open an issue if you can think of more then please open an issue.
