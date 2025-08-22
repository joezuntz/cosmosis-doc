tdcosmo
================================================

Likelihood of the TDCOSMO IV analysis

+-------------+----------------------------------------------------------------------------+
| File        | likelihood/tdcosmo/tdcosmo_likelihood.py                                   |
+-------------+----------------------------------------------------------------------------+
| Attribution | TDCOSMO IV (Birrer et al.) for the measurement                             |
+-------------+----------------------------------------------------------------------------+
|             | Martin Millon, Judit Prat and Simon Birrer for the cosmoSIS implementation |
+-------------+----------------------------------------------------------------------------+
| URL         | 10.1051/0004-6361/202038861                                                |
+-------------+----------------------------------------------------------------------------+
| Citations   | Birrer et al., 2020, A&A, 643, A165                                        |
+-------------+----------------------------------------------------------------------------+
|             | Suyu et al., 2010, ApJ, 711, 201                                           |
+-------------+----------------------------------------------------------------------------+
|             | Suyu et al., 2014, ApJ, 788, L35                                           |
+-------------+----------------------------------------------------------------------------+
|             | Wong et al., 2017, MNRAS, 465, 4895                                        |
+-------------+----------------------------------------------------------------------------+
|             | Birrer et al., 2019, MNRAS, 484, 4726                                      |
+-------------+----------------------------------------------------------------------------+
|             | Chen et al., 2019, MNRAS, 490, 1743                                        |
+-------------+----------------------------------------------------------------------------+
|             | Jee et al., 2019, Science, 365, 1134                                       |
+-------------+----------------------------------------------------------------------------+
|             | Rusu et al., 2020, MNRAS, 498, 1440                                        |
+-------------+----------------------------------------------------------------------------+
|             | Wong et al., 2020, MNRAS, 498, 1420                                        |
+-------------+----------------------------------------------------------------------------+
|             | Sahjib et al., 2020, MNRAS, 494, 6072                                      |
+-------------+----------------------------------------------------------------------------+

This module contain the likelihood of a 7 time-delay lenses, presented in TDCOSMO IV (Birrer et al., 2020).
This module allows us to reproduce the hierarchical inference of the cosmological parameters and of the lens population parameters,
which are grouped under the block `nuisance_strong_lensing` (see details below). 

Additional data sets such as 'SLACS_SDSS' and 'SLACS_IFU' can be added to the 'tdcosmo7' data set to help constrain these parameters.
Adding these 2 data sets requires to make the additional assumption that the lensing galaxy of the 7 TDCOSMO lenses and of the SLACS lenses 
come from the same population of galaxies.


Assumptions
-----------

 - Strong lensing modelling details.
 - Time delay distance structure
 - Hierarchical inference of the mass model and stellar anisotropy parameters



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_sets
     - str
     - tdcosmo7
     - Data sets to use. Choose any combination of 'tdcosmo7', 'SLACS_SDSS' and 'SLACS_IFU'. You can use 'tdcosmo7+SLACS_SDSS' or 'tdcosmo7+SLACS_SDSS+SLACS_IFU' for example.
   * - num_distribution_draws
     - int
     - 200
     - Number of random realisation for kinematic computations.
   * - distances_computation_module
     - str
     - astropy
     - Module used distance-redshift relation. 'astropy' uses standard astropy cosmology w0waCDM. 'CosmoInterp' to use the CosmoInterp module of lenstronomy to interpolate. 'camb' will use the distances provided by camb to compute Ds, Dd, and Dds.


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - cosmological_parameters
     - omega_l
     - real
     - 
     - Dark energy density fraction today
   * - 
     - h0
     - real
     - 
     - Hubble parameter H0 (km/s/Mpc)
   * - 
     - omega_m
     - real
     - 
     - Dark matter density fraction today
   * - nuisance_strong_lensing
     - lambda_mst
     - real
     - 1.0
     - Internal Mass sheet degeneracy parameter
   * - 
     - lambda_mst_sigma
     - real
     - 0.04
     - 1-sigma Gaussian scatter in lambda_mst
   * - 
     - alpha_lambda
     - real
     - 0.0
     - Slope of lambda_mst with r_eff/theta_E
   * - 
     - a_ani
     - real
     - 1.5
     - mean a_ani anisotropy parameter in the Osipkov-Merritt model
   * - 
     - a_ani_sigma
     - real
     - 0.3
     - 1-sigma Gaussian scatter in a_ani


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - TDCOSMO_like
     - real
     - Total likelihood of the TDCOSMO sample


