The Minuit sampler
--------------------------------------------------------------------

Find the maximum posterior using the MINUIT library

+-------------+------------------------------------------------------+
| Name        | minuit                                               |
+-------------+------------------------------------------------------+
| Version     | 1.0                                                  |
+-------------+------------------------------------------------------+
| Author(s)   | SciPy developers                                     |
+-------------+------------------------------------------------------+
| URL         | https://seal.web.cern.ch/seal/MathLibs/Minuit2/html/ |
+-------------+------------------------------------------------------+
| Citation(s) |                                                      |
+-------------+------------------------------------------------------+
| Parallelism | serial                                               |
+-------------+------------------------------------------------------+

This sampler attempts to find the single point in parameter space with the highest posterior probability.  It is a wrapper around the powerful MINUIT2 library that is widely used in particle physics.

Minuit is one of the more robust optimizers, but you should still try starting the sampler from a few different points to make sure they converge to the same place.

By default this wrapper uses the MIGRAD algorithm, which is pretty robust unless  there are sharp edges in the parameter space.  It also re-parameterizes so that the formal parameter edges (the limits in your values file) are shifted to +- infinity.

At the end of the sampling a covariance estimate is also returned.

Note on parallelism: The minuit2 sampler can be used in parallel, but the version that is packaged with the CosmoSIS auto-installer does not support that yet, so at the moment we are only supporting serial sampling (no MPI).




Installation
============

Requires the Minuit2 library. the auto-installer includes Minuit2, but if you are installing manually you may need to download and install from your package manager or the URL above. You will also need to set the MINUIT2_INC and MINUIT2_LIB environment variables in your setup script to point to the directories of the minuit2 headers and libraries respectively. (The minuit2 headers directory has two subdirectories, called Minuit2 and Math. The MINUIT2_INC should point to the parent directory, not the subdir).




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| Name           | Type    | Description                                                                                                                                                             | Default   |
+================+=========+=========================================================================================================================================================================+===========+
| maxiter        | integer | Maximum number of likelihood calculations to do                                                                                                                         | 1000      |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| width_estimate | float   | A guess of the parameter posterior widths as a fraction of their range. Can speed convergence the more accurate it is but does not need to be very exact.               | 0.05      |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| tolerance      | real    | The tolerance parameter in milliSigmas - the default setting will try to get within 0.05 sigma of the best-fit.                                                         | 0.05      |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| save_dir       | string  | If set, save the data block containing the cosmology at the best-fit point to this directory name                                                                       | (empty)   |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| output_ini     | string  | if present, save the resulting parameters to a new ini file with this name                                                                                              | (empty)   |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| save_cov       | string  | if present and the sampler supports it, save the estimated covariance to this file                                                                                      | (empty)   |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| verbose        | bool    | Print more information to the command line.                                                                                                                             | F         |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| strategy       | string  | Choose from fast, medium, and safe. Safe mode means slower convergence but less chance of failure. Fast means the opposite.                                             | medium    |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| algorithm      | string  | Choose from migrad, simplex, and fallback. Migrad is better unless there are strange parameter space cliffs. Fallback tries migrad first and if it fails tries simplex. | migrad    |
+----------------+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+


