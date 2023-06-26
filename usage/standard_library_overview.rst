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
   * - :doc:`growth_factor <../reference/standard_library/growth_factor>` 
     - returns linear growth factor and growth rate for flat cosmology with either const w or variable DE eos w(a) = w + (1-a)*wa
   * - :doc:`astropy_background <../reference/standard_library/astropy_background>` 
     - Calculate background cosmology using astropy
   * - :doc:`distances <../reference/standard_library/distances>` 
     - Output cosmological distance measures for dynamical dark energy
   * - :doc:`log_w_model <../reference/standard_library/log_w_model>` 
     - Implement Tripathi, Sangwan, Jassal (2017) w(z) model



Boltzmann
-----------------------

Boltzmann codes evolve cosmic perturbations from the early Universe through recombination and to late times, and power spectra of matter, the CMB, and other quantities.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`class <../reference/standard_library/class>` 
     - Boltzmann and background integrator for BG, CMB, matter power, and more
   * - :doc:`isitgr-camb <../reference/standard_library/isitgr-camb>` 
     - Modified version of CAMB to implement phenomenological modified gravity models
   * - :doc:`mgcamb <../reference/standard_library/mgcamb>` 
     - Modified Gravity Boltzmann and background integrator for BG, CMB, and matter power
   * - :doc:`camb <../reference/standard_library/camb>` 
     - Boltzmann and background integrator for BG, CMB, and matter power



Structure
-----------------------

These modules compute aspects of cosmic structure, for example by emulating matter behaviour, integrating over it, or calculating halo model quantities.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`CosmicEmu <../reference/standard_library/CosmicEmu>` 
     - Emulate N-body simulations to compute nonlinear matter power
   * - :doc:`sigma_r <../reference/standard_library/sigma_r>` 
     - Compute anisotropy dispersion sigma(R,z)
   * - :doc:`constant_bias <../reference/standard_library/constant_bias>` 
     - Apply a galaxy bias constant with k and z.
   * - :doc:`extract_growth <../reference/standard_library/extract_growth>` 
     - returns growth factor and growth rate by examining small-scale P(k)
   * - :doc:`CRL_Eisenstein_Hu <../reference/standard_library/CRL_Eisenstein_Hu>` 
     - Komatsu's CRL code to compute the power spectrum using EH fitting formula.
   * - :doc:`Press_Schechter_MF <../reference/standard_library/Press_Schechter_MF>` 
     - Code to compute the PressSchechter mass function given Pk from CAMB, based on Komatsu's CRL
   * - :doc:`Extreme_Value_Statistics <../reference/standard_library/Extreme_Value_Statistics>` 
     - PDF of the maximum cluster mass given cosmological parameters
   * - :doc:`FrankenEmu <../reference/standard_library/FrankenEmu>` 
     - Emulate N-body simulations to compute nonlinear matter power
   * - :doc:`Sheth-Tormen MF <../reference/standard_library/Sheth-Tormen MF>` 
     - Code to compute the Sheth-Tormen mass function given Pk from CAMB, based on Komatsu's CRL
   * - :doc:`extrapolate <../reference/standard_library/extrapolate>` 
     - Simple log-linear extrapolation of P(k) to high k
   * - :doc:`sigma_cpp <../reference/standard_library/sigma_cpp>` 
     - Compute anisotropy dispersion sigma(R,z) in cpp
   * - :doc:`NLfactor <../reference/standard_library/NLfactor>` 
     - Compute nonlinear weyl potential (and other) spectrum by multiplying the linear spectrum with matter_power_nl/matter_power_lin
   * - :doc:`Tinker_MF <../reference/standard_library/Tinker_MF>` 
     - Code to compute the Tinker et al. mass function given Pk from CAMB, based on Komatsu's CRL



Two-point Mathemetics
-----------------------

These modules perform mathematical claculations associated with two-point statistics, mostly on a sphere.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`project_2d <../reference/standard_library/project_2d>` 
     - Project 3D power spectra to 2D tomographic bins using the Limber approximation
   * - :doc:`cl_to_xi_wigner_d <../reference/standard_library/cl_to_xi_wigner_d>` 
     - Compute correlation functions from power spectra
   * - :doc:`wl_spectra <../reference/standard_library/wl_spectra>` 
     - Compute various weak lensing C_ell from P(k,z) with the Limber integral
   * - :doc:`wl_spectra_ppf <../reference/standard_library/wl_spectra_ppf>` 
     - Compute weak lensing C_ell from P(k,z) and MG D(k,z) with the Limber integral
   * - :doc:`cl_to_corr <../reference/standard_library/cl_to_corr>` 
     - Compute correlation functions xi+, xi-, w, and gamma_t from C_ell
   * - :doc:`cl_to_xi_nicaea <../reference/standard_library/cl_to_xi_nicaea>` 
     - Compute WL correlation functions xi+, xi- from C_ell



Two-point Systematics
-----------------------

These modules compute and apply quantities associated with systematics errors on two-point (and potentially other) quantities.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`constant_bias <../reference/standard_library/constant_bias>` 
     - Apply a galaxy bias constant with k and z.
   * - :doc:`no_bias <../reference/standard_library/no_bias>` 
     - Generate galaxy power P(k) as though galaxies were unbiased DM tracers
   * - :doc:`linear_alignments <../reference/standard_library/linear_alignments>` 
     - Compute the terms P_II and P_GI which go into intrinsic aligment calculations
   * - :doc:`clerkin <../reference/standard_library/clerkin>` 
     - Compute galaxy bias as function of k, z for 3-parameter Clerkin et al 2014 model
   * - :doc:`kappa_ell_cut <../reference/standard_library/kappa_ell_cut>` 
     - Apply minimum and maximum ell to cross-power spectra with CMB kappa.
   * - :doc:`add_magnification <../reference/standard_library/add_magnification>` 
     - Add magnification terms to C_ell
   * - :doc:`ia_z_powerlap <../reference/standard_library/ia_z_powerlap>` 
     - 
   * - :doc:`add_intrinsic <../reference/standard_library/add_intrinsic>` 
     - Sum together intrinsic aligments with shear signal
   * - :doc:`kappa_beam <../reference/standard_library/kappa_beam>` 
     - Apply smoothing function to cross-correlations with CMB kappa in harmonic space.
   * - :doc:`baryonic <../reference/standard_library/baryonic>` 
     - Apply baryonic effects to nonlinear pk based on hydrodynamic simulation measurements
   * - :doc:`apply_astrophysical_biases <../reference/standard_library/apply_astrophysical_biases>` 
     - Apply various astrophysical biases to the matter power spectrum P(k,z)
   * - :doc:`shear_bias <../reference/standard_library/shear_bias>` 
     - Modify a set of calculated shear C_ell with a multiplicative bias



Sample Properties
-----------------------

These modules compute properties, mostly number density, of galaxy samples.

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`nz_multirank <../reference/standard_library/nz_multirank>` 
     - Load, rank, and sample a set of density n(z) realisations from a FITS file
   * - :doc:`photoz_bias <../reference/standard_library/photoz_bias>` 
     - Modify a set of loaded n(z) distributions with a multiplicative or additive bias
   * - :doc:`load_nz <../reference/standard_library/load_nz>` 
     - Load a number density n(z) for weak lensing from a file
   * - :doc:`smail <../reference/standard_library/smail>` 
     - Compute window functions for photometric n(z)
   * - :doc:`gaussian_window <../reference/standard_library/gaussian_window>` 
     - Compute Gaussian n(z) window functions for weak lensing bins
   * - :doc:`load_nz_fits <../reference/standard_library/load_nz_fits>` 
     - Load a number density n(z) from a FITS file
   * - :doc:`Joachimi_Bridle_alpha <../reference/standard_library/Joachimi_Bridle_alpha>` 
     - Calculate the gradient of the galaxy luminosity function at the limiting magnitude of the survey.



Likelihoods
-----------------------

These module provide likelihoods that compare theory predictions to data

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`pantheon <../reference/standard_library/pantheon>` 
     - Likelihood of the Pantheon supernova analysis
   * - :doc:`Cluster_mass <../reference/standard_library/Cluster_mass>` 
     - Likelihood of z=1.59 Cluster mass from Santos et al. 2011
   * - :doc:`wmap <../reference/standard_library/wmap>` 
     - Likelihood function of CMB from WMAP
   * - :doc:`6dFGS <../reference/standard_library/6dFGS>` 
     - Compute the likelihood of supplied D_v or fsigma8(z=0.067)
   * - :doc:`boss_dr12 <../reference/standard_library/boss_dr12>` 
     - Compute the likelihood of the supplied expansion and growth history against BOSS DR12 data
   * - :doc:`mgs_bao <../reference/standard_library/mgs_bao>` 
     - Compute the likelihood against SDSS MGS data
   * - :doc:`JulloLikelihood <../reference/standard_library/JulloLikelihood>` 
     - Likelihood of Jullo et al (2012) measurements of a galaxy bias sample
   * - :doc:`planck2018 <../reference/standard_library/planck2018>` 
     - Likelihood function of CMB from Planck 2015 data
   * - :doc:`balmes <../reference/standard_library/balmes>` 
     - 
   * - :doc:`eboss_dr16_lrg <../reference/standard_library/eboss_dr16_lrg>` 
     - Compute the likelihood of eBOSS DR16 from LRG
   * - :doc:`Riess11 <../reference/standard_library/Riess11>` 
     - Likelihood of hubble parameter H0 from Riess et al supernova sample
   * - :doc:`Riess21 <../reference/standard_library/Riess21>` 
     - Likelihood of hubble parameter H0 from Riess et al supernova sample
   * - :doc:`wmap_shift <../reference/standard_library/wmap_shift>` 
     - Massively simplified WMAP9 likelihood reduced to just shift parameter
   * - :doc:`h0licow <../reference/standard_library/h0licow>` 
     - 
   * - :doc:`fgas <../reference/standard_library/fgas>` 
     - Likelihood of galaxy cluster gas-mass fractions
   * - :doc:`BICEP2 <../reference/standard_library/BICEP2>` 
     - Compute the likelihood of the supplied CMB power spectra
   * - :doc:`planck_sz <../reference/standard_library/planck_sz>` 
     - Prior on sigma_8 * Omega_M ** 0.3 from Planck SZ cluster counts
   * - :doc:`jla <../reference/standard_library/jla>` 
     - Supernova likelihood for SDSS-II/SNLS3
   * - :doc:`mgs <../reference/standard_library/mgs>` 
     - Compute the likelihood of MGS BAO and FS as distributed by eBOSS DR16
   * - :doc:`eboss_dr14_lya <../reference/standard_library/eboss_dr14_lya>` 
     - Compute the likelihood of eBOSS DR14 D_m and D_h from Lyman alpha
   * - :doc:`eboss_dr16_lya <../reference/standard_library/eboss_dr16_lya>` 
     - Compute the likelihood of eBOSS DR16 from Lyman alpha
   * - :doc:`BOSS <../reference/standard_library/BOSS>` 
     - Compute the likelihood of supplied fsigma8(z=0.57), H(z=0.57), D_a(z=0.57), omegamh2, bsigma8(z=0.57)
   * - :doc:`BBN <../reference/standard_library/BBN>` 
     - Simple prior on Omega_b h^2 from light element abundances
   * - :doc:`strong_lens_time_delays <../reference/standard_library/strong_lens_time_delays>` 
     - 
   * - :doc:`boss_dr12_lrg_reanalyze <../reference/standard_library/boss_dr12_lrg_reanalyze>` 
     - Compute the likelihood of the supplied expansion and growth history against BOSS DR12 data as reanalyzed by eBOSS DR16
   * - :doc:`eboss_dr16_elg <../reference/standard_library/eboss_dr16_elg>` 
     - Compute the likelihood of eBOSS DR16 from ELG
   * - :doc:`eboss_dr16_qso <../reference/standard_library/eboss_dr16_qso>` 
     - Compute the likelihood of eBOSS DR16 from QSO
   * - :doc:`lrg <../reference/standard_library/lrg>` 
     - Compute the likelihood of eBOSS DR14 D_v from LRG
   * - :doc:`WiggleZBao <../reference/standard_library/WiggleZBao>` 
     - Compute the likelihood of the supplied expansion history against WiggleZ BAO data
   * - :doc:`Riess16 <../reference/standard_library/Riess16>` 
     - Likelihood of hubble parameter H0 from Riess et al 2.4% supernova sample
   * - :doc:`qso <../reference/standard_library/qso>` 
     - Compute the likelihood of eBOSS DR14 D_v from QSO
   * - :doc:`des-y3-bao <../reference/standard_library/des-y3-bao>` 
     - Compute the likelihood of DES Y3 BAO data
   * - :doc:`2pt <../reference/standard_library/2pt>` 
     - Generic 2-point measurement Gaussian likelihood



Misc & Utilities
-----------------------

These modules supply special utilities or calculation tools

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
   * - :doc:`fast_pt <../reference/standard_library/fast_pt>` 
     - Compute various 1-loop perturbation theory quantities
   * - :doc:`copy <../reference/standard_library/copy>` 
     - Copy a section to a new section
   * - :doc:`w0wa_sum_prior <../reference/standard_library/w0wa_sum_prior>` 
     - Skip parameter sample without failing if w0+wa>0.
   * - :doc:`stop <../reference/standard_library/stop>` 
     - Enters python debugger.
   * - :doc:`BBN-Consistency <../reference/standard_library/BBN-Consistency>` 
     - Compute consistent Helium fraction from baryon density given BBN
   * - :doc:`sigma8_rescale <../reference/standard_library/sigma8_rescale>` 
     - Rescale structure measures to use a specified sigma_8
   * - :doc:`delete <../reference/standard_library/delete>` 
     - Enters python debugger.
   * - :doc:`rename <../reference/standard_library/rename>` 
     - Rename a section to a new name
   * - :doc:`consistency <../reference/standard_library/consistency>` 
     - Deduce missing cosmological parameters and check consistency
