The Maxlike sampler
--------------------------------------------------------------------

Find the maximum likelihood using various methods in scipy

+-------------+-----------------------------------------------------------------------------------------+
| Name        | maxlike                                                                                 |
+-------------+-----------------------------------------------------------------------------------------+
| Version     | 1.0                                                                                     |
+-------------+-----------------------------------------------------------------------------------------+
| Author(s)   | SciPy developers                                                                        |
+-------------+-----------------------------------------------------------------------------------------+
| URL         | http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.minimize.html |
+-------------+-----------------------------------------------------------------------------------------+
| Citation(s) |                                                                                         |
+-------------+-----------------------------------------------------------------------------------------+
| Parallelism | serial                                                                                  |
+-------------+-----------------------------------------------------------------------------------------+

This sampler attempts to find the single point in parameter space with the highest likelihood.  It wraps a variety of samplers from the scipy.minimize package.

These methods are all iterative and local, not global, so they can only find the  nearest local maximum likelihood point from the parameter starting position.

Maximum likelihood using these kinds of methods can be something of a dark art. Results can be quite sensitive to the starting position and exact parameters used, so if you need precision ML then you should carefully explore the robustness of your results.

These samplers are wrapped in the current version of scipy:

- Nelder-Mead

- Powell

- CG

- BFGS

- Newton-CG

- Anneal (deprecated by scipy)

- L-BFGS-B

- TNC

- COBYLA

- SLSQP

- dogleg

- trust-ncg

- bobyqa (requires pybobyqa)



Each has different (dis)advantages, and which works best will depend on your particular application.  The default in CosmoSIS is Nelder-Mead. See the references on the scipy URL above for more details.

Some methods can also output an estimated covariance matrix at the likelihood  peak.




Installation
============

Requires SciPy 0.14 or above.  This is installed by the CosmoSIS bootstrap, but if you are installing manually you can get it with the command:

pip install scipy  #to install centrally, may require sudo

pip install scipy --user #to install just for you




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| Name          | Type    | Default     | Description                                                                                                     |
+===============+=========+=============+=================================================================================================================+
| method        | string  | Nelder-Mead | The minimization method to use.                                                                                 |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| tolerance     | real    | 1e-3        | The tolerance parameter for termination.  Meaning depends on the sampler - see scipy docs.                      |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| maxiter       | integer | 1000        | Maximum number of iterations of the sampler                                                                     |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| output_ini    | string  | (empty)     | if present, save the resulting parameters to a new ini file with this name                                      |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| output_covmat | string  | (empty)     | if present and the sampler supports it, save the estimated covariance to this file                              |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| max_posterior | bool    | False       | find the max a posteriori point instead of max like (includes the priors as well)                               |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| repeats       | integer | 1           | number of times to repeat the minimization from different starting points                                       |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| start_method  | string  | (empty)     | method to use to generate starting points.  Options are 'prior' and 'chain', 'cov', or blank for default start' |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| start_input   | string  | (empty)     | input file to use for starting points if start_method is 'chain' or 'cov'                                       |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+
| nstep         | integer | 1           | number of steps to output at once                                                                               |
+---------------+---------+-------------+-----------------------------------------------------------------------------------------------------------------+


