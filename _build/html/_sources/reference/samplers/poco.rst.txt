The Poco sampler
--------------------------------------------------------------------

Preconditioned Monte Carlo with normalizing flows

+-------------+-----------------------------------------------------------------------------+
| Name        | poco                                                                        |
+-------------+-----------------------------------------------------------------------------+
| Version     | 0.1.1                                                                       |
+-------------+-----------------------------------------------------------------------------+
| Author(s)   | Minas Karamanis, David Nabergoj, Florian Beutler, John Peacock, Uros Seljak |
+-------------+-----------------------------------------------------------------------------+
| URL         | https://pocomc.readthedocs.io/                                              |
+-------------+-----------------------------------------------------------------------------+
| Citation(s) | https://arxiv.org/abs/2207.05660, https://arxiv.org/abs/2207.05652          |
+-------------+-----------------------------------------------------------------------------+
| Parallelism | parallel                                                                    |
+-------------+-----------------------------------------------------------------------------+

pocoMC relies on the Preconditioned Monte Carlo algorithm which utilises a Normalising Flow  in order to decorrelate the parameters of the posterior, and facilitates efficient sampling  of probability distributions with non-trivial geometries.

It generates both posterior samples and Bayesian evidences.

PocoMC does not currently support checkpointing (all the output appears at the end of the run) or derived parameters.




Installation
============

if using conda, do this first to ensure consistent dependencies:

    conda install -c conda-forge corner pytorch tqdm

pip install pocomc




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| Name        | Type    | Description                                                                                                                                                   | Default   |
+=============+=========+===============================================================================================================================================================+===========+
| n_particles | integer | Number of particles/walkers                                                                                                                                   |           |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| nsample_add | integer | Number of extra posterior samples to draw at the end                                                                                                          | 0         |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| threshold   | float   | The threshold value for the (normalised) proposal scale parameter below which normalising flow preconditioning (NFP) is enabled. Default is to always enable. | 1.0       |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| scale       | bool    | Whether to scale the distribution of particles to have zero mean and unit variance                                                                            | N         |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| rescale     | bool    | Whether to rescale the distribution of particles to have zero mean and unit variance in every iteration                                                       | N         |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| diagonal    | bool    | Use a diagonal covariance matrix when rescaling instead of a full covariance                                                                                  | T         |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| ess         | float   | The effective sample size maintained during the run                                                                                                           | 0.95      |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| gamma       | float   | Threshold for the correlation coefficient that is used to adaptively determine the number of MCMC steps                                                       | 0.75      |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| n_min       | int     | Minimum number of MCMC steps per iteration                                                                                                                    | ndim/2    |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| n_max       | int     | Maximum number of MCMC steps per iteration                                                                                                                    | ndim*10   |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| seed        | int     | A random seed for reproducibility. Default is to generate automatically.                                                                                      | 0         |
+-------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+


