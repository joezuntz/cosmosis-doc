camb
================================================

Boltzmann and background integrator for BG, CMB, and matter power

+-------------+---------------------------------------+
| File        | boltzmann/camb/camb_interface.py      |
+-------------+---------------------------------------+
| Attribution | Antony Lewis                          |
+-------------+---------------------------------------+
|             | Anthony Challinor (camb)              |
+-------------+---------------------------------------+
|             | Tilman Troester                       |
+-------------+---------------------------------------+
|             | Angela Chen (interface)               |
+-------------+---------------------------------------+
| URL         | http://camb.info                      |
+-------------+---------------------------------------+
| Citations   | http://arxiv.org/abs/1201.3654        |
+-------------+---------------------------------------+
|             | http://arxiv.org/abs/astro-ph/9911177 |
+-------------+---------------------------------------+

The Code for Anisotropies in the Microwave Background, using the
newer python interface, which must be installed separately.

CAMB is the standard cosmology code for evolving perturbations
in the primordial universe into CMB and matter power spectra, as
well as various auxiliary quantities.

See http://camb.info for a fuller description

It has a wide variety of options only a few of which are currently
exposed here.  This will be extended in future.  This version of
camb has been modified very slightly to output a few new pieces
of data useful in other modules, notably the dark matter density
history rho(z) (which can vary in non-lcdm models)

The CosmoSIS team wrote the interface here, so if you have any issues
running it here please ask us first.


Assumptions
-----------

 - The wLCDM model



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - mode
     - str
     - 
     - Choose from Background, thermal, cmb, power, or all. In background mode only the expansion history is calculated. In thermal mode the recombination history is computed and rs_zdrag and related quantities also. In cmb mode the CMB power spectra are also calculated. In power mode the CMB is not calculated but low-z mattter power is.  In all mode everything is calculated.
   * - feedback
     - int
     - 0
     - Amount of output to print.  0 for no feedback.  1 for basic, 2 for extended, maybe higher?
   * - max_printed_errors
     - int
     - 20
     - Max number of full tracebacks to print when camb fails
   * - do_lensing
     - bool
     - False
     - Include lensing of CMB, and save C_ell phi-phi.
   * - do_reionization
     - bool
     - True
     - Use the tanh reionization model to calculate the reionization history.
   * - do_tensors
     - bool
     - False
     - Include tensor modes.
   * - do_vectors
     - bool
     - False
     - Vector modes.
   * - power_spectra
     - str
     - delta_tot
     - Which power spectra to save. Any combination of delta_cdm, delta_baryon, delta_photon, delta_neutrino, delta_nu, delta_tot, delta_nonu, delta_nonu, weyl, v_newtonian_cdm, v_newtonian_baryon, v_baryon_cdm, separated by spaces.
   * - nonlinear
     - str
     - none
     - One of 'none', 'pk', 'lens', 'both'.  Determining whether to generate NL p(k,z) and to apply NL corrections to lensing. /both depending on mode choice
   * - halofit_version
     - str
     - mead
     - If nonlinear!=none, select a halofit version from original, bird, peacock, takahashi, mead, halomodel, casarini, mead2015.
   * - initial
     - str
     - adiabatic
     - One of adiabatic, iso_CDM, iso_baryon, iso_neutrino, iso_neutrino_vel.  Scalar initial conditions.
   * - neutrino_hierarchy
     - str
     - degenerate
     - Choose from 'degenerate', 'normal', or 'inverted' (1 or 2 eigenstate approximation).
   * - use_ppf_w
     - bool
     - False
     - Whether to use the PPF perturbation approximation (arXiv:0808.3125) instead of the constant sound-speed single fluid model
   * - use_tabulated_w
     - bool
     - False
     - Set to true to load w(z) from the datablock instead of assuming a model
   * - pivot_scalar
     - real
     - 0.05
     - Pivot scale for scalar spectrum
   * - pivot_tensor
     - real
     - 0.05
     - Pivot scale for tensor spectrum
   * - lmax
     - int
     - 2600
     - Only if mode in cmb,all. The max ell to use for cmb calculation
   * - kmax
     - real
     - 10.0
     - Max wavenumber k to calculate P(k,z)
   * - kmax_extrapolate
     - real
     - kmax
     - Max wavenumber k to save P(k,z), extrapolating log-linearly beyond calculation
   * - nk
     - int
     - 200
     - Number of k values to save P(k,z).
   * - zmin
     - real
     - 0.0
     - Min redshift value to save P(k,z).
   * - zmax
     - real
     - 3.01
     - Max redshift value to save P(k,z)
   * - nz
     - int
     - 150
     - Number of z values to save P(k,z)
   * - zmid
     - real
     - 
     - If set then use two ranges of z values, zmin-zmid and zmid-zmax, with different nz values
   * - nzmid
     - int
     - 
     - Number of redshift points to use in lower range zmin-zmid, if set
   * - zmin_background
     - real
     - 0.0
     - Min redshift value to save distance measures.
   * - zmax_background
     - real
     - zmax
     - Max redshift value to save distance measures
   * - nz_background
     - int
     - nz
     - Number of z values to save distance measures
   * - do_bao
     - bool
     - True
     - Whether to save BAO quantities rs_DV and F_AP. Switch off to save time in SN-only runs.
   * - theta_H0_range
     - str
     - 10 100
     - Two space-separated values with the min and max H0 values to use when sampling in cosmomc_theta instead of H0.
   * - max_eta_k
     - real
     - ell-dependent
     - Maximum k*eta_0 for scalar C_ell, where eta_0 is the conformal time today.
   * - k_eta_fac
     - real
     - 2.5
     - Default factor for setting max_eta_k = k_eta_fac*lmax if max_eta_k=None.
   * - k_per_logint
     - int
     - 0
     - Number of k steps per log k, or zero for camb automatic assignment.
   * - lAccuracyBoost
     - real
     - 1.0
     - Factor to increase the maximum ell included in the Boltzmann hierarchies.
   * - lens_k_eta_reference
     - real
     - 18000.0
     - Value of max_eta_k to use when lens_potential_accuracy>0; use k_eta_max = lens_k_eta_reference*lens_potential_accuracy
   * - lens_margin
     - int
     - 150
     - The Delta lmax to use to ensure lensed C_ell are correct at lmax.
   * - lens_potential_accuracy
     - real
     - 1.0
     - Set to 1 or higher if you want to get the lensing potential accurate (1 is Planck-level accuracy)
   * - AccuracyBoost
     - real
     - 1.0
     - Apply an accuracy boost across all calculations.
   * - accurate_massive_neutrinos
     - bool
     - False
     - True if you want neutrino transfer functions accurate.
   * - min_kh_nonlinear
     - real
     - 0.005
     - Minimum k/h at which to apply non-linear corrections
   * - lSampleBoost
     - real
     - 1.0
     - Factor to increase density of ell sampling for CMB
   * - use_optical_depth
     - bool
     - True
     - Whether to use the tau parametrization of reionization instead of z.
   * - DoLateRadTruncation
     - bool
     - True
     - Whether to use smooth approx to radiation perturbations after decoupling on small scales, saving evolution of irrelevant osciallatory multipole equations.
   * - include_helium_fullreion
     - bool
     - True
     - Whether to include second reionization of helium
   * - tau_max_redshift
     - real
     - 50.0
     - Maxmimum redshift allowed when mapping tau into reionization redshift
   * - tau_solve_accuracy_boost
     - real
     - 1.0
     - Accuracy boosting parameter for solving for z_re from tau
   * - tau_timestep_boost
     - real
     - 1.0
     - Accuracy boosting parameter for the minimum number of time sampling steps through reionization


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
     - ombh2
     - real
     - 
     - Physical baryon density
   * - 
     - omch2
     - real
     - 
     - Physical cold dark matter density
   * - 
     - omega_k
     - real
     - 
     - Curvature density
   * - 
     - n_s
     - real
     - 
     - Primordial scalar spectral index
   * - 
     - A_s
     - real
     - 
     - Primordial scalar spectral amplitude
   * - 
     - sigma_8
     - real
     - 
     - Amplitude of linear perturbations at z=0 on scales of 8 Mpc/h. Only A_s or sigma_8 should be provided.
   * - 
     - hubble
     - real
     - 
     - Hubble parameter in km/s/Mpc
   * - 
     - h0
     - real
     - 
     - Hubble parameter in km/s/Mpc/100 (searched for if hubble not found)
   * - 
     - cosmomc_theta
     - real
     - 
     - Acoustic scale parameter (if hubble and h0 not found)
   * - 
     - tau
     - real
     - 
     - Optical depth to reionization (use_optical_depth=T)
   * - 
     - w
     - real
     - -1.0
     - W(z=0) equation of state of dark energy. Ignored if use_tabulated_w=T
   * - 
     - wa
     - real
     - 0.0
     - Equation of state parameter w(z) = w_0 + w_a z / (1+z). Ignored if use_tabulated_w=T
   * - 
     - cs2_de
     - real
     - 1.0
     - Dark energy sound speed/c
   * - 
     - nrun
     - real
     - 0.0
     - Running of the scalar spectral index
   * - 
     - nrunrun
     - real
     - 0.0
     - Second order running of the scalar spectral index
   * - 
     - r
     - real
     - 0.0
     - Tensor to scalar ratio at pivot
   * - 
     - nt
     - real
     - inflation consistency
     - Tensor spectral index
   * - 
     - ntrun
     - real
     - 0.0
     - Running of tensor spectral index
   * - 
     - TCMB
     - real
     - 2.7255
     - CMB temperature today
   * - 
     - YHe
     - real
     - BBN consistency
     - Helium mass fraction
   * - 
     - num_massive_neutrinos
     - int
     - 1
     - Number of massive neutrino species
   * - 
     - mnu
     - real
     - 0.06
     - Sum of neutrino masses (in eV); Omega_nu is calculated approximately from this.
   * - 
     - nnu
     - real
     - 3.046
     - N_eff, the effective relativistic degrees of freedom
   * - 
     - standard_neutrino_neff
     - real
     - 3.046
     - Default value for N_eff in fiducial cosmology used to calculate omnhu2
   * - 
     - A_lens
     - real
     - 1.0
     - Scaling of the lensing potential compared to theory prediction
   * - reionization
     - redshift
     - real
     - 
     - Reionization redshift to use if use_optical_depth=False
   * - 
     - delta_redshift
     - real
     - 
     - Duration of reionization if use_optical_depth=False
   * - 
     - fraction
     - real
     - -1.0
     - Reionization fraction when complete, or -1 for full ionization of hydrogen and first ionization of helium
   * - 
     - helium_redshift
     - real
     - 3.5
     - Redshift for second reionization of helium
   * - 
     - helium_delta_redshift
     - real
     - 0.4
     - Width in redshift for second reionization of helium
   * - 
     - helium_redshiftstart
     - real
     - 5.5
     - Include second helium reionizatio below this redshift
   * - recfast
     - min_a_evolve_Tm
     - real
     - 1.0
     - Minimum scale factor at which to solve matter temperature perturbation if evolving sound speed or ionization fraction perturbations (/(1+900)
   * - 
     - RECFAST_fudge
     - real
     - 1.14
     - Float Hydrogen fudge parameter
   * - 
     - RECFAST_fudge_He
     - real
     - 0.86
     - Helium fudge parameter
   * - 
     - RECFAST_Heswitch
     - int
     - 6
     - 0-6, method to use for calculating Helium recombination. See camb docs.
   * - 
     - RECFAST_Hswitch
     - bool
     - True
     - Whether to include H recombination corrections
   * - 
     - AGauss1
     - real
     - -0.14d
     - Amplitude of 1st recfast Gaussian
   * - 
     - AGauss2
     - real
     - 0.079
     - Amplitude of 2nd recfast Gaussian
   * - 
     - zGauss1
     - real
     - 7.28
     - ln(1+z) of 1st recfast Gaussian
   * - 
     - zGauss2
     - real
     - 6.73
     - ln(1+z) of 2nd recfast Gaussian
   * - 
     - wGauss1
     - real
     - 0.18
     - Width of 1st recfast Gaussian
   * - 
     - wGauss2
     - real
     - 0.33
     - Width of 2nd recfastGaussian
   * - halo_model_parameters
     - A
     - real
     - 
     - Amplitude of the concentration-mass relation
   * - 
     - eta
     - real
     - 
     - Real halo window function re-scaling parameter
   * - de_equation_of_state
     - a
     - real 1d
     - none
     - Scale factor a values used if use_tabulated_w=T.
   * - 
     - w
     - real 1d
     - none
     - Wquation of state w(a) values used if use_tabulated_w=T.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - cosmological_parameters
     - sigma_8
     - real
     - Amplitude of linear matter power at 8/h Mpc at z=0.  Only calculated if mode=all
   * - distances
     - nz
     - int
     - Number of distance samples
   * - 
     - z
     - real 1d
     - Redshifts of distance samples
   * - 
     - a
     - real 1d
     - Scale factor of distance samples
   * - 
     - d_a
     - real 1d
     - Angular diameter distance in Mpc
   * - 
     - d_m
     - real 1d
     - Co-moving distance in Mpc
   * - 
     - d_l
     - real 1d
     - Luminosity distance in Mpc
   * - 
     - mu
     - real 1d
     - Distance modulus
   * - 
     - h
     - real 1d
     - Hubble parameter with in units of Mpc
   * - 
     - age
     - real
     - Age of universe in GYr
   * - 
     - zstar
     - real
     - Redshift of unity optical depth.  Only if mode!=background
   * - 
     - thetastar
     - real
     - Angular size of sound horizon at zstar. Only if mode!=background
   * - 
     - DAstar
     - real
     - Angular diameter distance to zstar. Only if mode!=background
   * - 
     - chistar
     - real
     - Comoving distance to zstar. Only if mode!=background
   * - 
     - zdrag
     - real
     - Redshift where baryons no longer dragged by photons. Only if mode!=background
   * - 
     - rdrag
     - real
     - Sound horizon size at zdrag. Only if mode!=background
   * - 
     - rs_zdrag
     - real
     - Same as rdrag
   * - 
     - kd
     - real
     - K parameter at drag epoch
   * - 
     - thetad
     - real
     - Theta parameter at drag epoch
   * - 
     - zeq
     - real
     - Redshift of matter-radiation equality
   * - 
     - keq
     - real
     - Wavenumber (1/a) (da/dtau) at equality
   * - 
     - thetaeq
     - real
     - Angle 100 tau_eq / D_A(zstar)
   * - 
     - thetarseq
     - real
     - Angle 100 r_s(eq)/DA(zstar)
   * - growth_parameters
     - z
     - real 1d
     - Redshift samples of other values in this section, (all if mode=power or all)
   * - 
     - a
     - real 1d
     - Scale factor samples of other values in this section
   * - 
     - sigma_8
     - real 1d
     - Amplitude of linear matter power as function of z sigma_8(z)
   * - 
     - fsigma_8
     - real 1d
     - Growth rate (f*sigma_8)(z)
   * - 
     - rs_DV
     - real 1d
     - (rs_zdrag / volume distance D_V)(z)
   * - 
     - H
     - real 1d
     - Hubble parameter H(z). Repeated here at this sampling since useful to have BAO values at same z values
   * - 
     - DA
     - real 1d
     - Angular diameter distance D_A(z)
   * - 
     - F_AP
     - real 1d
     - Alcock-Paczynski factor  (D_A * H / c)(z)
   * - 
     - d_z
     - real 1d
     - Growth factor D(z)
   * - 
     - f_z
     - real 1d
     - Growth rate f(z)=dlog(D)/dlog(a)
   * - cmb_cl
     - ell
     - int 1d
     - Angular frequencies. Only if mode=cmb or all
   * - 
     - tt
     - real 1d
     - ell * (ell+1) C_ell^TT / 2 pi in mu K^2. Only if mode=cmb or all
   * - 
     - ee
     - real 1d
     - ell * (ell+1) C_ell^EE / 2 pi in mu K^2. Only if mode=cmb or all
   * - 
     - bb
     - real 1d
     - ell * (ell+1) C_ell^BB / 2 pi in mu K^2. Only if mode=cmb or all
   * - 
     - te
     - real 1d
     - ell * (ell+1) C_ell^TE / 2 pi in mu K^2. Only if mode=cmb or all
   * - 
     - pp
     - real 1d
     - Phi-Phi lensing spectrum; note ell scaling: ell * (ell+1) C_ell^PhiPhi. Only if mode=cmb or all
   * - 
     - pt
     - real 1d
     - Phi-T lensing spectrum; note ell scaling: ell * (ell+1) C_ell^PhiT. Only if mode=cmb or all
   * - 
     - pe
     - real 1d
     - Phi-E lensing spectrum; note ell scaling: ell * (ell+1) C_ell^PhiE. Only if mode=cmb or all
   * - matter_power_lin
     - z
     - real 1d
     - Redshifts of samples. Only if mode is 'all' or 'power', nonlinear!=none and matter_power is switched on in the power_spectra option. Other values specified in power_spectra will output equivalent sections.
   * - 
     - k_h
     - real 1d
     - Wavenumbers k of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - Linear power spectrum at samples in (Mpc/h)^-3.
   * - matter_power_nl
     - z
     - real 1d
     - Redshifts of samples. Only if mode is 'all' or 'power', and matt is switched on in the power_spectra option. Other values specified in power_spectra will output equivalent sections.
   * - 
     - k_h
     - real 1d
     - Wavenumbers k of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - Non-linear power spectrum at samples in (Mpc/h)^-3.


