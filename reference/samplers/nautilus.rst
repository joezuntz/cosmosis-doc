The Nautilus sampler
--------------------------------------------------------------------

Neural Network-Boosted Importance Nested Sampling

+-------------+-----------------------------------------+
| Name        | nautilus                                |
+-------------+-----------------------------------------+
| Version     | 0.7.0                                   |
+-------------+-----------------------------------------+
| Author(s)   | Johannes U. Lange                       |
+-------------+-----------------------------------------+
| URL         | https://github.com/johannesulf/nautilus |
+-------------+-----------------------------------------+
| Citation(s) | https://arxiv.org/abs/2306.16923        |
+-------------+-----------------------------------------+
| Parallelism | parallel                                |
+-------------+-----------------------------------------+

Nautilus is an MIT-licensed pure-Python package for Bayesian posterior and evidence estimation. It utilizes importance sampling and efficient space exploration using neural networks. Compared to traditional MCMC and Nested Sampling codes, it often needs fewer likelihood calls and produces much larger posterior samples. Additionally, nautilus is highly accurate and can produce Bayesian evidence estimates with percent precision.




Installation
============

pip install nautilus-sampler conda install -c conda-forge nautilus-sampler




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| Name                | Type                | Description                                                                     | Default   |
+=====================+=====================+=================================================================================+===========+
| n_live              | integer             | number of live points                                                           | 2000      |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| n_update            | integer             | number of additions to the live set before a new bound is created               | n_live    |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| enlarge_per_dim     | float               | factor by which ellipsoidal bounds are increased in each dimension              | 1.1       |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| n_points_min        | integer             | minimum number of points for constructing a bounding ellipsoid                  | 50+n_dim  |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| split_threshold     | float               | volume threshold for splitting bounding ellipsoids                              | 100       |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| n_networks          | integer             | number of neural networks in each network ensemble                              | 4         |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| n_batch             | integer             | number of likelihood evaluations that are performed at each step                | 100       |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| seed                | integer, default=-1 | random seed, no fixed seed is used if negative                                  |           |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| filepath            | string              | file used for checkpointing, must have .hdf5 ending                             | 'None'    |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| resume              | bool                | if True, resume from previous run stored in `filepath`                          | False     |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| f_live              | float               | live set evidence fraction when exploration phase terminates                    | 0.01      |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| n_shell             | int                 | minimum number of points in each shell                                          | n_batch   |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| n_eff               | float               | minimum effective sample size                                                   | 10000.0   |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| n_like_max          | int                 | maximum number of likelihood calls, negative values are interpreted as infinity | -1        |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| discard_exploration | bool                | whether to discard points drawn in the exploration phase                        | False     |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+
| verbose             | bool                | If true, print information about sampler progress                               | False     |
+---------------------+---------------------+---------------------------------------------------------------------------------+-----------+


