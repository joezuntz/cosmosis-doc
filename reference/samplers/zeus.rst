zeus: Ensemble Slice Sampling
============================

Zeus is a pure-Python implementation of the Ensemble Slice Sampling method that can sample from multimodal and highly correlated distributions that are difficult for traditional MCMC methods.

Attribution
-----------
* Minas Karamanis and contributors

Installation
------------
Zeus needs to be installed separately::

    pip install zeus-mcmc  # to install centrally, may require sudo
    
    pip install zeus-mcmc --user  # to install just for you

Purpose
-------
Zeus is a pure-Python implementation of the Ensemble Slice Sampling method. It can be used to sample from multimodal and highly correlated distributions that are difficult for traditional MCMC methods.

Zeus uses an ensemble of walkers that explore the parameter space using slice sampling, which automatically adapts to the local structure of the distribution. This makes it particularly effective for complex posterior distributions common in cosmological parameter estimation.

The total number of samples generated will be walkers × samples.

How to Use
----------
Zeus uses an ensemble of walkers similar to emcee, but with slice sampling for the individual steps. This often provides better performance on highly correlated or multimodal distributions.

Parameters
==========

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name           | Type    | Default   | Description                                                                                                                                                             |
+================+=========+===========+=========================================================================================================================================================================+
| walkers        | integer |           | Number of walkers in the ensemble (required)                                                                                                                           |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| samples        | integer |           | Number of samples to generate per walker (required)                                                                                                                    |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nsteps         | integer | 50        | Number of sample steps taken in between writing output                                                                                                                 |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| random_start   | boolean | F         | Whether to start walkers at random points in the prior                                                                                                                 |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| start_points   | string  | (empty)   | File containing starting points for the walkers                                                                                                                        |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| covmat         | string  | (empty)   | File containing covariance matrix for initializing walkers                                                                                                             |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| moves          | string  | differential | Type of moves to use for sampling                                                                                                                                   |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tune           | boolean | T         | Whether to tune the sampler parameters during burn-in                                                                                                                  |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tolerance      | real    | 0.05      | Tolerance for tuning convergence                                                                                                                                       |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| maxsteps       | integer | 10000     | Maximum number of steps for tuning                                                                                                                                     |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| patience       | integer | 5         | Patience parameter for tuning convergence                                                                                                                              |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| maxiter        | integer | 10000     | Maximum number of iterations for sampling                                                                                                                              |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| verbose        | boolean | F         | Whether to print verbose output during sampling                                                                                                                        |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

References
==========
* Karamanis, M., et al. "zeus: A Python implementation of ensemble slice sampling for efficient Bayesian parameter inference", MNRAS, 508, 3589-3603, 2021