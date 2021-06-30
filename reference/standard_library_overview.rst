Standard Library Overview
==============================

The CosmoSIS standard library is a collection of modules
designed for Cosmological parameter estimation.  You can couple
together pieces of it to build analysis piplines.


Background
-----------------------

These modules calculate quantities related to the average background expansion of the Universe.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`growth_factor <standard_library/growth_factor>` 
     - returns linear growth factor and growth rate for flat cosmology with either const w or variable DE eos w(a) = w + (1-a)*wa
   * - :doc:`distances <standard_library/distances>` 
     - Output cosmological distance measures for dynamical dark energy



Boltzmann
-----------------------

Boltzmann codes evolve cosmic perturbations from the early Universe through recombination and to late times, and power spectra of matter, the CMB, and other quantities.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`mgcamb <standard_library/mgcamb>` 
     - Modified Gravity Boltzmann and background integrator for BG, CMB, and matter power
   * - :doc:`camb <standard_library/camb>` 
     - Boltzmann and background integrator for BG, CMB, and matter power
   * - :doc:`isitgr-camb <standard_library/isitgr-camb>` 
     - Modified version of CAMB to implement phenomenological modified gravity models
   * - :doc:`class <standard_library/class>` 
     - Boltzmann and background integrator for BG, CMB, matter power, and more



Structure
-----------------------

These modules compute aspects of cosmic structure, for example by emulating matter behaviour, integrating over it, or calculating halo model quantities.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`Sheth-Tormen MF <standard_library/Sheth-Tormen MF>` 
     - Code to compute the Sheth-Tormen mass function given Pk from CAMB, based on Komatsu's CRL
   * - :doc:`Press_Schechter_MF <standard_library/Press_Schechter_MF>` 
     - Code to compute the PressSchechter mass function given Pk from CAMB, based on Komatsu's CRL
   * - :doc:`FrankenEmu <standard_library/FrankenEmu>` 
     - Emulate N-body simulations to compute nonlinear matter power
   * - :doc:`extrapolate <standard_library/extrapolate>` 
     - Simple log-linear extrapolation of P(k) to high k
   * - :doc:`extract_growth <standard_library/extract_growth>` 
     - returns growth factor and growth rate by examining small-scale P(k)
   * - :doc:`Extreme_Value_Statistics <standard_library/Extreme_Value_Statistics>` 
     - PDF of the maximum cluster mass given cosmological parameters
   * - :doc:`CRL_Eisenstein_Hu <standard_library/CRL_Eisenstein_Hu>` 
     - Komatsu's CRL code to compute the power spectrum using EH fitting formula.
   * - :doc:`constant_bias <standard_library/constant_bias>` 
     - Apply a galaxy bias constant with k and z.
   * - :doc:`Tinker_MF <standard_library/Tinker_MF>` 
     - Code to compute the Tinker et al. mass function given Pk from CAMB, based on Komatsu's CRL
   * - :doc:`sigma_r <standard_library/sigma_r>` 
     - Compute anisotropy dispersion sigma(R,z)
   * - :doc:`sigma_cpp <standard_library/sigma_cpp>` 
     - Compute anisotropy dispersion sigma(R,z) in cpp
   * - :doc:`CosmicEmu <standard_library/CosmicEmu>` 
     - Emulate N-body simulations to compute nonlinear matter power



Two-point Mathemetics
-----------------------

These modules perform mathematical claculations associated with two-point statistics, mostly on a sphere.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`wl_spectra_ppf <standard_library/wl_spectra_ppf>` 
     - Compute weak lensing C_ell from P(k,z) and MG D(k,z) with the Limber integral
   * - :doc:`wl_spectra <standard_library/wl_spectra>` 
     - Compute various weak lensing C_ell from P(k,z) with the Limber integral
   * - :doc:`cl_to_xi_nicaea <standard_library/cl_to_xi_nicaea>` 
     - Compute WL correlation functions xi+, xi- from C_ell
   * - :doc:`cl_to_corr <standard_library/cl_to_corr>` 
     - Compute correlation functions xi+, xi-, w, and gamma_t from C_ell
   * - :doc:`project_2d <standard_library/project_2d>` 
     - Project 3D power spectra to 2D tomographic bins using the Limber approximation
   * - :doc:`shear_xi <standard_library/shear_xi>` 
     - Compute the likelihood of a tomographic shear correlation function data set
   * - :doc:`cl_to_xi_wigner_d <standard_library/cl_to_xi_wigner_d>` 
     - Compute correlation functions from power spectra



Two-point Systematics
-----------------------

These modules compute and apply quantities associated with systematics errors on two-point (and potentially other) quantities.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`ia_z_powerlap <standard_library/ia_z_powerlap>` 
     - 
   * - :doc:`kappa_beam <standard_library/kappa_beam>` 
     - Apply smoothing function to cross-correlations with CMB kappa in harmonic space.
   * - :doc:`kappa_ell_cut <standard_library/kappa_ell_cut>` 
     - Apply minimum and maximum ell to cross-power spectra with CMB kappa.
   * - :doc:`linear_alignments <standard_library/linear_alignments>` 
     - Compute the terms P_II and P_GI which go into intrinsic aligment calculations
   * - :doc:`add_intrinsic <standard_library/add_intrinsic>` 
     - Sum together intrinsic aligments with shear signal
   * - :doc:`constant_bias <standard_library/constant_bias>` 
     - Apply a galaxy bias constant with k and z.
   * - :doc:`clerkin <standard_library/clerkin>` 
     - Compute galaxy bias as function of k, z for 3-parameter Clerkin et al 2014 model
   * - :doc:`shear_bias <standard_library/shear_bias>` 
     - Modify a set of calculated shear C_ell with a multiplicative bias
   * - :doc:`no_bias <standard_library/no_bias>` 
     - Generate galaxy power P(k) as though galaxies were unbiased DM tracers
   * - :doc:`apply_astrophysical_biases <standard_library/apply_astrophysical_biases>` 
     - Apply various astrophysical biases to the matter power spectrum P(k,z)



Sample Properties
-----------------------

These modules compute properties, mostly number density, of galaxy samples.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`Joachimi_Bridle_alpha <standard_library/Joachimi_Bridle_alpha>` 
     - Calculate the gradient of the galaxy luminosity function at the limiting magnitude of the survey.
   * - :doc:`nz_hyperrank <standard_library/nz_hyperrank>` 
     - Load, rank, and sample a set of density n(z) realisations from a FITS file
   * - :doc:`load_nz_fits <standard_library/load_nz_fits>` 
     - Load a number density n(z) from a FITS file
   * - :doc:`photoz_bias <standard_library/photoz_bias>` 
     - Modify a set of loaded n(z) distributions with a multiplicative or additive bias
   * - :doc:`load_nz <standard_library/load_nz>` 
     - Load a number density n(z) for weak lensing from a file
   * - :doc:`smail <standard_library/smail>` 
     - Compute window functions for photometric n(z)
   * - :doc:`gaussian_window <standard_library/gaussian_window>` 
     - Compute Gaussian n(z) window functions for weak lensing bins



Likelihoods
-----------------------

These module provide likelihoods that compare theory predictions to data

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`pantheon <standard_library/pantheon>` 
     - Likelihood of the Pantheon supernova analysis
   * - :doc:`Riess16 <standard_library/Riess16>` 
     - Likelihood of hubble parameter H0 from Riess et al 2.4% supernova sample
   * - :doc:`mgs_bao <standard_library/mgs_bao>` 
     - Compute the likelihood against SDSS MGS data
   * - :doc:`fgas <standard_library/fgas>` 
     - Likelihood of galaxy cluster gas-mass fractions
   * - :doc:`strong_lens_time_delays <standard_library/strong_lens_time_delays>` 
     - 
   * - :doc:`boss_dr12 <standard_library/boss_dr12>` 
     - Compute the likelihood of the supplied expansion and growth history against BOSS DR12 data
   * - :doc:`BBN <standard_library/BBN>` 
     - Simple prior on Omega_b h^2 from light element abundances
   * - :doc:`planck2018 <standard_library/planck2018>` 
     - Likelihood function of CMB from Planck 2015 data
   * - :doc:`planck_sz <standard_library/planck_sz>` 
     - Prior on sigma_8 * Omega_M ** 0.3 from Planck SZ cluster counts
   * - :doc:`Riess11 <standard_library/Riess11>` 
     - Likelihood of hubble parameter H0 from Riess et al supernova sample
   * - :doc:`balmes <standard_library/balmes>` 
     - 
   * - :doc:`BICEP2 <standard_library/BICEP2>` 
     - Compute the likelihood of the supplied CMB power spectra
   * - :doc:`wmap_shift <standard_library/wmap_shift>` 
     - Massively simplified WMAP9 likelihood reduced to just shift parameter
   * - :doc:`Cluster_mass <standard_library/Cluster_mass>` 
     - Likelihood of z=1.59 Cluster mass from Santos et al. 2011
   * - :doc:`BOSS <standard_library/BOSS>` 
     - Compute the likelihood of supplied fsigma8(z=0.57), H(z=0.57), D_a(z=0.57), omegamh2, bsigma8(z=0.57)
   * - :doc:`2pt <standard_library/2pt>` 
     - Generic 2-point measurement Gaussian likelihood
   * - :doc:`6dFGS <standard_library/6dFGS>` 
     - Compute the likelihood of supplied D_v or fsigma8(z=0.067)
   * - :doc:`WiggleZBao <standard_library/WiggleZBao>` 
     - Compute the likelihood of the supplied expansion history against WiggleZ BAO data
   * - :doc:`h0licow <standard_library/h0licow>` 
     - 
   * - :doc:`jla <standard_library/jla>` 
     - Supernova likelihood for SDSS-II/SNLS3
   * - :doc:`wmap <standard_library/wmap>` 
     - Likelihood function of CMB from WMAP
   * - :doc:`JulloLikelihood <standard_library/JulloLikelihood>` 
     - Likelihood of Jullo et al (2012) measurements of a galaxy bias sample



Misc & Utilities
-----------------------

These modules supply special utilities or calculation tools

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`sigma8_rescale <standard_library/sigma8_rescale>` 
     - Rescale structure measures to use a specified sigma_8
   * - :doc:`stop <standard_library/stop>` 
     - Enters python debugger.
   * - :doc:`BBN-Consistency <standard_library/BBN-Consistency>` 
     - Compute consistent Helium fraction from baryon density given BBN
   * - :doc:`consistent_parameters <standard_library/consistent_parameters>` 
     - Deduce missing cosmological parameters and check consistency
