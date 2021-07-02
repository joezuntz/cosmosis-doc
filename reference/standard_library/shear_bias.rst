shear_bias
================================================

Modify a set of calculated shear C_ell with a multiplicative bias

.. list-table::
    
   * - File
     - shear/shear_bias/shear_bias.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


Errors in cosmic shear measurement can lead to a multiplicative factor
scaling the observed shear spectra.

This module scales the measured C_ell to account for that difference,
assuming model values of the multiplicative factor m, either per bin or for all bins.

Since the bias can be different in different bins we have, for the general case
including cross-spectra:

C^{ij}_ell -> (1+m_i)(1+m_j) C^{ij}_ell


Assumptions
-----------

 - Simple multiplicative shear bias model: C^{ij}_ell -> (1+m_i)(1+m_j) C^{ij}_ell



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - m_per_bin
     - bool
     - True
     - If T use a separate m for each bin, otherwise a single global one


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - wl_number_density
     - nbin
     - int
     - 
     - Number of tomographic bins.
   * - shear_calibration_parameters
     - m0
     - real
     - 
     - Only if m_per_bin=F. The multiplicative bias for all the bins.
   * - 
     - m_{i}
     - int
     - 
     - Only if m_per_bin=F; for i=1..nbin. The multiplicative bias for each bin.
   * - shear_cl
     - bin_{i}_{j}
     - real 1d
     - 
     - Shear power spectrum for i and j=1..nbin.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - shear_cl
     - bin_{i}_{j}
     - real 1d
     - Modified shear power spectrum for i and j=1..nbin.


