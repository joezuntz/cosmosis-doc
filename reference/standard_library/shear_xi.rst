shear_xi
================================================

Compute the likelihood of a tomographic shear correlation function data set

.. list-table::
    
   * - File
     - likelihood/shear_xi/xipm_like_interface.py
   * - Attribution
     - Niall Maccrann
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -



DEPRECATED: This module is not recommended for use any more; use the 2pt_like likelihood instead.

Several surveys are measuring the cosmic shear 2-pt correlation functions xi_+(theta) 
and xi_minus(theta) of the gravitational lensing in tomographic redshift bins.

This module calculates the likelihood of theoretical xi(theta) values
values given a data set.  It assumes a simple Gaussian likelihood, so the only
complexities are:
   selecting exactly which data to use - angular ranges, whether to use xi_minus
   if the covariance matrix came from simulations this
     adds noise to the covariance matrix - this the number of sims can be set



Assumptions
-----------

 - Gaussian likelihood of shear xi
 - Redshift distribution used correctly matches tomographic bins



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_file
     - str
     - 
     - File containing the data vector. Each row should be one angle, and then the ordering for e.g. three bins is: xip(0,1) xip(0,2) xip(1,1) xip(1,2) xip(2,2) xim(0,0) xim(0,1) xim(0,2) xim(1,1) xim(1,2) xim(2,2)
   * - covmat_file
     - str
     - 
     - File containing the covariance matrix, either text file or numpy npy file. Ordering goes down the columns of the data vector first.
   * - n_z_bins
     - int
     - 
     - Number of redshift bins to use
   * - cov_num_rlzn
     - int
     - 0
     - Number of realizations to assume for covariance simulations. Zero means no simulation errors.
   * - plus_only
     - bool
     - False
     - Whether to use only xi+ and ignore xi-
   * - theta_mins
     - str
     - 
     - Comma separated minimum angles in arcmin for the different bin pairs
   * - theta_maxs
     - str
     - 
     - Comma separated maximum angles in arcmin for the different bin pairs


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - shear_xi
     - theta
     - real 1d
     - 
     - Theta values of theory correlation functions
   * - 
     - xi_plus_i_j
     - real 1d
     - 
     - Xi_plus meausurements for i,j=(1..n_z_bins)
   * - 
     - xi_minus_i_j
     - real 1d
     - 
     - Xi_minus meausurements for i,j=(1..n_z_bins)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - xipm_like
     - real
     - Likelihood of supplied theory correlation functions


