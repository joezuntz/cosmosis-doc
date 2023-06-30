eboss_dr16_qso
================================================

Compute the likelihood of eBOSS DR16 from QSO

+-----------+---------------------------------------------+
| File      | likelihood/eboss_dr16/qso/eboss_dr16_qso.py |
+-----------+---------------------------------------------+
| URL       |                                             |
+-----------+---------------------------------------------+
| Citations | Neveux et al, MNRAS 2020                    |
+-----------+---------------------------------------------+
|           | Hou et al, MNRAS 2020                       |
+-----------+---------------------------------------------+

This module computes the likelihood of Dm_over_rd and Dh_over_rd for BAO-only analysis and Dm_over_rd, Dh_over_rd, and fsigma8 for BAO+FS analysis, both using eBOSS DR16 measurements from QSO.  We assume likelihoods are Gaussian.


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

   * - mode
     - int
     - 0
     - 0 for BAO-only. 1 for BAO + Full-shape


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
   * - growth_parameters
     - fsigma8
     - real 1d
     - 
     - Structure amplitude f(z) * sigma8(z())
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
     - eboss16_qso_like
     - real
     - QSO BAO likelihood


