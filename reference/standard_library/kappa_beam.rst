kappa_beam
================================================

Apply smoothing function to cross-correlations with CMB kappa in harmonic space.

.. list-table::
    
   * - File
     - cmb_lensing/kappa_beam/kappa_beam.py
   * - Attribution
     -
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - You can do what you want with this file.


"It is often useful to convolve an estimated CMB lensing map with a Gaussian beam before measuring correlation functions with galaxies and shears.  If such smoothing is applied, we must account for it on the modeling side.  This module accounts for such smoothing by multiplying the theoretical power spectra by the necessary beam factors."



Assumptions
-----------

 - 



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - shearkappa_section
     - str
     - 
     - Section name where harmonic-space cross-spectrum between galaxy shear and CMB kappa is stored.  Leave blank if none.
   * - galkappa_section
     - str
     - 
     - Section name where harmonic-space cross-spectrum between galaxy density and CMB kappa is stored.  Leave blank if none.
   * - beam_sigma_arcmin
     - real
     - 
     - Sigma of Gaussian for smoothing CMB kappa (in arcminutes)
   * - beam_fwhm_arcmin
     - real
     - 
     - FWHM of Gaussian for smoothing CMB kappa (in arcminutes)


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - shear_cmbkappa_cl
     - ell
     - int 1d
     - 
     - Angular frequency values at which Shear-kappa c_ell is evaluated
   * - 
     - bin_{i}_{j}
     - real 1d
     - 
     - Shear-kappa C_ell calculated at corresponding ell for relevant i and j combinations
   * - galaxy_cmbkappa_cl
     - ell
     - int 1d
     - 
     - Angular frequency values at which Galaxy-kappa c_ell is evaluated
   * - 
     - bin_{i}_{j}
     - real 1d
     - 
     - Galaxy-kappa C_ell calculated at corresponding ell for relevant i and j combinations


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - shear_cmbkappa_cl
     - ell
     - int 1d
     - Angular frequency values at which Shear-kappa c_ell is evaluated
   * - 
     - bin_{i}_{j}
     - real 1d
     - Shear-kappa C_ell smoothed by beam
   * - galaxy_cmbkappa_cl
     - ell
     - int 1d
     - Values at which c_ell is evaluated
   * - 
     - bin_{i}_{j}
     - real 1d
     - Galaxy-kappa C_ell smoothed by beam


