Samplers
--------

Samplers are the different methods that CosmoSIS uses to choose points in parameter spaces to evaluate.

Some are designed to actually explore likelihood spaces; others are useful for testing and understanding likelihoods.

Simple Samplers
===============

.. toctree::
    :maxdepth: 1

     test: Evaluate a single parameter set and save all results<test>
     list: Evaluate a pre-made list of parameter sets <list>


MCMC Samplers
===============

.. toctree::
    :maxdepth: 1

     emcee: Ensemble walker sampling <emcee>
     metropolis: Classic Metropolis-Hastings sampling <metropolis>
     multinest: Nested sampling for Bayesian Evidence <multinest>
     polychord: Ensemble nested sampling for Bayesian Evidence <polychord>
     importance: Importance sampling <importance>
     kombine: Clustered KDE <kombine>
     pmc: Adaptive Importance Sampling <pmc>

Optimizers
===============
     
.. toctree::
    :maxdepth: 1

     maxlike: Find the maximum likelihood using various methods in scipy <maxlike>
     minuit sampler MPI-aware maxlike sampler from the ROOT package. <minuit>
     gridmax: Naive grid maximum-posterior <gridmax>


Grid Samplers
===============

.. toctree::
    :maxdepth: 1

     grid: Simple grid sampler <grid>
     snake: Intelligent Grid exploration <snake>


Specialist Samplers
===============

.. toctree::
    :maxdepth: 1

     fisher: Fisher matrix calculation <fisher>
     star: Simple star sampler <star>
     apriori: Draw samples from the prior and evaluate the likelihood <apriori>

