NLfactor
================================================

Compute nonlinear weyl potential (and other) spectrum by multiplying the linear spectrum with matter_power_nl/matter_power_lin

.. list-table::
    
   * - File
     - structure/nlfactor/NLfactor.py
   * - Attribution
     - Danielle Leonard
   * -
     - Angela Chen
   * - URL
     - None
   * - Citation
     -
   * - Rules
     - It assumes the nonlinearity of the target spectrum is due to the nonlinearity of the matter perturbation. You should also make sure that the linear k_h is not in a narrower range than the nonlinear k_h. Target nonlinear pk will be truncated to the nonlinear matter power k_h range.


This module multiplies the target_section by the nonlinear boost (matter_power_nl/matter_power_lin).


Assumptions
-----------

 - It assumes the nonlinearity of the target spectrum is due to the nonlinearity of the matter perturbation.



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - linear_section
     - str
     - matter_power_nl
     - The name of nonlinear matter power spectrum section
   * - target_section
     - str
     - weyl_curvature_spectrum
     - The name of target matter power spectrum section


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - matter_power_lin
     - k_h
     - real 1d
     - 
     - sample values of linear spectrum in Mpc/h
   * - 
     - z
     - real 1d
     - 
     - redshift of linear spectrum samples
   * - 
     - p_k
     - real 2d
     - 
     - linear spectrum in (Mpc/h)^{-3}
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
   * - target_section
     - k_h
     - real 1d
     - 
     - sample values of target spectrum in Mpc/h
   * - 
     - z
     - real 1d
     - 
     - redshift of target spectrum samples
   * - 
     - p_k
     - real 2d
     - 
     - Target spectrum in (Mpc/h)^{-3}


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - target_section
     - k_h
     - real 1d
     - sample values of target spectrum in Mpc/h
   * - 
     - z
     - real 1d
     - redshift of target spectrum samples
   * - 
     - p_k
     - real 2d
     - Target spectrum in (Mpc/h)^{-3}


