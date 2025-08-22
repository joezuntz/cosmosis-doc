pmaxlike: Parallel Maximum Likelihood
====================================

The pmaxlike sampler finds the maximum likelihood point in parameter space using gradient-based optimization methods from scipy.optimize, with parallel computing support and automatic numerical gradient computation.

Attribution
-----------
* CosmoSIS Team
* SciPy developers

Installation
------------
Requires SciPy 0.14 or above. This is installed by the CosmoSIS bootstrap, but if you are installing manually you can get it with::

    pip install scipy  # to install centrally, may require sudo
    
    pip install scipy --user  # to install just for you

Purpose
-------
This sampler finds the maximum likelihood point in parameter space using gradient-based optimization methods from scipy.optimize. Unlike the serial maxlike sampler, this version can run in parallel and automatically computes gradients numerically using finite differences.

The pmaxlike sampler is particularly useful when you have a smooth likelihood surface and want to leverage parallel computing to accelerate the optimization. It normalizes parameters to the range [0,1] before optimization to improve numerical stability.

The sampler computes both the posterior value and its gradient at each evaluation point, making it more efficient for gradient-based optimization methods like conjugate gradient (CG) or BFGS.

How to Use
----------
The pmaxlike sampler uses scipy optimization methods and is well-suited for finding the best-fit parameters when you have a reasonably smooth likelihood surface and want to use parallel computing.

Parameters
==========

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name           | Type    | Default   | Description                                                                                                                                                             |
+================+=========+===========+=========================================================================================================================================================================+
| method         | string  | CG        | The optimization method to use. Options include CG, BFGS, L-BFGS-B, etc.                                                                                              |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tolerance      | real    | 1e-3      | Tolerance for termination of the optimization algorithm                                                                                                                |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| maxiter        | integer | 1000      | Maximum number of iterations for the optimization                                                                                                                      |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| output_ini     | string  | (empty)   | If present, save the resulting parameters to a new ini file with this name                                                                                            |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| output_covmat  | string  | (empty)   | If present, save the estimated covariance matrix to this file                                                                                                         |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| gradient_epsilon | real  | 1e-9      | Step size for numerical gradient computation                                                                                                                           |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| gradient_tolerance | real | 1e-5     | Tolerance for gradient convergence criterion                                                                                                                           |
+----------------+---------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+