project_2d
================================================

Project 3D power spectra to 2D tomographic bins using the Limber approximation

.. list-table::
    
   * - File
     - structure/projection/project_2d.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


The Limber approximation integrates a 3D power spectrum over the radial
direction to get a 2D angular power spectrum.  It is an approximation
which is only valid on smaller scales.

C_\ell =  A \int_0^{\chi_1} W_1(\chi) W_2(\chi) P(k=(l+0.5)/\chi, z(\chi)) / chi^2 d\chi

The full integral must integrate over k(\ell) also.
This module is a python interface to a Limber integrator written in C, and can 
generate a range of different spectra depending on what options you set.

It can generate spectra for any pair of
    (Shear, Position, Intrinsic, Magnification, Cmbkappa)
though beware that for certain combinations and scales the Limber approximation will 
be inaccurate.

Depending which spectra you ask for, it will look for different input P(k) value:

    Option name                       Input-3d-spectrum                 Default output name
    
    shear-shear                       matter_power_nl                   shear_cl
    weyl-weyl                         weyl_curvature_spectrum_nl        shear_cl
    shear-intrinsic                   matter_intrinsic_power            shear_cl_gi
    intrinsic-intrinsic               intrinsic_power                   shear_cl_ii
    intrinsicb-intrinsicb             intrinsic_power_bb                shear_cl_bb
    position-position                 matter_power_nl                   galaxy_cl
    magnification-density             matter_power_nl                   magnification_density_cl
    magnification-magnification       matter_power_nl                   magnification_cl
    position-shear                    matter_power_nl                   galaxy_shear_cl
    density-intrinsic                 matter_intrinsic_power            galaxy_intrinsic_cl
    magnification-intrinsic           matter_intrinsic_power            magnification_intrinsic_cl
    magnification-shear               matter_power_nl                   magnification_shear_cl
    shear-cmbkappa                    matter_power_nl                   shear_cmbkappa_cl
    cmbkappa-cmbkappa                 matter_power_nl                   cmbkappa_cl
    intrinsic-cmbkappa                matter_intrinsic_power            intrinsic_cmbkappa_cl
    density-cmbkappa                  matter_power_nl                   galaxy_cmbkappa_cl
    fast-shear-shear-ia               matter_power_nl                   shear_cl
    fast-lingal-shear-ia              matter_power_nl                   galaxy_shear_cl
    fast-position-shear-ia            matter_power_nl                   galaxy_shear_cl
    lingal-lingal                     matter_power_nl                   galaxy_cl
    lingal-shear                      matter_power_nl                   galaxy_shear_cl
    lingal-magnification              matter_power_nl                   galaxy_magnification_cl
    lingal-intrinsic                  matter_intrinsic_power            galaxy_intrinsic_cl
    nlgal-nlgal                       matter_power_nl                   galaxy_cl
    nlgal-shear                       matter_power_nl                   galaxy_shear_cl
    nlgal-magnification               matter_power_nl                   galaxy_magnification_cl


For each of the spectra listed above you can set a parameter in the parameter file 
to describe whether that term should be calculated and what input n(z) and output
names should be used for it.

You can set either:
shear-shear = T   ; to use the default wl_number_density n(z) section and save to default shear_cl
shear-shear = euclid-ska  ; to cross-correlate n(z) from nz_euclid and nz_ska sections, and save to shear_cl
shear-shear = red-red:shear_cl_red  ; to auto-correlate n(z) from the nz_red section and then save to shear_cl_red

If no spectra are chosen at all then only "shear-shear=T" is assumed.

The same forms can be used for all the other spectra, though note that the magnification spectra
also require information on the luminosity function.

Lingal refers to clustering spectra for a linearly-biased sample. Nlgal is for non-linearly biased samples.

Parts of this code and the underlying implementation of limber are based on cosmocalc:
https://bitbucket.org/beckermr/cosmocalc-public


Assumptions
-----------

 - The Limber approximation is reasonable for the fields being integrated
 - Flat sky approximation
 - GR is assumed in various ways



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - verbose
     - bool
     - False
     - Print more output.
   * - fatal_errors
     - bool
     - False
     - Raise an error instead of returning non-zero on error loading splines. Handy for debugging.
   * - get_kernel_peaks
     - bool
     - False
     - Save peak positions for the computed kernels
   * - do_exact
     - str
     - 
     - Spectra for which to do exact (non-limber) calculation at low ell (space-separated)
   * - auto_only
     - str
     - 
     - Spectra for which to only compute auto-correlations, not inter-bin correlations (space-separated)
   * - clip_chi_kernels
     - float
     - 1e-06
     - Fraction of the integration kernel peaks below which to set the kernel to zero
   * - sig_over_dchi
     - float
     - 50.0
     - Ratio of the kernel width to sampling. Sets the sampling of the kernels. Larger is more precise.
   * - shear_kernel_dchi
     - float
     - 5.0
     - Sample spacing for shear kernels
   * - limber_ell_start
     - int
     - 300
     - For spectra listed in do_exact, the minimum ell to switch to Limber
   * - ell_min_logspaced
     - real
     - -1
     - Minimum ell value for log-spaced values (usually higher than linear)
   * - ell_max_logspaced
     - real
     - -1
     - Maximum ell value for log-spaced values (usually higher than linear)
   * - n_ell_logspaced
     - real
     - -1
     - Number of log-spaced C_ell values produced
   * - ell_min_linspaced
     - real
     - -1
     - Minimum ell value for linearly-spaced values (usually lower than log-spaced)
   * - ell_max_linspaced
     - real
     - -1
     - Maximum ell value for linearly-spaced values (usually higher than log-spaced)
   * - n_ell_linspaced
     - real
     - 
     - Number of linearly-spaced C_ell values produced
   * - dlogchi
     - int
     - -1
     - spacing in log-chi for exact non-limber calculation (or -1 to auto-set)
   * - chi_pad_upper
     - float
     - 2.0
     - Lower padding fraction in chi for non-limber calculation
   * - shear-shear
     - str or bool
     - 
     - See note in the explanation above for this and related parameters
   * - limber_abs_tol
     - real
     - 0.0
     - Absolute tolerance for the Limber integral
   * - limber_rel_tol
     - real
     - 0.001
     - Relative tolerance for the Limber integral
   * - lin_bias_prefix
     - str
     - b
     - Parameter name to use for linear bias values, e.g. b for b1, b2, b3, etc.
   * - do_rsd
     - bool
     - False
     - Whether to compute RSD in non-limber calculations


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - matter_power_nl
     - k_h
     - real 1d
     - 
     - Sample values of nonlinear spectrum in Mpc/h. Many inputs P(k) sections may be required depending on what C_ell spectra are requested - see above.
   * - 
     - z
     - real 1d
     - 
     - Redshift of nonlinear spectrum samples
   * - 
     - P_k
     - real 2d
     - 
     - Nonlinear spectrum in (Mpc/h)^{-3}
   * - distances
     - z
     - real 1d
     - 
     - Redshift samples of d_m
   * - 
     - a
     - real 1d
     - 
     - Scale factor samples of d_m
   * - 
     - d_m
     - real 1d
     - 
     - Comoving distance to sample points.
   * - cosmological_parameters
     - h0
     - real
     - 
     - The Hubble parameter H0/100 km/s/Mpc
   * - 
     - chi_star
     - real
     - 
     - CMB distance. Only needed if doing CMB Kappa spectra.
   * - wl_number_density
     - z
     - real 1d
     - 
     - Redshift samples of binned n(z). A different section name to wl_number_density will be used depending on the options chosen (see above)
   * - 
     - nbin
     - int
     - 
     - Number of tomographic bins used
   * - 
     - bin_{i}
     - real 1d
     - 
     - Number density n(z) samples for each bin i=1..nbin.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - shear_cl
     - nbin_a
     - int
     - Number of tomographic bins for first of the two quantities correlated. Various sections will have these outputs depending on the options chosen
   * - 
     - nbin_b
     - int
     - Number of tomographic bins for second of the two quantities correlated
   * - 
     - nbin
     - int
     - Only if auto-correlation is calculated. Number of tomographic bins for the quantity (nbin=nbin_a=nbin_b)
   * - 
     - ell
     - int 1d
     - Values at which c_ell are calculated
   * - 
     - bin_{i}_{j}
     - real 1d
     - S for relevant i and j combinations. C_ell calculated at corresponding ell.
   * - 
     - chi_peak_{i}_{j}
     - real
     - Only if get_kernel_peaks=T. Peak of the n(z) or w(z) for this bin combination
   * - 
     - arcmin_per_Mpch_{i}_{j}
     - real
     - Only if get_kernel_peaks=T. Conversion factor from mpc/h to arcmin for this bin


