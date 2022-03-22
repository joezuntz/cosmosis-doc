fast_pt
================================================

Compute various 1-loop perturbation theory quantities

.. list-table::
    
   * - File
     - structure/fast_pt/fast_pt_interface.py
   * - Attribution
     - Niall Maccrann
   * -
     - Jonathan Blazek
   * - URL
     - https://github.com/JoeMcEwen/FAST-PT
   * - Citation
     - https://iopscience.iop.org/article/10.1088/1475-7516/2016/09/015
   * - Rules
     -


The FAST-PT library computes a selection of quantities which are 
integrals over the 3D matter power spectrum, coupled with itself by a
mode-coupling kernel.

This module runs that library to compute various terms that are useful
for either intrinsic alignment calculations for the TATT model, and/or
galaxy bias terms.

This module is not fully documented yet



Assumptions
-----------

 - 1-loop perturbation theory



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - do_dd_spt
     - bool
     - False
     - Compute matter power spectrum terms
   * - do_ia
     - bool
     - False
     - Compute intrinsic alignment TATT terms
   * - do_bias
     - bool
     - False
     - Compute galaxy bias terms
   * - do_rsd
     - bool
     - False
     - Compute redshift space distortion terms
   * - do_ia_tt
     - bool
     - False
     - Compute intrinsic alignment tidal torqing terms
   * - do_ia_ta
     - bool
     - False
     - Compute intrinsic alignment tidal alignment terms
   * - do_ia_mix
     - bool
     - False
     - Compute intrinsic alignment mixed terms
   * - bias_section
     - str
     - bias
     - Name of block section to load bias parameter from
   * - output_nl_grid
     - bool
     - False
     - Whether to save a grid of nonlinear matter power
   * - only_terms
     - bool
     - False
     - Whether to save only PT terms not actual spectra
   * - always_init
     - bool
     - False
     - Re-initialize FAST-PT at every parameter space point
   * - k_res_fac
     - real
     - 4.0
     - Factor to increase k-space resolution
   * - low_extrap
     - real
     - -5.0
     - Log10 value of k down to which to extrapolate
   * - high_extrap
     - real
     - 3.0
     - Log10 value of k up to which to extrapolate
   * - C_window
     - real
     - 0.75
     - Taper fourier coefficients at |m| > C_window * N/2
   * - n_pad_fac
     - real
     - 1.0
     - Number of zeros to pad the FT with
   * - verbose
     - bool
     - False
     - Print extra output


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - matter_power_lin
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumbers k of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - 
     - Linear power spectrum at samples in (Mpc/h)^-3.
   * - matter_power_nl
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumbers k of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - 
     - Non-linear power spectrum at samples in (Mpc/h)^-3.
   * - bias_section
     - b_1
     - real
     - 
     - Linear bias term
   * - 
     - b_2
     - real
     - 
     - Quadratic bias term
   * - 
     - b_s
     - real
     - 
     - s bias term
   * - 
     - b1_alpha
     - real
     - 0.0
     - Power law index for b1
   * - 
     - b2_alpha
     - real
     - 0.0
     - Power law index for b2
   * - 
     - bs_alpha
     - real
     - 0.0
     - Power law index for bs
   * - 
     - b1_z0
     - real
     - 0.0
     - Power law baseline for b1
   * - 
     - b2_z0
     - real
     - 0.0
     - Power law baseline for b2
   * - 
     - bs_z0
     - real
     - 0.0
     - Power law baseline for bs


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - fastpt
     - z
     - real 1d
     - Redshift values at which terms are calculated
   * - 
     - k_h
     - real 1d
     - Wavenumber values at which linear terms are calculated
   * - 
     - k_h_nl
     - real 1d
     - Wavenumber values at which non-linear terms are calculated
   * - 
     - Plin
     - real 2d
     - Linear matter power from FAST-PT
   * - 
     - Pd1d2
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pd2d2
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pd1s2
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pd2s2
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Ps2s2
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pgg
     - real 2d
     - Galaxy density power spectrum
   * - 
     - Pggsub
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pmg
     - real 2d
     - Matter-galaxy cross-power from
   * - 
     - sig4kz
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - one_loopkz
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - P1Lkz
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pkz2
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pd1d2_o
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pd2d2_o
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pd1s2_o
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pd2s2_o
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Ps2s2_o
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pgg_o
     - real 2d
     - Galaxy density power spectrum on the nonlinear grid
   * - 
     - Pggsub_o
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - Pmg_o
     - real 2d
     - Matter-Galaxy power spectrum on the nonlinear grid
   * - 
     - sig4kz_o
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - P_tt_EE
     - real 2d
     - Tidal torquing E-mode power spectrum
   * - 
     - P_tt_BB
     - real 2d
     - Tidal torquing B-mode power spectrum
   * - 
     - P_ta_dE1
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - P_ta_dE2
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - P_ta_EE
     - real 2d
     - Tidal-alignment E-mode power spectrum
   * - 
     - P_ta_BB
     - real 2d
     - Tidal-alignment B-mode power spectrum
   * - 
     - P_mix_A
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - P_mix_B
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - P_mix_D_EE
     - real 2d
     - Perturbative quantity not yet documented
   * - 
     - P_mix_D_BB
     - real 2d
     - Perturbative quantity not yet documented
   * - galaxy_power
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - Wavenumbers k of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - Matter density - Galaxy density cross power spectrum
   * - galaxy_power_sublowk
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - Wavenumbers k of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - Perturbative quantity not yet documented


