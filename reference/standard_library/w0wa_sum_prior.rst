w0wa_sum_prior
================================================

Skip parameter sample without failing if w0+wa>0.

.. list-table::
    
   * - File
     - utility/exclude_w0_wa/w0wa_sum_prior.py
   * - Attribution
     - Jessie Muir
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - Please maintain attribution.


This module imposes a the requirement that  w_0+w_a<0, which
ensures that w(a)= w_0 + (1-a)w_a  is always negative. 

This is useful because it allows us to avoid computational problems that
 CAMB (and possibly other boltzman codes) has when the dark energy 
 equation of state becomes positive.

This module checks whether w_0+w_a<0. If that condition is  
fulfilled, the module does nothing. If w_0+w_a>=0, the module returns 1, 
which will cause cosmosis samplers to throw out the point and skip the 
rest of the pipeline for that sample.


Assumptions
-----------

 - Cosmological parameters include w and wa.



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - verbose
     - bool
     - False
     - Whether to print an error message noting when points fail the w_0+w_a<0 requirement


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
     - Dark energy equation of state at z=0 (w_0)
   * - 
     - wa
     - real
     - 
     - Linear coefficient of dark energy equation of state on scale factor


Output values
----------------


None


