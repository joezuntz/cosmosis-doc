log_w_model
================================================

Implement Tripathi, Sangwan, Jassal (2017) w(z) model

.. list-table::
    
   * - File
     - background/log_w_model/log_w_model.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     - Tripathi, Sangwan, Jassal (2017)
   * - Rules
     -


This w(z) model is several of the example scripts; it uses
w(z) = w_0 + w_1 log(1 + z)

Nothing else is calculated here.


Assumptions
-----------

 - w(z) = w_0 + w_1 log(1 + z)



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - zmax
     - real
     - 3.0
     - Maximum redshift to tabulate w(z) to
   * - nz
     - int
     - 301
     - Number of redshifts to tabulate w(z) at


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
     - w
     - real
     - 
     - w0 dark energy equation of state parameter today
   * - 
     - w1
     - real
     - 
     - w1 dark energy equation of state change with log(1+z)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - de_equation_of_state
     - a
     - real 1d
     - Scale factor at tabulated points
   * - 
     - z
     - real 1d
     - Redshift at tabulated points
   * - 
     - w
     - real 1d
     - Equation of state at tabulated points


