mgs
================================================

Compute the likelihood of MGS BAO and FS as distributed by eBOSS DR16

.. list-table::
    
   * - File
     - likelihood/eboss_dr16/mgs/mgs.py
   * - Attribution
     - MGS team, eBOSS DR16 team
   * - URL
     - https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_0/likelihoods/
   * - Citation
     - C. Howlett et al, MNRAS 2015
   * - Rules
     -


This module computes the likelihood of MGS, using f*sigma8 and  D_v/r_s measurements. 


Assumptions
-----------

 - Gaussian likelihood



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
     - sdss_MGS_FSBAO_DVfs8.txt
     - Path to file with measured D_v(zeff),fsig8(zeff) values
   * - cov_file
     - str
     - sdss_MGS_FSBAO_DVfs8_covtot.txt
     - Path to covariance matrix file
   * - rs_fiducial
     - real
     - 147.8
     - Fiducial value of sound horizon at last scattering used in making data
   * - verbose
     - bool
     - False
     - Whether to print extra output


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - growth_parameters
     - d_z
     - real 1d
     - 
     - Linear growth factor D(z)
   * - 
     - f_z
     - real 1d
     - 
     - Linear growth rate f(z)
   * - 
     - z
     - real 1d
     - 
     - Redshift of samples
   * - cosmological_parameters
     - omega_m
     - real
     - 
     - Matter density fraction of critical
   * - 
     - sigma_8
     - real
     - 
     - Amplitude of linear matter power at 8/h Mpc at z=0
   * - 
     - h0
     - real
     - 
     - Hubble parameter H0 / (100 km/s/Mpc)
   * - distances
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - d_a
     - real 1d
     - 
     - Angular diameter distance in Mpc
   * - 
     - h
     - real 1d
     - 
     - Hubble parameter with in units of Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - mgs_like
     - real
     - Likelihood of Dv and fsigma8 at z=0.15


