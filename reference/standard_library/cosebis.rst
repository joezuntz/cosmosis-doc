cosebis
================================================

Calculate COSEBIs from C_ell power spectra

+-------------+----------------------------------------------+
| File        | shear/cosebis/cl_to_cosebis/cl_to_cosebis.so |
+-------------+----------------------------------------------+
| Attribution | Marika Asgari                                |
+-------------+----------------------------------------------+
|             | Patrick Simon                                |
+-------------+----------------------------------------------+
| URL         |                                              |
+-------------+----------------------------------------------+
| Citations   | https://arxiv.org/abs/1201.2669              |
+-------------+----------------------------------------------+
|             | https://arxiv.org/abs/1601.00115             |
+-------------+----------------------------------------------+

COSEBIs (Complete Orthogonal Sets of E/B-Integral) are a set of alternative two-point statistics 
designed to separate E/B-modes completely on a finite angular range. They have a reasonably localised
response to Fourier modes, ell, and are also easy to measure from data. This module calculates both E_n and B_n 
log-COSEBIs from https://arxiv.org/abs/1002.2136.

The expectation value of B-modes is zero if there is no B-mode power spectra. 
To calculate B-mode COSEBIs simply switch input_section_name to take B-mode Cls as input 
and output_section_name to avoid mixing E/B-modes.

For this CosmoSIS edition we include the cl_to_cosebis mode for a KiDS-1000 or DES+KiDS
joint analysis.  This is taken from the public COSEBIs library of software https://github.com/maricool/2pt_stats
which includes additional software to convert xi_pm measurements into COSEBIs and calculate covariance matrices.
Note the 'maricool' version also includes additional capability to marginalise over an uncertain c-term which we
do not include here for simplicity.


Assumptions
-----------

 - Flat sky approximation



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - theta_min
     - real
     - 0.5
     - Minimum angular distance between galaxies in arcminutes.
   * - theta_max
     - real
     - 300.0
     - Maximum angular distance between galaxies in arcminutes.
   * - n_max
     - integer
     - 5
     - Maximum COSEBIs mode to be calculated: n=1,2,.., n_max.
   * - input_section_name
     - str
     - shear_cl
     - Section name for input cls.
   * - output_section_name
     - str
     - cosebis
     - Section name for outputs.
   * - Wn_Output_FolderName
     - str
     - COSEBIS_DIR "/WnLog/"
     - Folder name for Wn files.
   * - Wn_file_name
     - str
     - WnLog
     - Wn file name.
   * - table_precision
     - int
     - 10
     - number of digits used in saved WnLog table
   * - number_of_Wn_l_bins
     - int
     - 100000
     - number of log ell bins used in saved WnLog table
   * - Roots_n_Norms_FolderName
     - str
     - COSEBIS_DIR "/TLogsRootsAndNorms"
     - Folder name for Roots and Normalisations.


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - input_section_name
     - ell
     - real 1d
     - 
     - Sample ell values for input C_ell
   * - 
     - nbin_a
     - int
     - 
     - Number of redshift bins in the first quantity.
   * - 
     - nbin_b
     - int
     - 
     - Number of redshift bins in the second quantity. If nbin_a is not equal nbin_b gives an error.
   * - 
     - nbin
     - int
     - 
     - Number of redshift bins used if nbin_a or b not found.
   * - 
     - bin_i_j
     - real 1d
     - 
     - C_ell (no l(l+1) factor) for bin i and j.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - output_section_name
     - n
     - real 1d
     - Array of mode values n for COSEBIs.
   * - 
     - bin_i_j
     - real 1d
     - Array of E_n or B_n, for bin i and j.
   * - 
     - theta_min
     - real
     - Minimum angle in arcmin
   * - 
     - theta_max
     - real
     - Maximum angle in arcmin
   * - 
     - nbin_a
     - int
     - Number of redshift bins in the first quantity.
   * - 
     - nbin_b
     - int
     - Number of redshift bins in the second quantity. Currently nbin_a==nbin_b.


