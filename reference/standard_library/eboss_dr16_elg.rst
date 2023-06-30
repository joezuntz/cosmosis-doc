eboss_dr16_elg
================================================

Compute the likelihood of eBOSS DR16 from ELG

+-----------+---------------------------------------------------------------------------+
| File      | likelihood/eboss_dr16/elg/eboss_dr16_elg.py                               |
+-----------+---------------------------------------------------------------------------+
| URL       | https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_0/likelihoods/ |
+-----------+---------------------------------------------------------------------------+
| Citations | A. de Mattia et al, 2007.09008                                            |
+-----------+---------------------------------------------------------------------------+

This module computes the likelihood of Dv_over_rd for BAO-only analysis and Dm_over_rd, Dh_over_rd, and fsigma8 for BAO+FS analysis, both using eBOSS DR16 measurements from ELG.


Assumptions
-----------

 - Non-Gaussian likelihood



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
     - Whether to print extra output
   * - mode
     - bool
     - False
     - Whether to include full-shape information instead of just BAO


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
     - Comoving distance in Mpc
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


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - eboss16_elg_like
     - real
     - ELG BAO likelihood


