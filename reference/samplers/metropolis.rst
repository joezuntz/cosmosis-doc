The Metropolis sampler
--------------------------------------------------------------------

Classic Metropolis-Hastings sampling

+-------------+---------------------------------------------------+
| Name        | metropolis                                        |
+-------------+---------------------------------------------------+
| Version     | 1.0                                               |
+-------------+---------------------------------------------------+
| Author(s)   | CosmoSIS Team                                     |
+-------------+---------------------------------------------------+
| URL         | https://bitbucket.org/joezuntz/cosmosis           |
+-------------+---------------------------------------------------+
| Citation(s) | Journal of Chemical Physics 21 6 1087-1092 (1953) |
+-------------+---------------------------------------------------+
| Parallelism | multi-serial                                      |
+-------------+---------------------------------------------------+

Metropolis-Hastings is the classic Monte-Carlo Markov Chain method for sampling from distributions.

MH as a Markov process where from each point in chain there is a process for choosing the next point in such a way that the distribution of chain points tends to the underlying distribution.

In MH a proposal function is defined that suggests a possible next point in the chain.  The posterior of that point is evaluated and if: P_new / P_old > U[0,1] where U[0,1] is a random number from 0-1, then the new point is 'accepted' and becomes the next chain element.  Otherwise the current point is repeated.

The choice of proposal function strongly determines how quickly the sampler converges to the underlying distribution.  In particular a covariance matrix approximately describing the distribution provides a significant speed up.

The CosmoSIS metropolis sampler tries to mirror the CosmoMC MH implementation.

Metropolis-Hastings is intrinsically a serial (non-parallel) algorithm. Like CosmoMC, CosmoSIS parallelizes it by running several independent chains in parallel and comparing them to assess convergence using the Gelman-Rubin test.




Installation
============

No special installation required; everything is packaged with CosmoSIS




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| Name                    | Type            | Description                                                                                                               | Default   |
+=========================+=================+===========================================================================================================================+===========+
| samples                 | integer         | number of steps                                                                                                           |           |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| random_start            | bool            | whether to start the chains at random points in the prior instead of the ini file start                                   | N         |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| covmat_sample_start     | bool, default=N | start from random points sampled from the covariance matrix                                                               |           |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| Rconverge               | float           | when multiple chains are run, use this as the Gelman-Rubin statistic                                                      | -1.0      |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| covmat                  | string          | load a covariance matrix from this file.  The parameter order should match the order of varied parameters in the ini file | (empty)   |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| nsteps                  | integer         | number of points between saving data and testing convergence                                                              | 100       |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| tuning_frequency        | int             | How often to update the proposal during the tuning period                                                                 | -1        |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| tuning_grace            | int             | Number of samples before starting the tuning period                                                                       | 5000      |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| tuning_end              | int             | Number of samples before ending the tuning period                                                                         | 100000    |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+
| exponential_probability | float           | Fraction of an exponential proposal to mix into the Gaussian                                                              | 0.333     |
+-------------------------+-----------------+---------------------------------------------------------------------------------------------------------------------------+-----------+


