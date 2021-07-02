wmap_shift
================================================

Massively simplified WMAP9 likelihood reduced to just shift parameter

.. list-table::
    
   * - File
     - likelihood/wmap_shift/wmap_shift.so
   * - Attribution
     - The WMAP Collaboration (measurement)
   * -
     - CosmoSIS team (code)
   * - URL
     - 
   * - Citation
     - Hinshaw et al, ApJS, 208, 2, 19, 25
   * - Rules
     -


The full WMAP likelihood is slow and requires a full Boltzmann
integration (also slow) to get the CMB spectra.

This module uses a lightweight alternative - the CMB shift parameter,
which can be calculated from background evolution alone.

This does not provide as much information as the full likelihood.



Assumptions
-----------

 - CMB shift parameter as in LCDM
 - WMAP9 measurement of parameter



Setup Parameters
----------------

None


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
     - cmbshift
     - real
     - 
     - CMB Shift parameter


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - shift_like
     - real
     - Combined log-likelihood from all WMAP components


