kappa_ell_cut
================================================

Apply minimum and maximum ell to cross-power spectra with CMB kappa.

.. list-table::
    
   * - File
     - cmb_lensing/kappa_ell_cut/kappa_beam.py
   * - Attribution
     -
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - You can do what you want with this file.


"It is often useful to apply a maximum or minimum ell cut to a CMB lensing map before measuring correlation functions with galaxies and shears.  If such an ell-cut is applied, we must account for it on the modeling side.  This module applies the lmin/lmax cut to the relevant cross-power spectra."



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
   * - lmin
     - 0
     - 
     - Minimum ell to impose for CMB kappa cross-spectra.
   * - lmax
     - int
     - 999999
     - Maximum ell to impose for CMB kappa cross-spectra.


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
     - Shear-kappa C_ell, set to zero outside cuts
   * - galaxy_cmbkappa_cl
     - ell
     - int 1d
     - Values at which c_ell is evaluated
   * - 
     - bin_{i}_{j}
     - real 1d
     - Galaxy-kappa C_ell, set to zero outside cuts


