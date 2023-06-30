extract_growth
================================================

returns growth factor and growth rate by examining small-scale P(k)

+-------------+--------------------------------------------+
| File        | structure/extract_growth/extract_growth.py |
+-------------+--------------------------------------------+
| Attribution | CosmoSIS Team                              |
+-------------+--------------------------------------------+
| URL         |                                            |
+-------------+--------------------------------------------+

This simple module extracts the the linear growth factor D, and linear growth rate, from the matter power spectra
It takes the z spacing from the input module



Assumptions
-----------

 - Nonlinear or linear P(k,z) calculated at a small k value.



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - input_section
     - str
     - matter_power_lin
     - Which input section (spectrum) to use
   * - output_section
     - str
     - growth_parameters
     - Which output section to put the results in


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
     - Wavenumbers of samples
   * - 
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - p_k
     - real 2d
     - 
     - Matter power spectrum samples


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - growth_parameters
     - d_z
     - real 1d
     - Linear growth factor D(z)
   * - 
     - f_z
     - real 1d
     - Linear growth rate f(z)
   * - 
     - z
     - real 1d
     - Redshift of samples


