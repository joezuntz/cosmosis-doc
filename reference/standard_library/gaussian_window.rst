gaussian_window
================================================

Compute Gaussian n(z) window functions for weak lensing bins

.. list-table::
    
   * - File
     - number_density/gaussian_window/gaussian_window.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - You can do what you want with this file


This very simple module sets up fixed redshift n(z) bins for weak lensing.
 We should probably upgrade it to take the redshift and sigma from the 
 sampling instead of the ini file.


Assumptions
-----------

 - Gaussian window in redshift



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - z
     - real or real 1d
     - 
     - Redshift(s) of the bins
   * - sigma
     - real or real 1d
     - 
     - Width of the bins in redshift


Input values
----------------

None


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - wl_number_density
     - nz
     - int
     - Number of redshift samples
   * - 
     - nbin
     - int
     - Number of bins
   * - 
     - z
     - real 1d
     - Redshift sample values
   * - 
     - bin_{i}
     - real 1d
     - n(z) at redshift sample values.  bin_1, bin_2, ...


