pyhmcode
================================================

Compute the non-linear matter power spectrum with pyhalofit

+-------------+--------------------------------------------------------------------+
| File        | structure/pyhmcode/hmcode_interface.py                             |
+-------------+--------------------------------------------------------------------+
| Attribution | Xiangchong Li (interface)                                          |
+-------------+--------------------------------------------------------------------+
|             | Tilman Troester (pyhmcode)                                         |
+-------------+--------------------------------------------------------------------+
|             | Alexander Mead (HMCode)                                            |
+-------------+--------------------------------------------------------------------+
| URL         | https://github.com/tilmantroester/pyhmcode                         |
+-------------+--------------------------------------------------------------------+
| Citations   | HMCode2015: Mead et al. (2015; https://arxiv.org/abs/1505.07833)   |
+-------------+--------------------------------------------------------------------+
|             | HMCode2016: Mead et al. (2016; https://arxiv.org/abs/1602.02154)   |
+-------------+--------------------------------------------------------------------+
|             | HMCode2020: Mead et al. (2021; https://arxiv.org/abs/2009.01858)   |
+-------------+--------------------------------------------------------------------+
|             | HMx: Mead, Tröster et al. (2020; https://arxiv.org/abs/2005.00009) |
+-------------+--------------------------------------------------------------------+

HMCode uses a halo model approach, in which dark matter is modelled
as a population of bound halos and observable quantities are related
to the properties of these halos and the tracer distribution within them.

There is a version of HMCode included in CAMB, which you can use through
cosmosis - see the camb module non-linear options. There is also an independent
HMCode, and a set of python wrappings, pyhmcode.

This is not the official pyhmcode CosmoSIS interface, but one made for the
HSC likelihood in order to match the CAMB settings as closely as possible.


Assumptions
-----------

 - The HMCode family of models for the non-linear matter power spectrum



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
     - Whether to print extra output
   * - version
     - str
     - HMcode2020
     - Which version of HMCode to use. Options are HMcode2016, HMcode2016_1par, HMcode2020, HMcode2020_feedback


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - halo_model_parameters
     - A_bary
     - real
     - 
     - Halo concentration parameter. Only read if version is HMcode2016 or HMcode2016_1par.
   * - 
     - eta0
     - real
     - 
     - Halo profile scaling parameter. Only read if version is HMcode2016. Set to 0.98 - 0.12 * A_bary in the 1par model.
   * - 
     - logT_AGN
     - real
     - 
     - AGN temperature parameter. Only read if version is HMcode2020_feedback..
   * - matter_power_lin
     - z
     - real 1d
     - 
     - Redshifts of samples.
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
   * - 
     - omega_m
     - real
     - 
     - Matter density fraction of critical
   * - 
     - omega_b
     - real
     - 
     - Baryon density fraction of critical
   * - 
     - omega_lambda
     - real
     - 
     - Dark energy density fraction of critical
   * - 
     - mnu
     - real
     - 
     - Sum of neutrino masses (in eV)
   * - 
     - sigma_8
     - real
     - 
     - Amplitude of linear matter power at 8/h Mpc at z=0.
   * - 
     - h0
     - real
     - 
     - Dimensionless Hubble h = H_0 / 100 km/s/Mpc
   * - 
     - n_s
     - real
     - 
     - Primordial scalar spectral index


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - matter_power_nl
     - z
     - real 1d
     - Redshifts of samples.
   * - 
     - k_h
     - real 1d
     - Wavenumbers k of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - Non-linear power spectrum at samples in (Mpc/h)^-3.


