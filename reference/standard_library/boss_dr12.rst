boss_dr12
================================================

Compute the likelihood of the supplied expansion and growth history against BOSS DR12 data

.. list-table::
    
   * - File
     - likelihood/boss_dr12/boss_dr12.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - https://www.sdss3.org/science/boss_publications.php
   * - Citation
     - arxiv: 1607.03155
   * - Rules
     - You can do what you want with the python code here


"This module gives a likelihood of the comoving angular diameter distance D_m, the Hubble parameter H(z) and f*sigma_8. It uses the sound horizon at last-scatter rs_zdrag.
A correlated Gaussian likelihood is then returned."



Assumptions
-----------

 - LCDM Model
 - Details of BOSS reconstruction



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
     - Included file
     - Path to file with measured D_m(z1), H(z1), fsig8(z1), D_m(z2), etc values
   * - cov_file
     - str
     - Included file
     - Path to covariance matrix file
   * - redshift_file
     - str
     - Included file
     - Path to file with the effective redshifts of the measurements
   * - rs_fiducial
     - real
     - 147.78
     - Fiducial value of sound horizon at last scattering used in making data
   * - feedback
     - int
     - 0
     - Feedback level - 0 for no feedback, 1 for lots


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
     - boss_dr12_like
     - real
     - Likelihood of supplied expansion history


