eboss_dr16_lrg
================================================

Compute the likelihood of eBOSS DR16 from LRG

+-----------+---------------------------------------------+
| File      | likelihood/eboss_dr16/lrg/eboss_dr16_lrg.py |
+-----------+---------------------------------------------+
| URL       |                                             |
+-----------+---------------------------------------------+
| Citations | J. Bautista et al, MNRAS 2020               |
+-----------+---------------------------------------------+
|           | H. Gil-Marin et al, MNRAS 2020              |
+-----------+---------------------------------------------+

This module computes the likelihood of Dm_over_rd and Dh_over_rd for BAO-only analysis and Dm_over_rd, Dh_over_rd, and fsigma8 for BAO+FS analysis, both using eBOSS DR16 measurements from LRG.  We assume likelihoods are Gaussian.


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

   * - feedback
     - bool
     - False
     - Whether to print feedback
   * - mode
     - int
     - 0
     - type of analysis. 0 for BAO-only. 1 for BAO + Full-shape


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
     - fsigma8
     - real 1d
     - 
     - Structure amplitude
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
     - eboss16_lrg_like
     - real
     - likelihood of BAO


