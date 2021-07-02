load_nz
================================================

Load a number density n(z) for weak lensing from a file

.. list-table::
    
   * - File
     - number_density/load_nz/load_nz.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - If you use a file from a particular survey you should cite that survey


"This simple module just loads a set of n(z) for different bins from a
fixed file and provides it as-is.  The n(z) are normalized before being saved."



Assumptions
-----------

 - n(z) file first column = z, others = bin n(z)



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - filepath
     - str
     - 
     - Absolute or relative path to an n(z) file
   * - des_fmt
     - bool
     - False
     - Use the DES format n(z) with columns zmin, zmax, nz1, nz2...
   * - histogram
     - bool
     - False
     - Assume that the given z values are lower edges of histogram bins, not sample points.
   * - output_section
     - str
     - wl_number_density
     - The section to which to save the output.


Input values
----------------

No inputs


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
     - Number of redshift samples.
   * - 
     - nbin
     - int
     - Number of bins
   * - 
     - z
     - real 1d
     - ; redshift sample values
   * - 
     - bin_{i}
     - real 1d
     - ; n(z) at redshift sample values.  bin_1, bin_2, ...


