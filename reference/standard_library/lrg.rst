lrg
================================================

Compute the likelihood of eBOSS DR14 D_v from LRG

.. list-table::
    
   * - File
     - likelihood/eboss/lrg/eboss_dr14_lrg.py
   * - Attribution
     -
   * - URL
     - 
   * - Citation
     -  Bautista et al ApJ 863 110 (2018)
   * - Rules
     -


This module computed the likelihood of D_v using eBOSS DR14 measurement from LRG.  We assume the likelihood on D_v is Gaussian.


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
     - int
     - 0
     - Amount of output to print.  0 for no feedback.  1 for basic


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
     - eboss14_lrg_like
     - real
     - likelihood of  Dv at z=0.72


