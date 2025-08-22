Samplers
--------

Samplers are the different methods that CosmoSIS uses to choose points in parameter spaces to evaluate.

Some are designed to actually explore likelihood spaces; others are useful for testing and understanding likelihoods.

Simple Samplers
===============

.. toctree::
    :maxdepth: 1

     test: Evaluate a single parameter set and save all results <../reference/samplers/test>
     list: Evaluate a pre-made list of parameter sets <../reference/samplers/list>


MCMC Samplers
===============

.. toctree::
    :maxdepth: 1

     emcee: Ensemble walker sampling <../reference/samplers/emcee>
     zeus: Ensemble slice sampling <../reference/samplers/zeus>
     metropolis: Classic Metropolis-Hastings sampling <../reference/samplers/metropolis>
     pymc: PyMC integration <../reference/samplers/pymc>
     importance: Importance sampling <../reference/samplers/importance>
     kombine: Clustered KDE <../reference/samplers/kombine>
     pmc: Adaptive Importance Sampling <../reference/samplers/pmc>
     pocoMC: Preconditioned Monte Carlo for Accelerated Posterior and Evidence Estimation <../reference/samplers/pocomc>

Nested Samplers
===============

.. toctree::
    :maxdepth: 1

     multinest: Nested sampling for Bayesian Evidence <../reference/samplers/multinest>
     polychord: Ensemble nested sampling for Bayesian Evidence <../reference/samplers/polychord>
     nautilus: ML-enhanced nested sampling for Bayesian Evidence <../reference/samplers/nautilus>
     dynesty: Dynamic nested sampling for Bayesian Evidence <../reference/samplers/dynesty>


Optimizers
===============
     
.. toctree::
    :maxdepth: 1

     maxlike: Find the maximum likelihood using various methods in scipy <../reference/samplers/maxlike>
     pmaxlike: Parallel maximum likelihood estimation <../reference/samplers/pmaxlike>
     minuit sampler MPI-aware maxlike sampler from the ROOT package. <../reference/samplers/minuit>
     gridmax: Naive grid maximum-posterior <../reference/samplers/gridmax>


Grid Samplers
===============

.. toctree::
    :maxdepth: 1

     grid: Simple grid sampler <../reference/samplers/grid>
     snake: Intelligent Grid exploration <../reference/samplers/snake>


Specialist Samplers
===================

.. toctree::
    :maxdepth: 1

     fisher: Fisher matrix calculation <../reference/samplers/fisher>
     star: Simple star sampler <../reference/samplers/star>
     apriori: Draw samples from the prior and evaluate the likelihood <../reference/samplers/apriori>
     abc: Approximate Bayesian Computing <../reference/samplers/abc>

