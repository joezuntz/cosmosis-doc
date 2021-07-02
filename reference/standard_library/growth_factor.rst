growth_factor
================================================

returns linear growth factor and growth rate for flat cosmology with either const w or variable DE eos w(a) = w + (1-a)*wa

.. list-table::
    
   * - File
     - structure/growth_factor/interface.so
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - If you use a file from a particular survey you should cite that survey


This simple module calculates the linear growth factor D, and linear growth rate, f, for flat cosmology with either const w or variable DE eos w(a) = w + (1-a)*wa. 
Where D, f are defined by the growth of a
linear perturbation, delta, with scale factor a: delta(a') = delta(a)*(D(a')/D(a)) and f = dlnD/dlna


Assumptions
-----------

 - linear growth factor and rate in flat cosmology



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - zmin
     - real
     - 0.0
     - Min value to save f,D
   * - zmax
     - real
     - 3.0
     - Max value to save f,D
   * - dz
     - real
     - 0.01
     - Redshift binsize
   * - zmax_log
     - real
     - 1100.0
     - Redshift max for additional z values tacked above zmax, log space
   * - nz_log
     - int
     - 0.0
     - Number of log spaced values (if 0 then no log-spaced values)


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - cosmological_parameters
     - omega_m
     - real
     - 
     - Baryon + cdm density fraction today
   * - 
     - omega_lambda
     - real
     - 1-omega_m
     - Dark energy density today
   * - 
     - w
     - real
     - -1.0
     - Equation of state of dark energy w(z=0)
   * - 
     - wa
     - real
     - 0.0
     - Equation of state parameter in w(z) = w_0 + w_a z / (1+z)


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


