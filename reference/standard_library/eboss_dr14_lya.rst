eboss_dr14_lya
================================================

Compute the likelihood of eBOSS DR14 D_m and D_h from Lyman alpha

+-----------+----------------------------------------+
| File      | likelihood/eboss/lya/eboss_dr14_lya.py |
+-----------+----------------------------------------+
| URL       |                                        |
+-----------+----------------------------------------+
| Citations | de Sainte Agathe et al A&A 629 (2019)  |
+-----------+----------------------------------------+
|           | Blomqvist et al A&A 629 (2019)         |
+-----------+----------------------------------------+

This module computes the likelihood of D_m and D_h using eBOSS DR14 measurement from Lyman alpha. At the moment, we are only using the combined measurements from auto and cross correlations. We use the chi2 table given at https://github.com/igmhub/picca/tree/master/data/deSainteAgatheetal2019/combined_stdFit.  The first column is alpha_parallel and the second alpha_perpendicular (sometimes called alpha_transverse) The relation between alphas and D_m and D_h is: alpha_perp = (Dm/rd)/(Dm_fid/rd_fid) alpha_par  = (Dh/rd)/(Dh_fid/rd_fid)
We use the fiducial values from de Sainte Agathe et al as done in this paper.  We then relate the chi2 to the likelihood: log(like) = -chi2/2 


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
     - eboss14_lya_like
     - real
     - likelihood of Dh and Dm at z=2.34


