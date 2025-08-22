abc: Approximate Bayesian Computing Population Monte Carlo
==========================================================

Approximate Bayesian Computing (ABC) is a likelihood-free method for parameter estimation that uses a model to simulate datasets given parameters and retains parameter values based on a distance metric between simulated and observed data.

Attribution
-----------
* Joel Akeret and contributors

Installation
------------
abc requires the abcpmc python library::

    pip install abcpmc  # to install centrally, may require sudo
    
    pip install abcpmc --user  # to install just for you

Purpose
-------
abcpmc is a Python implementation of Approximate Bayesian Computing (ABC) Population Monte Carlo (PMC) based on Sequential Monte Carlo (SMC) with Particle Filtering techniques. 

This likelihood-free implementation estimates the posterior distribution using a model to simulate a dataset given a set of parameters. A distance metric ρ is used to determine similarity between the model and data, and parameter values are retained if ρ(model,data) < ε. This ε threshold can be fixed or modified (linearly or exponentially) every iteration.

The sampler uses a set of N particles to explore parameter space θ. On the first iteration (t=0), these are chosen from the prior. On subsequent iterations t, another N particles are selected with a perturbation kernel K(θ(t) | θ(t-1)) using twice the weighted covariance matrix.

How to Use
----------
This implementation requires an understanding of how ABC sampling works. We recommend contacting the CosmoSIS team for specific implementation questions.

Parameters
==========

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name           | Type    | Default   | Description                                                                                                                                                             |
+================+=========+===========+=========================================================================================================================================================================+
| npart          | integer |           | Number of particles to use in the sampling                                                                                                                             |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| threshold      | string  | LinearEps | Threshold implementation method. Options: LinearEps, ConstEps, ExpEps                                                                                                  |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| epimax         | double  | 5.0       | Epsilon value at iteration t=0                                                                                                                                         |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| epimin         | double  | 1.0       | Epsilon value at final iteration t=T                                                                                                                                   |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| niter          | integer | 2         | Number of iterations T                                                                                                                                                  |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| particle_prop  | string  | weighted_cov | Particle proposal kernel. Options: weighted_cov, KNN, OLCM                                                                                                         |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| num_nn         | integer | 10        | Number of neighbors when using particle_prop = KNN                                                                                                                     |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| set_prior      | string  | Gaussian  | Prior distribution type. Options: Gaussian, uniform                                                                                                                    |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| run_multigauss | boolean | F         | Generate multigaussian test data                                                                                                                                       |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ngauss         | integer | 4         | Dimension of multigaussian if run_multigauss = T                                                                                                                       |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| metric         | string  | chi2      | Distance metric. Options: mean, chi2, or "other" (requires distance_func)                                                                                             |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| distance_func  | string  | (empty)   | Custom distance function definition when metric = "other"                                                                                                              |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| param_cov_file | string  | (empty)   | Parameter covariance file for the prior                                                                                                                                |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| diag_cov       | boolean | F         | Use diagonal covariance matrix                                                                                                                                          |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

References
==========
* Akeret, J., Refregier, A., Amara, A, Seehars, S., and Hasner, C., JCAP (submitted 2015)
* Beaumont et al. 2009 arXiv:0805.2256
* Fillippi et al 2012 arXiv:1106.6280