dynesty: Dynamic Nested Sampling
================================

dynesty provides both static and dynamic nested sampling algorithms to explore complex posterior distributions and estimate Bayesian evidence, with dynamic allocation of sampling effort to regions of highest posterior density.

Attribution
-----------
* Josh Speagle and contributors

Installation
------------
dynesty is included in the cosmosis bootstrap, but if you are installing manually you can get dynesty using::

    pip install dynesty  # to install centrally, may require sudo
    
    pip install dynesty --user  # to install just for you

Purpose
-------
dynesty is a pure-Python package for estimating Bayesian posteriors and evidences via Dynamic Nested Sampling. It provides both static and dynamic nested sampling algorithms to explore complex posterior distributions and estimate Bayesian evidence.

Dynamic nested sampling adaptively allocates sampling effort to regions of highest posterior density, making it particularly effective for multi-modal or highly constrained problems. This makes it well-suited for cosmological parameter estimation where the posterior may have complex structure.

How to Use
----------
The dynesty sampler in CosmoSIS supports both static and dynamic nested sampling modes. The dynamic mode is generally preferred as it adapts the sampling strategy during the run.

Parameters
==========

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name           | Type    | Default   | Description                                                                                                                                                             |
+================+=========+===========+=========================================================================================================================================================================+
| mode           | string  | static    | Nested sampling mode. Options: "static", "dynamic"                                                                                                                     |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| nlive          | integer | 500       | Number of live points to use in the nested sampling algorithm                                                                                                          |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| bound          | string  | multi     | Bounding method. Options: "none", "single", "multi", "balls", "cube"                                                                                                  |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sample         | string  | auto      | Sampling method. Options: "unif", "rwalk", "slice", "rslice", "hslice", "auto"                                                                                        |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| update_interval| real    | 0.6       | Fraction of the evidence to use for updating bounds                                                                                                                    |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min_ncall      | integer | 2*nlive   | Minimum number of likelihood calls                                                                                                                                     |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min_eff        | real    | 10.0      | Minimum sampling efficiency                                                                                                                                             |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| queue_size     | integer | (varies)  | Size of the proposal queue for parallel sampling                                                                                                                       |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| parallel_prior | boolean | T         | Whether to evaluate priors in parallel                                                                                                                                 |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max_call       | integer | (very large) | Maximum number of likelihood calls                                                                                                                                   |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dlogz          | real    | 0.01      | Stopping criterion for evidence convergence                                                                                                                            |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| print_progress | boolean | (varies)  | Whether to print progress information                                                                                                                                   |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

References
==========
* Speagle, J.S., "dynesty: A Dynamic Nested Sampling Package for Estimating Bayesian Posteriors and Evidences", arXiv:1904.02180