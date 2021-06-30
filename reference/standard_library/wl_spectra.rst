wl_spectra
================================================

Compute various weak lensing C_ell from P(k,z) with the Limber integral

.. list-table::
    
   * - File
     - shear/spectra/interface.so
   * - Attribution
     - CosmoSIS team
   * -
     - Matt Becker
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


"
DEPRECATED: You should use the module cosmosis-standard-library/structure/projection/project_2d.py instead.

The Limber approximation integrates a 3D power spectrum over the radial
direction to get a 2D angular power spectrum.  It is an approximation
which is only valid on smaller scales.


C_\ell =  A \int_0^{\chi_1} W_1(\chi) W_2(\chi) P(k=l/\chi, z(\chi)) / chi^2 d\chi

The full integral must integrate over k(\ell) also.

For weak lensing, the power spectrum is the matter power spectrum and the two
kernel functions W depend on the redshift bins being used and the geometry.

Parts of this code and the underlying implementation of limber are based on cosmocalc:
https://bitbucket.org/beckermr/cosmocalc-public
"



Assumptions
-----------

 - The Limber integral is valid on the scales in question



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - n_ell
     - int
     - 
     - Number of log-spaced ell values to compute
   * - ell_min
     - real
     - 
     - Minimum ell value to compute
   * - ell_max
     - real
     - 
     - Maximum ell value to compute
   * - shear_shear
     - bool
     - True
     - Compute shear auto-spectra?
   * - intrinsic_alignments
     - bool
     - False
     - Compute intrinsic alignments spectra?
   * - matter_spectra
     - bool
     - False
     - Compute matter power spectra?
   * - ggl_spectra
     - bool
     - False
     - Compute galaxy-galaxy lensing spectra?
   * - gal_IA_cross_spectra
     - bool
     - False
     - Compute cross-power between galaxy positions and alignments?
   * - mag_gal_cross_spectra
     - bool
     - False
     - Compute lensing magnification cross-spectra?
   * - mag_mag
     - bool
     - False
     - Compute lensing magnification auto-spectra?


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
     - omega_m
     - real
     - 
     - Density fraction of all matter; used in the prefactor
   * - 
     - h0
     - real
     - 
     - Hubble factor H0 / 100 km/s/Mpc.
   * - distances
     - z
     - real 1d
     - 
     - Redshift values of distance samples
   * - 
     - d_m
     - real 1d
     - 
     - Comoving distnace to redshift values in units of Mpc (no factor h)
   * - matter_power_nl
     - z
     - real 1d
     - 
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P(k,z) samples in units of Mpc/h
   * - 
     - P_k
     - real 2d
     - 
     - Non-linear matter power spectrum at samples in (Mpc/h)^{-3}
   * - wl_number_density
     - nbin
     - int
     - 
     - Number of redshift bins
   * - 
     - z
     - real 1d
     - 
     - Redshift values of n(z) samples
   * - 
     - bin_
     - real 1d
     - 
     - Bin n(z) values.  Need not be normalized. bin_1, bin_2, bin_3, ....
   * - matter_power_gal
     - z
     - real 1d
     - 
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P(k,z) samples in units of Mpc/h
   * - 
     - P_k
     - real 2d
     - 
     - Non-linear galaxy power spectrum at samples in (Mpc/h)^{-3}
   * - matter_power_gal_mass
     - z
     - real 1d
     - 
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P_{gm}(k,z) samples in units of Mpc/h
   * - 
     - P_k
     - real 2d
     - 
     - Non-linear galaxy-mass cross-power spectrum at samples in (Mpc/h)^{-3}


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - shear_cl
     - ell
     - real 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - shear_cl_ii
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - shear_cl_gi
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - matter_cl
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - ggl_cl
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - gal_IA_cross_cl
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - magnification_galaxy_cl
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - magnification_magnification_cl
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - magnification_intrinsic_cl
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.
   * - magnification_shear_cl
     - ell
     - int 1d
     - Sample ell values for output C_ell
   * - 
     - nbin
     - int
     - Number of redshift bins used
   * - 
     - bin_{i}_{j}
     - real 1d
     - C_ell (no l(l+1) factor) for (auto-correlation) bin i and j. Only stores j<=i.


