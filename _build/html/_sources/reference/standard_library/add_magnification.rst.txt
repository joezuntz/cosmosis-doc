add_magnification
================================================

Add magnification terms to C_ell

+-------------+----------------------------------------------+
| File        | structure/magnification/add_magnification.py |
+-------------+----------------------------------------------+
| Attribution | Niall MacCrann                               |
+-------------+----------------------------------------------+
|             | Jack Elvin-Poole                             |
+-------------+----------------------------------------------+
| URL         |                                              |
+-------------+----------------------------------------------+

Magnification affects both the galaxy density and galaxy galaxy-lensing spectra,
adding extra terms to each.  The module finds and adds those terms.

For density (g), we have gg -> gg + gm + mg + mm
For density shear (gG) we have gG -> gG + mG
where m is magnification.

We can also include intrinsic aligment (I) - magnification interactions, in which
case the module does: gG + gI -> gG + gI + mG + mI


Assumptions
-----------

None



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - galaxy-galaxy
     - bool
     - True
     - Whether to add magnification terms to galaxy density spectra
   * - galaxy-shear
     - bool
     - True
     - Whether to add magnification terms to galaxy density-lensing cross-spectra
   * - include_intrinsic
     - bool
     - False
     - Whether to add include intrinsic alignment magnification terms


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - galaxy_cl
     - nbin
     - int
     - 
     - Number of bins in this spectrum
   * - 
     - ell
     - int 1d
     - 
     - Angular wavenumber values for the spectra
   * - 
     - auto_only
     - bool
     - False
     - Whether this bin only contains auto spectra
   * - 
     - bin_i_j
     - real 1d
     - 
     - C_ell values for the galaxy density spectra in bin pair i, j
   * - galaxy_shear_cl
     - nbin_a
     - int
     - 
     - Number of galaxy density bins in this spectrum
   * - 
     - nbin_b
     - int
     - 
     - Number of shear bins in this spectrum
   * - 
     - ell
     - int 1d
     - 
     - Angular wavenumber values for the spectra
   * - 
     - bin_i_j
     - real 1d
     - 
     - C_ell values for the density-shear cross-spectra in bin pair i, j
   * - galaxy_magnification_cl
     - ell
     - int 1d
     - 
     - Angular wavenumber values for the spectra. Can be different to the density/shear ones
   * - 
     - bin_i_j
     - real 1d
     - 
     - C_ell values for the density-magnification cross-spectra in bin pair i, j
   * - magnification_cl
     - ell
     - int 1d
     - 
     - Angular wavenumber values for the spectra. Can be different to the density/shear ones
   * - 
     - bin_i_j
     - real 1d
     - 
     - C_ell values for the density-magnification cross-spectra in bin pair i, j


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - galaxy_cl_gg
     - ell
     - int 1d
     - Angular wavenumber values for the spectra.
   * - 
     - bin_i_j
     - real 1d
     - Copy of the density-shear cross-spectrum without any modifications made
   * - galaxy_cl
     - bin_i_j
     - real 1d
     - Updated C_ell density values including magnification terms
   * - galaxy_shear_cl
     - bin_i_j
     - real 1d
     - Updated C_ell cross-spectra values including magnification terms


