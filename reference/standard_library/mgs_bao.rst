mgs_bao
================================================

Compute the likelihood against SDSS MGS data

.. list-table::
    
   * - File
     - likelihood/mgs_bao/mgs_bao.py
   * - Attribution
     - MGS team
   * - URL
     - 
   * - Citation
     - A. Ross et al, MNRAS 449 (2015)
   * - Rules
     -


"This module gives a likelihood of the redshift-distance and redshift-Hubble
relations in combined form D_v = (da**2 * (1+z)**2 * dr)**(1./3.) 
where dr = z / H. It uses the sound horizon at last-scatter rs_zdrag and 
the predicted expansion since last scattering to predict the BAO size
at the redshifts at which SDSS MGS measured them."



Assumptions
-----------

 - MGS chi2
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
     - MGS_BAO_LIKE
     - real
     - Likelihood of supplied expansion history


