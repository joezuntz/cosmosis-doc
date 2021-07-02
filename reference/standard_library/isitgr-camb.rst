isitgr-camb
================================================

Modified version of CAMB to implement phenomenological modified gravity models

.. list-table::
    
   * - File
     - boltzmann/isitgr/camb.so
   * - Attribution
     - Jason Dossett
   * -
     - Mustapha Ishak
   * -
     - Jacob Moldenhauer
   * -
     - Antony Lewis
   * -
     - Anthony Challinor
   * - URL
     - http://www.utdallas.edu/~jdossett/isitgr
   * - Citation
     - http://arxiv.org/abs/1109.4583
   * -
     - Phys. Rev. D86, 103008, 2012
   * - Rules
     - Since isitgr is derived from CAMB, please abide by the conditions set out in the CAMB license if you use this module http://camb.info/CAMBsubmit.html


ISiTGR, the Integrated Software in Testing General Relativity, is
a set of modifications to CAMB and CosmoMC which implement a set of modified
gravity models where the perturbed metric quantities phi and psi are
modified by some fitting functions as a general, phenomenological model
of some unknown new physics.

There are a number of possible ways to describe such functions; this 
code uses the variables in equations 8 and 10 of http://arxiv.org/pdf/1109.4583v3.pdf
and the functional form ansatz in equation 11:

For X as Q, D, or R we use:
    X(k,a) = [X_0 exp(-k/k_c) + X_inf (1-exp(-k/k_c)) - 1] a^s + 1

Most of the parameters in this code are the same as those in camb; see
the camb module information for more details.

ISiTGR is pronounced "Is it GR?" not "Easy, Tiger".

Anthony Lewis has kindly given permission for CAMB to be packaged
with CosmoSIS.

The CosmoSIS team packaged this module into cosmosis form so any issues
running it here please ask us first.


Assumptions
-----------

 - The modified gravity phenomenological model described in the referenced papers



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - scale_dependent
     - bool
     - 
     - Use scale dependent parameterized functions.  If False, k_c is ignored.
   * - use_r_function
     - bool
     - 
     - Give R scale and time dependence instead of Q.
   * - mode
     - str
     - 
     - Choose from Background, thermal, cmb, or all.
In background mode only the expansion history is calculated. In thermal mode the recombination history is computed and rs_zdrag and related quantities also. In cmb mode the CMB power spectra are also calculated. In all mode the matter power spectrum at low redshift and sigma8 are also calculated.
   * - lmax
     - int
     - 
     - Only if mode!=background, default 1200 - the max ell to use for cmb calculation
   * - feedback
     - int
     - 
     - Amount of output to print.  0 for no feedback.  1 for basic, 2 for extended, maybe higher?
   * - use_tabulated_w
     - bool
     - False
     - Set to true to load w(z) from previous module
   * - k_eta_max_scalar
     - int
     - 
     - Maximum value of (k eta) to evolve for scalars. (default 2*lmax)
   * - do_tensors
     - ???
     - False
     - Include tensor modes
   * - zmin
     - ???
     - 0
     - Min value to save P(k,z)
   * - zmax
     - ???
     - 4
     - Max value to save P(k,z)
   * - nz
     - ???
     - 
     - Number of z values to save P(k,z) (default 401, so that dz=0.01)
   * - do_nonlinear
     - ???
     - False
     - Apply non-linear halofit corrections to matter-power.  Relevant only for lensing right now
   * - do_lensing
     - ???
     - False
     - Include lensing of CMB, and save C_ell phi-phi
   * - high_ell_template
     - ???
     - 
     - Required for lensing - set to the file included in the camb dir (no default)


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
     - d_0
     - real
     - 
     - Poisson equation modification at k<<k_c and z=0
   * - 
     - d_inf
     - real
     - 
     - Poisson equation modification at k>>k_c and z=0
   * - 
     - q_0
     - real
     - 
     - Gravitational slip modification at k<<k_c and z=0
   * - 
     - q_inf
     - real
     - 
     - Gravitational slip modification at k>>k_c and z=0
   * - 
     - s
     - real
     - 
     - Index of variation of effects with scale factor
   * - 
     - k_c
     - real
     - 
     - Transition scale between small and large k.
   * - cosmological_parameters
     - omega_b
     - real
     - 
     - Baryon density fraction today
   * - 
     - omega_c
     - real
     - 
     - Cdm density fraction today
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
     - W(z=0) equation of state of dark energy
   * - 
     - wa
     - real
     - 0.0
     - Equation of state parameter w(z) = w_0 + w_a z / (1+z)
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

   * - modified_gravity
     - v_0
     - real
     - 2*d_0 - q_0
   * - 
     - v_inf
     - real
     - 2*d_inf - q_inf
   * - 
     - r_0
     - real
     - 2*d_0/q_0 - 1
   * - 
     - r_inf
     - real
     - 2*d_inf/q_inf - 1
   * - cosmological_parameters
     - sigma_8
     - real
     - Only of mode=all. Amplitude of linear matter power at 8/h Mpc at z=0.
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
     - age
     - real
     - Age of universe in GYr
   * - matter_power_lin
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - K wavenumbers of samples in Mpc/h
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3
   * - linear_cdm_transfer
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - K wavenumbers of samples in Mpc/h
   * - 
     - delta_cdm
     - real 2d
     - Linear CDM transfer function at samples
   * - cmb_cl
     - ell
     - int 1d
     - Angular frequencies
   * - 
     - tt
     - real 1d
     - Ell * (ell+1) C_ell^TT / 2 pi in mu K^2
   * - 
     - ee
     - real 1d
     - Ell * (ell+1) C_ell^EE / 2 pi in mu K^2
   * - 
     - bb
     - real 1d
     - Ell * (ell+1) C_ell^BB / 2 pi in mu K^2
   * - 
     - te
     - real 1d
     - Ell * (ell+1) C_ell^TE / 2 pi in mu K^2
   * - 
     - PhiPhi
     - real 1d
     - Lensing spectrum; note ell scaling: ell * (ell+1) C_ell^PhiPhi


