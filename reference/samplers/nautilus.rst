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

+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| Name                | Type                | Default   | Description                                                                     |
+=====================+=====================+===========+=================================================================================+
| n_live              | integer             | 2000      | number of live points                                                           |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| n_update            | integer             | n_live    | number of additions to the live set before a new bound is created               |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| enlarge_per_dim     | float               | 1.1       | factor by which ellipsoidal bounds are increased in each dimension              |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| n_points_min        | integer             | 50+n_dim  | minimum number of points for constructing a bounding ellipsoid                  |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| split_threshold     | float               | 100       | volume threshold for splitting bounding ellipsoids                              |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| n_networks          | integer             | 4         | number of neural networks in each network ensemble                              |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| n_batch             | integer             | 100       | number of likelihood evaluations that are performed at each step                |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| seed                | integer, default=-1 |           | random seed, no fixed seed is used if negative                                  |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| filepath            | string              | 'None'    | file used for checkpointing, must have .hdf5 ending                             |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| resume              | bool                | False     | if True, resume from previous run stored in `filepath`                          |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| f_live              | float               | 0.01      | live set evidence fraction when exploration phase terminates                    |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| n_shell             | int                 | n_batch   | minimum number of points in each shell                                          |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| n_eff               | float               | 10000.0   | minimum effective sample size                                                   |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| n_like_max          | int                 | -1        | maximum number of likelihood calls, negative values are interpreted as infinity |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| discard_exploration | bool                | False     | whether to discard points drawn in the exploration phase                        |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+
| verbose             | bool                | False     | If true, print information about sampler progress                               |
+---------------------+---------------------+-----------+---------------------------------------------------------------------------------+


