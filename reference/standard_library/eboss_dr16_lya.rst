eboss_dr16_lya
================================================

Compute the likelihood of eBOSS DR16 from Lyman alpha

+-----------+---------------------------------------------------------------------------+
| File      | likelihood/eboss_dr16/lya/eboss_dr16_lya.py                               |
+-----------+---------------------------------------------------------------------------+
| URL       | https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_0/likelihoods/ |
+-----------+---------------------------------------------------------------------------+
| Citations | du Mas des Bourboux, the Astrophysical Journal, 2020                      |
+-----------+---------------------------------------------------------------------------+

This module computes the likelihood of Dm and Dh using eBOSS DR16 measurement from Lyman alpha, auto and cross correlations.  These have only geometric information (no RSD). 
This module computes the combined likelihoods of cross and auto. 


Assumptions
-----------

None



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - feedback
     - bool
     - False
     - Whether to print feedback


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
     - rs_zdrag
     - real
     - 
     - Value of predicted drag redshift


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - eboss16_lya_like
     - real
     - likelihood of Dh and Dm at z=2.334


