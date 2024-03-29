6dFGS
================================================

Compute the likelihood of supplied D_v or fsigma8(z=0.067)

+-------------+--------------------------------------+
| File        | likelihood/6dfgs/6dfgs_rsd.py        |
+-------------+--------------------------------------+
| Attribution | 6dFGS Team                           |
+-------------+--------------------------------------+
| URL         |                                      |
+-------------+--------------------------------------+
| Citations   | BAO MNRAS 416, 3017 3032 (2011)      |
+-------------+--------------------------------------+
|             | fsigma8 MMNRAS 423, 3430 3444 (2012) |
+-------------+--------------------------------------+




Assumptions
-----------

 - 6dFGS dataset



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
   * - bao_like
     - bool
     - True
     - Whether to use BAO likelihood
   * - rsd_like
     - bool
     - False
     - Whether to use RSD likelihood
   * - bao_mode
     - str
     - rs_dv
     - Set to "dv" to use the measurement of D_v or to "rs_dv" to use the ratio r_s/D_v
   * - mean
     - real
     - 457.0 or 0.423
     - Dv for mode 0 or fsigma8 for mode 1
   * - sigma
     - real
     - 27.0 or 0.055
     - Sigma_Dv for mode 0 or sigma_fsigma8
   * - redshift
     - real
     - 0.106 or 0.067
     - Redshift of measurements, depending on mode


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
     - bias
     - real
     - 
     - Galaxy bias
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
     - d_m
     - real 1d
     - 
     - Physical angular diameter distance in Mpc
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
     - 6dfgs_LIKE
     - real
     - Likelihood of supplied Dv(z=0.106) or fsigma8(z=0.067)


