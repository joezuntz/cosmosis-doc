des-y3-bao
================================================

Compute the likelihood of DES Y3 BAO data

.. list-table::
    
   * - File
     - likelihood/des-y3-bao/bao_y3_like.py
   * - Attribution
     - DES Collaboration
   * - URL
     - 
   * - Citation
     - DES Collaboration, Physical Review D, 2022, Volume 105, Issue 4, article id.043512
   * - Rules
     -


This module gives a likelihood of the combination d_m / r_s from the DES Y3 data.
It interpolates the ratio of that combination to a fiducial value, and then interpolates
into a pre-computed chi2 as a function of that ratio.



Assumptions
-----------

 - BAO chi2
 - FLRW metric and standard BAO size



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - verbose
     - bool
     - False
     - Print extra output
   * - chi2_dir
     - str
     - Module directory
     - Directory to find data file
   * - chi2_file
     - str
     - chi2profile_dvdesy3_cosmoplanck18_covcosmolike.csv
     - Name of CSV data file within chi2_dir
   * - chi2_column
     - int
     - 1
     - Column to read for alpha from the file


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - distances
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - d_m
     - real 1d
     - 
     - Physical angular diameter distance in Mpc
   * - 
     - h
     - real 1d
     - 
     - Hubble parameter with in units of Mpc
   * - 
     - rz_zdrag
     - real
     - 
     - Sound horizon at last scattering in Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - des_y3_bao_like
     - real
     - Likelihood of supplied expansion history


