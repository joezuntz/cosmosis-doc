mgcamb
================================================

Modified Gravity Boltzmann and background integrator for BG, CMB, and matter power

.. list-table::
    
   * - File
     - boltzmann/mgcamb/camb.so
   * - Attribution
     - A. Hojjati
   * -
     - G.B. Zhao
   * -
     - L. Pogosian
   * -
     - A. Silvestri
   * -
     - Antony Lewis
   * -
     - Anthony Challinor
   * - URL
     - http://www.sfu.ca/~aha25/MGCAMB.html
   * - Citation
     - http://arxiv.org/abs/1106.4543
   * -
     - http://arxiv.org/abs/0809.3791
   * - Rules
     - Please abide by the conditions set out in the CAMB license if you use this module http://camb.info/CAMBsubmit.html


See the CAMB module for a general introduction to CAMB.

MGCAMB is a modified version of CAMB in which the linearized 
Einstein equations of General Relativity (GR) are modified.

It implements several different parameterizations, which are described on this page:
http://www.sfu.ca/~aha25/Models.html
and referred to here as:
model 0 : default GR
model 1 : BZ(mu,gamma) ( introduced in arXiv:0801.2431)
model 2 : (Q,R) ( introduced in arXiv:1002.4197 )
model 3 : (Q0,R0,s)( introduced in arXiv:1002.4197 )
model 4 : f(R) ( introduced in arXiv:0909.2045 )
model 5 : Chameleon ( introduced in arXiv:0909.2045 )
model 6 : Linder's gamma (introduced in arXiv:0507263 )



Assumptions
-----------

 - One of several modification ansatzes specifying changes from GR
 - wCDM background evolution
 - Other camb assumptions



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
     - Choose from Background, thermal, cmb, or all. In background mode only the expansion history is calculated. In thermal mode the recombination history is computed and rs_zdrag and related quantities also. In cmb mode the CMB power spectra are also calculated. In all mode the matter power spectrum at low redshift and sigma8 are also calculated.
   * - mg_model
     - int
     - 
     - From 0-6, choice of MG model to use
   * - lmax
     - int
     - 
     - Only if mode!=background, default 1200 - the max ell to use for cmb calculation
   * - feedback
     - int
     - 
     - Amount of output to print.  0 for no feedback.  1 for basic, 2 for extended.
   * - use_tabulated_w
     - bool
     - False
     - Set to true to load w(z) from previous module
   * - k_eta_max_scalar
     - int
     - 
     - Maximum value of (k eta) to evolve for scalars. (default 2*lmax)
   * - do_tensors
     - bool
     - False
     - Include tensor modes
   * - zmin
     - real
     - 0.0
     - Min value to save P(k,z)
   * - zmax
     - real
     - 4.0
     - Max value to save P(k,z)
   * - nz
     - int
     - 401
     - Number of z values to save P(k,z) (default gives dz=0.01)
   * - do_nonlinear
     - bool
     - False
     - Apply non-linear halofit corrections to matter-power.  Relevant only for lensing right now
   * - do_lensing
     - bool
     - False
     - Include lensing of CMB, and save C_ell phi-phi
   * - high_ell_template
     - str
     - 
     - Required for lensing - set to the file included in the camb dir


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - modified_gravity
     - grtrans
     - real
     - 
     - Scale factor of transition from GR
   * - 
     - b1
     - real
     - 
     - Model 1, beta 1 in mu(a,k)
   * - 
     - b2
     - real
     - 
     - Model 1, beta 2 in gamma(a,k)
   * - 
     - lambda1_2
     - real
     - 
     - Model 1, lambda_1^2 in mu(a,k)
   * - 
     - lambda2_2
     - real
     - 
     - Model 1, lambda_2^2 in gamma(a,k)
   * - 
     - ss
     - real
     - 
     - Model 1,  scale factor power index in mu and gamma
   * - 
     - MGQfix
     - real
     - 
     - Model 2, Constant Q value
   * - 
     - MGRfix
     - real
     - 
     - Model 2, Constant R value
   * - 
     - Qnot
     - real
     - 
     - Model 3, Q_0 term in Q(k,a)
   * - 
     - Rnot
     - real
     - 
     - Model 3, R_0 term in R(k,a)
   * - 
     - sss
     - real
     - 
     - Model 3, scale factor power index for Q and R
   * - 
     - b0
     - real
     - 
     - Models 4 & 5, B_0 term that goes into lambda_1^2 in mu(a,k)
   * - 
     - beta1
     - real
     - 
     - Model 5, beta_1 term that goes into lambda_2^2 term in mu(a,k)
   * - 
     - s
     - real
     - 
     - Model 5 scale factor power index for mu
   * - 
     - linder_gamma
     - real
     - 
     - Model 6, gamma_L power law in Omega_M for growth rate
   * - cosmological_parameters
     - omega_b
     - real
     - 
     - Baryon density fraction today
   * - 
     - omega_c
     - real
     - 
     - CDM density fraction today
   * - 
     - omega_k
     - real
     - 0.0
     - Curvature density fraction today
   * - 
     - omega_lambda
     - real
     - 
     - Dark energy density fraction today
   * - 
     - hubble
     - real
     - 
     - Hubble parameter H0 (km/s/Mpc)
   * - 
     - tau
     - real
     - 
     - Optical depth to last-scattering (ignored in background mode)
   * - 
     - n_s
     - real
     - 
     - Scalar spectral index (ignored in background/thermal mode)
   * - 
     - A_s
     - real
     - 
     - Scalar spectrum primordial amplitude (ignored in background/thermal mode)
   * - 
     - k_s
     - real
     - 
     - Power spectrum pivot scale (default 0.05/Mpc)
   * - 
     - r_t
     - real
     - 0.0
     - Tensor to scalar ratio
   * - 
     - n_run
     - real
     - 0.0
     - Running of scalar spectrum d n_s / d log_k
   * - 
     - n_t
     - real
     - 0.0
     - Tensor spectral index
   * - 
     - omega_nu
     - real
     - 0.0
     - Neutrino density fraction today
   * - 
     - massless_nu
     - real
     - 3.046
     - Effective number of massless neutrinos
   * - 
     - massive_nu
     - int
     - 0
     - Number of massive neutrinos
   * - 
     - sterile_neutrino
     - int
     - 0
     - Number of sterile neutrinos
   * - 
     - delta_neff
     - real
     - 0
     - Contribution to N_eff by sterile neutrino
   * - 
     - sterile_mass_fraction
     - real
     - 
     - Fraction of omega_nu in sterile neutrino
   * - 
     - yhe
     - real
     - 0.24
     - Helium fraction
   * - 
     - w
     - real
     - -1.0
     - Equation of state of dark energy w(z=0)
   * - 
     - wa
     - real
     - 0.0
     - Equation of state parameter in w(z) = w_0 + w_a z / (1+z)
   * - 
     - cs2_de
     - real
     - 1.0
     - Dark energy sound speed/c


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - post_friedmann_parameters
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - Wavenumber k samples in Mpc/h.
   * - 
     - D
     - real 2d
     - D(k,z) modification to first perturbed Einstein equation
   * - 
     - Q
     - real 2d
     - Q(k,z) modification to second perturbed Einstein equation
   * - cosmological_parameters
     - sigma_8
     - real
     - Amplitude of linear matter power at 8/h Mpc at z=0.  Only calculated if mode=all
   * - distances
     - nz
     - int
     - Number of z samples
   * - 
     - z
     - real 1d
     - Redshifts of samples
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
     - rho
     - real 1d
     - Matter density, in kg/m^3  Only if mode=all
   * - 
     - age
     - real
     - Age of universe in GYr
   * - 
     - zdrag
     - real
     - Redshift where baryons no longer dragged by photons. Only if mode!=background
   * - 
     - rs_zdrag
     - real
     - Sound horizon size at zdrag. Only if mode!=background
   * - 
     - zstar
     - real
     - Redshift of unity optical depth.  Only if mode!=background
   * - 
     - theta
     - real
     - Angular size of sound horizon at zstar. Only if mode!=background
   * - 
     - chistar
     - real
     - Comoving distance to zstar. Only if mode!=background
   * - matter_power_lin
     - z
     - real 1d
     - Redshifts of samples. Only if mode=all
   * - 
     - k_h
     - real 1d
     - K wavenumbers of samples in Mpc/h. Only if mode=all
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3. Only if mode=all
   * - linear_cdm_transfer
     - z
     - real 1d
     - Redshifts of samples. Only if mode=all
   * - 
     - k_h
     - real 1d
     - Wavenumber k of samples in Mpc/h. Only if mode=all
   * - 
     - delta_cdm
     - real 2d
     - Linear CDM transfer function at samples. Only if mode=all
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
     - PhiPhi
     - real 1d
     - Lensing spectrum; note ell scaling: ell * (ell+1) C_ell^PhiPhi. Only if mode=cmb or all


