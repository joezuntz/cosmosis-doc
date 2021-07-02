linear_alignments
================================================

Compute the terms P_II and P_GI which go into intrinsic aligment calculations

.. list-table::
    
   * - File
     - intrinsic_alignments/la_model/linear_alignments_interface.py
   * - Attribution
     - CosmoSIS team
   * -
     - Donnacha Kirk
   * - URL
     - 
   * - Citation
     - MNRAS 424 3 1647 (2012)
   * -
     - New J Phys 9 12 444 (2007)
   * - Rules
     -


"
Intrinsic alignment refers to the extent to which galaxies align in the sky,
before any alignment induced by gravitational lensing.  It is a systematic
error contribution to cosmic shear measurements and is predicted here in the form
of two power spectra, one for the alignments, P_II, and one for the alignment-shear
correlations, P_GI.

In the original Linear Alignment model it was assumed that alignments among
galaxies were laid down early in the evolution of structure, and then (on average)
did not vary since.  The amount of alignment on a given scale was then related
to the linear power spectrum at that scale.

The P_II and P_GI power is described in terms of a power spectrum, integrated over
with a Limber integral in a similar way to the shear power spectrum. This code
does not do that integral, it just calculates P_II and P_GI.

A number of variations to the LA model have been discussed since, and this module
implements three of them.  The history is a little convoluted as an error was found
in early work missing a factor of (1+z), so one of our models is a corrected version
of one of the other ones.  Our models are:
    Bridle & King
    Bridle & King (corrected)
    Kirk, Rassat, Host, Bridle

See these papers for details of these models.

"



Assumptions
-----------

 - Uses one of three models for how matter power is turned into intrinsic alignments



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - method
     - str
     - 
     - Which model to run. Choice of 'bk', 'bk_corrected', 'krhb',
   * - name
     - str
     - 
     - If set, save the outputs to sections with the name as a suffix, e.g intrinsic_power_NAME
   * - grid_mode
     - bool
     - False
     - Whether to save the fields b(k,z) and r(k,z) as described in Bridle & King instead of applying directly to P(k)
   * - do_galaxy_intrinsic
     - bool
     - False
     - Compute the matter-IA cross correlation.


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
     - Density fraction of all matter.
   * - intrinsic_alignment_parameters
     - A
     - real
     - 
     - Single parameter scaling power spectra
   * - matter_power_nl
     - z
     - real 1d
     - 
     - redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - k values of P(k,z) samples in units of Mpc/h
   * - 
     - P_k
     - real 2d
     - 
     - non-linear matter power spectrum at samples in (Mpc/h)^{-3}
   * - matter_power_lin
     - z
     - real 1d
     - 
     - redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - k values of P(k,z) samples in units of Mpc/h
   * - 
     - P_k
     - real 2d
     - 
     - linear matter power spectrum at samples in (Mpc/h)^{-3}
   * - matter_galaxy_power
     - z
     - real 1d
     - 
     - redshift values of P(k,z) samples (if do_galaxy_intrinsic)
   * - 
     - k_h
     - real 1d
     - 
     - k values of P(k,z) samples in units of Mpc/h (if do_galaxy_intrinsic)
   * - 
     - P_k
     - real 2d
     - 
     - Nonlinear matter-galaxy cross power spectrum at samples in (Mpc/h)^{-3} (if do_galaxy_intrinsic)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - intrinsic_power
     - z
     - real 1d
     - Redshift values of P(k,z) samples (if grid_mode=F, the default)
   * - 
     - k_h
     - real 1d
     - Wavenumber k values of P(k,z) samples in units of Mpc/h (if grid_mode=F, the default)
   * - 
     - P_k
     - real 2d
     - Spectrum of intrinsic-intrinsic power at samples in (Mpc/h)^{-3} (if grid_mode=F, the default)
   * - matter_intrinsic_power
     - z
     - real 1d
     - Redshift values of P(k,z) samples (if grid_mode=F, the default)
   * - 
     - k_h
     - real 1d
     - ; k values of P(k,z) samples in units of Mpc/h (if grid_mode=F, the default)
   * - 
     - P_k
     - real 2d
     - Spectrum of shear-intrinsic power at samples in (Mpc/h)^{-3} (if grid_mode=F, the default)
   * - intrinsic_alignment_parameters
     - z
     - real 1d
     - Redshift values ofsamples (if grid_mode=F, the default)
   * - 
     - k_h
     - real 1d
     - Wavenumber k values of samples in units of Mpc/h (if grid_mode=F, the default)
   * - 
     - b_I
     - real 2d
     - The 'bias' term described in eqn 27 of Kirk, Rassat, Host Bridle. (if grid_mode=T)
   * - 
     - r_I
     - real 2d
     - The cross-correlation 'bias' term described in eqn 28 of Kirk, Rassat, Host Bridle. (if grid_mode=T)


