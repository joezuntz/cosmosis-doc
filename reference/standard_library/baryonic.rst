baryonic
================================================

Apply baryonic effects to nonlinear pk based on hydrodynamic simulation measurements

+-------------+------------------------------------------------------+
| File        | structure/baryon_power_scaling/baryonic_interface.py |
+-------------+------------------------------------------------------+
| Attribution | CosmoSIS Team                                        |
+-------------+------------------------------------------------------+
|             | Angela Chen                                          |
+-------------+------------------------------------------------------+
| URL         |                                                      |
+-------------+------------------------------------------------------+

This module reads in Pk_nonlinear from previous modules modifies it, applying
the ratio between DM-only and hydro simulations


Assumptions
-----------

 - Pk_baryonic/Pk_nonlinear = Pk_hydro/Pk_DMonly



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - ratiotable
     - str
     - 
     - Path to one of the ratio files supplied with in the module's data directory


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - matter_power_nl
     - k_h
     - real 1d
     - 
     - sample values of nonlinear spectrum in Mpc/h
   * - 
     - z
     - real 1d
     - 
     - redshift of nonlinear spectrum samples
   * - 
     - p_k
     - real 2d
     - 
     - Nonlinear spectrum in (Mpc/h)^{-3}


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - matter_power_nl
     - p_k
     - real 2d
     - Nonlinear spectrum in (Mpc/h)^{-3}, modified in-place


