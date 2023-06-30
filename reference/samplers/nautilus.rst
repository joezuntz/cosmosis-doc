The Nautilus sampler
--------------------------------------------------------------------

Neural Network-Boosted Importance Nested Sampling

+-------------+------------------------------------------------------------------------------------------------+
| Name        | nautilus                                                                                       |
+-------------+------------------------------------------------------------------------------------------------+
| Version     | 0.4.1                                                                                          |
+-------------+------------------------------------------------------------------------------------------------+
| Author(s)   | Johannes U. Lange                                                                              |
+-------------+------------------------------------------------------------------------------------------------+
| URL         | https://github.com/johannesulf/nautilus                                                        |
+-------------+------------------------------------------------------------------------------------------------+
| Citation(s) | h, t, t, p, s, :, /, /, a, r, x, i, v, ., o, r, g, /, a, b, s, /, 2, 3, 0, 6, ., 1, 6, 9, 2, 3 |
+-------------+------------------------------------------------------------------------------------------------+
| Parallelism | parallel                                                                                       |
+-------------+------------------------------------------------------------------------------------------------+

Nautilus is an MIT-licensed pure-Python package for Bayesian posterior and evidence estimation. It utilizes importance sampling and efficient space exploration using neural networks. Compared to traditional MCMC and Nested Sampling codes, it often needs fewer likelihood calls and produces much larger posterior samples. Additionally, nautilus is highly accurate and can produce Bayesian evidence estimates with percent precision.




Installation
============

pip install nautilus-sampler conda install -c conda-forge nautilus-sampler




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+---------------------+---------+-------------------------------------------------------------------+-----------+
| Name                | Type    | Description                                                       | Default   |
+=====================+=========+===================================================================+===========+
| n_live              | integer | number of live points                                             | 1500      |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| n_update            | integer | number of additions to the live set before a new bound is created | n_live    |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| enlarge             | float   | factor by which the volume of ellipsoidal bounds is increased     | 1.1*n_dim |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| n_batch             | integer | number of likelihood evaluations that are performed at each step  | 100       |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| random_state        | int     | random seed, negative values give a random random seed            | -1        |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| filepath            | string  | file used for checkpointing, must have .hdf5 ending               | 'None'    |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| resume              | bool    | if True, resume from previous run stored in `filepath`            | True      |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| f_live              | float   | live set evidence fraction when exploration phase terminates      | 0.01      |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| n_shell             | int     | minimum number of points in each shell                            | n_batch   |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| n_eff               | float   | minimum effective sample size                                     | 10000.0   |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| discard_exploration | bool    | whether to discard points drawn in the exploration phase          | False     |
+---------------------+---------+-------------------------------------------------------------------+-----------+
| verbose             | bool    | If true, print information about sampler progress                 | False     |
+---------------------+---------+-------------------------------------------------------------------+-----------+


