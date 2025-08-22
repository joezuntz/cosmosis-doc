pymc: PyMC Integration
======================

The pymc sampler provides integration with PyMC (version 2.x) for Bayesian parameter estimation using various MCMC algorithms including adaptive Metropolis-Hastings.

Attribution
-----------
* CosmoSIS Team  
* PyMC developers

Installation
------------
Requires PyMC 2.x. Note that this sampler is designed for PyMC 2.x, not the newer PyMC3/PyMC versions::

    pip install pymc  # to install centrally, may require sudo
    
    pip install pymc --user  # to install just for you

Purpose
-------
This sampler provides integration between CosmoSIS and PyMC 2.x, allowing you to use PyMC's MCMC algorithms for parameter estimation. PyMC provides sophisticated MCMC methods including adaptive Metropolis-Hastings that can automatically tune step sizes and proposal distributions.

The sampler supports various prior distributions (uniform, Gaussian, exponential) and can use covariance matrices to improve sampling efficiency. It also includes convergence diagnostics using the Gelman-Rubin statistic for parallel chains.

How to Use
----------
The PyMC sampler automatically converts CosmoSIS parameter specifications into PyMC stochastic variables and runs MCMC sampling using PyMC's algorithms.

Parameters
==========

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name           | Type    | Default   | Description                                                                                                                                                             |
+================+=========+===========+=========================================================================================================================================================================+
| samples        | integer | 1000      | Total number of MCMC samples to generate                                                                                                                               |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nsteps         | integer | 100       | Number of MCMC steps to take between output writes                                                                                                                     |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| burn_fraction  | real    | 0.0       | Fraction of samples to discard as burn-in, or if ≥1 then number of burn-in samples                                                                                   |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| adaptive_mcmc  | boolean | F         | Whether to use adaptive Metropolis-Hastings that tunes proposal distributions                                                                                         |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| covmat         | string  | (empty)   | File containing covariance matrix for initializing proposal distributions                                                                                             |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Rconverge      | real    | -1.0      | Convergence criterion for Gelman-Rubin statistic. If >0, chains are considered converged when R-1 < Rconverge for all parameters                                   |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note
----
This sampler is designed for PyMC 2.x and may not work with newer versions of PyMC (PyMC3, PyMC4, etc.). For modern PyMC integration, consider using other samplers or contact the CosmoSIS team.