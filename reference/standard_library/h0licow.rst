h0licow
================================================



+-------------+-------------------------------------------------------------------------------+
| File        | strong_lensing/h0licow/time_delay_interface.py                                |
+-------------+-------------------------------------------------------------------------------+
| Attribution | Original code by Stefan Taubenberger and Sherry Suyu, see final citation link |
+-------------+-------------------------------------------------------------------------------+
|             | Adapted from MontePython version by CosmoSIS team                             |
+-------------+-------------------------------------------------------------------------------+
| URL         |                                                                               |
+-------------+-------------------------------------------------------------------------------+
| Citations   | Suyu et al., 2010, ApJ, 711, 201                                              |
+-------------+-------------------------------------------------------------------------------+
|             | Suyu et al., 2014, ApJ, 788, L35                                              |
+-------------+-------------------------------------------------------------------------------+
|             | Wong et al., 2017, MNRAS, 465, 4895                                           |
+-------------+-------------------------------------------------------------------------------+
|             | Birrer et al., 2019, MNRAS, 484, 4726                                         |
+-------------+-------------------------------------------------------------------------------+
|             | Chen et al., 2019, MNRAS, 490, 1743                                           |
+-------------+-------------------------------------------------------------------------------+
|             | Jee et al., 2019, Science, 365, 1134                                          |
+-------------+-------------------------------------------------------------------------------+
|             | Rusu et al., 2019, arXiv:1905.09338                                           |
+-------------+-------------------------------------------------------------------------------+
|             | Wong et al., 2019, arXiv:1907.04869                                           |
+-------------+-------------------------------------------------------------------------------+
|             | https://zenodo.org/record/3632967#.YDOUEC2cY4d                                |
+-------------+-------------------------------------------------------------------------------+


The likelihood of a suite of time delay system from strong lenses,
as collected in Wong et al., 2019, arXiv:1907.04869

Various different pieces of the likelihood can be switched on and off
using the data\_ parameters.  The default configuration matches that
in the released MontePython code.



Assumptions
-----------

 - Strong lensing modelling details.
 - Time delay distance structure



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_dt_b1608
     - int
     - 0
     - Whether to include the dt_b1608 measurement in the likelihood (0=no, 1=yes)
   * - data_dd_dt_b1608
     - int
     - 1
     - Whether to include the dd_dt_b1608 measurement in the likelihood (0=no, 1=yes)
   * - data_dt_j1206
     - int
     - 0
     - Whether to include the dt_j1206 measurement in the likelihood (0=no, 1=yes)
   * - data_dd_dt_j1206
     - int
     - 1
     - Whether to include the dd_dt_j1206 measurement in the likelihood (0=no, 1=yes)
   * - data_dt_wfi2033
     - int
     - 1
     - Whether to include the dt_wfi2033 measurement in the likelihood (0=no, 1=yes)
   * - data_dt_he0435
     - int
     - 1
     - Whether to include the dt_he0435 measurement in the likelihood (0=no, 1=yes)
   * - data_dt_pg1115
     - int
     - 0
     - Whether to include the dt_pg1115 measurement in the likelihood (0=no, 1=yes)
   * - data_dd_dt_pg1115
     - int
     - 1
     - Whether to include the dd_dt_pg1115 measurement in the likelihood (0=no, 1=yes)
   * - data_dt_rxj1131
     - int
     - 0
     - Whether to include the dt_rxj1131 measurement in the likelihood (0=no, 1=yes)
   * - data_dd_dt_rxj1131
     - int
     - 1
     - Whether to include the dd_dt_rxj1131 measurement in the likelihood (0=no, 1=yes)
   * - data_dir
     - str
     - module_dir/timedelay_6lenses
     - Location of data files


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
     - d_a
     - real 1d
     - 
     - Angular diameter distance in Mpc
   * - cosmological_parameters
     - omega_k
     - real
     - 0.0
     - Curvature density fraction today
   * - 
     - hubble
     - real
     - 
     - Hubble parameter H0 (km/s/Mpc)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - h0licow_like
     - real
     - Total likelihood of system


