load_nz_fits
================================================

Load a number density n(z) from a FITS file

.. list-table::
    
   * - File
     - number_density/load_nz_fits/load_nz_fits.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - If you use a file from a particular survey you should cite that survey


This module is designed to work with the number density part of the FITS
files described in:
http://github.com/joezuntz/2point/

High-precision analyses of two-point measurements require knowing *precisely* what
is meant by a given n(z) analysis.  Most of the CosmoSIS standard library modules
downstream of this one assume that the n(z) specifies sample points in a smooth
curve, since that seems most physical.  Most photo-z codes, on the other hand,
provide data in the form of histograms, with small bins in z having a constant
assumed n(z) within them.

The actual difference between these two forms is 
usually well within the systematic errors associated with photometric
redshift estimation, so if you're doing a realistic analysis the difference should
be washed out.  But for code comparison exercises where you are trying to ensure 
0.1% level differences they are very large. 

The parameter 'upsampling' in this module is designed to address this. Higher upsampling
values add new sample points in between the existing ones, so that the two forms
look much closer.

A proper solution to this, where we use splines the parts of the code that actually
use the n(z) that understand the histogram form, is in our roadmap.




Assumptions
-----------

 - Data is provided in FITS extensions NZ_{NAME}
 - There are various subtleties to do with the sampling and form of the n(z) data



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - nz_file
     - str
     - 
     - Absolute or relative path to an n(z) file
   * - data_sets
     - str
     - 
     - Space separated names of the extensions from the FITS files to load and save to the block
   * - prefix_extension
     - bool
     - True
     - Add the prefix NZ_ to the names in data_sets when looking in the FITS file
   * - prefix_section
     - bool
     - True
     - Add the same NZ_ prefix to the section names used in the block.
   * - upsampling
     - int
     - 1.0
     - The number of sample points output for each one in the file. n(z) is assumed flat between them. See notes above.


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


