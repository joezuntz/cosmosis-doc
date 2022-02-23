boss_dr12_lrg_reanalyze
================================================

Compute the likelihood of the supplied expansion and growth history against BOSS DR12 data as reanalyzed by eBOSS DR16

.. list-table::
    
   * - File
     - likelihood/eboss_dr16/boss_dr12/boss_dr12_lrg_reanalyze.py
   * - Attribution
     -
   * - URL
     - https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_0/likelihoods/
   * - Citation
     - 
   * - Rules
     -


This module is adapted from boss_dr12.py module in boss_dr12, to read the boss dr12 likelihood data as released by eBOSS DR 16.  The data files are from the BAO-only and BAO-plus (which the recomended one) directories. One notable difference is that the txt files only  contain boss dr12 measurements for the two lowest redshift bins.
This module gives a likelihood of the comoving angular diameter distance D_m, the Hubble parameter H(z) and f*sigma_8. It uses the sound horizon at last-scatter rs_zdrag.
A correlated Gaussian likelihood is then returned.


Assumptions
-----------

 - 
 - 



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - mode
     - int
     - 0
     - 0 for BAO only, 1 for BAO+FS measurements
   * - data_file
     - str
     - sdss_DR12_LRG_BAO_DMDH.txt or sdss_DR12_LRG_FSBAO_DMDHfs8.txt
     - path to file with measured data values in
   * - cov_file
     - str
     - sdss_DR12_LRG_BAO_DMDH_covtot.txt or sdss_DR12_LRG_FSBAO_DMDHfs8_covtot.txt
     - path to covariance matrix file
   * - rs_fiducial
     - real
     - 147.78
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
     - Baryon + cdm density fraction today
   * - 
     - sigma_8
     - real
     - 
     - Amplitude of linear matter power at 8/h Mpc at z=0
   * - 
     - h0
     - real
     - 
     - Hubble parameter H0/(100 km/s/Mpc)
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
     - boss12_lrg_like
     - real
     - Likelihood of supplied expansion history


