apply_astrophysical_biases
================================================

Apply various astrophysical biases to the matter power spectrum P(k,z)

+-------------+-----------------------------------------------+
| File        | shear/apply_astrophysical_biases/interface.so |
+-------------+-----------------------------------------------+
| Attribution | CosmoSIS team                                 |
+-------------+-----------------------------------------------+
|             | Simon Samuroff                                |
+-------------+-----------------------------------------------+
| URL         |                                               |
+-------------+-----------------------------------------------+


Measurement of the matter power spectrum from real data relies on the visible positions and shapes of galaxies.
Real galaxies offer a window onto the underlying mass distribution but an imperfect one. Due to a variety of 
astrophysical processes in their formation and interaction history, the visible mass of galaxies is offset from
the dark matter. Additionally, the precise relationship between their shapes and the total mass is dependent on 
the details of how galaxies obtain intrinsic ellipticities. One can parameterise ignorance of these processes 
using a series of scale and time dependent biases, which map the matter power spectrum onto the observable
fields.   



Assumptions
-----------

None



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - intrinsic_alignments
     - bool
     - True
     - Whether to calculate intrisic alignment spectra
   * - galaxy_bias
     - bool
     - True
     - Whether to calculate galaxy position spectra.
   * - verbosity
     - int
     - 1
     - Parameter setting the level of terminal output


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
     - z
     - real 1d
     - 
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P(k,z) samples in Mpc/h
   * - 
     - P_k
     - real 2d
     - 
     - Non-linear matter power spectrum at samples in (Mpc/h)^{-3}
   * - intrinsic_alignment_parameters
     - z
     - real 1d
     - 
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P(k,z) samples in Mpc/h
   * - 
     - b_I
     - real 2d
     - 
     - Intrinsic alignment bias on grid
   * - 
     - r_I
     - real 2d
     - 
     - Stochastic intrinsic alignment bias
   * - bias_field
     - z
     - real 1d
     - 
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P(k,z) samples in Mpc/h
   * - 
     - b_g
     - real 2d
     - 
     - Galaxy bias on grid
   * - 
     - r_g
     - real 2d
     - 
     - Stochastic galaxy bias on grid


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - ia_spectrum_ii
     - z
     - real 1d
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - Wavenumber k values of P(k,z) samples in Mpc/h
   * - 
     - P_II
     - real 2d
     - Intrinsic-intrinsic shape spectrum at samples in (Mpc/h)^{-3}
   * - ia_spectrum_gi
     - z
     - real 1d
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - k values of P(k,z) samples in Mpc/h
   * - 
     - P_GI
     - real 2d
     - Mass-intrinsic shape spectrum at samples in (Mpc/h)^{-3}
   * - matter_power_gal_mass
     - z
     - real 1d
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - Wavenumber k values of P(k,z) samples in Mpc/h
   * - 
     - P_k
     - real 2d
     - ; galaxy position-mass spectrum at samples in (Mpc/h)^{-3}
   * - matter_power_gal
     - z
     - real 1d
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - Wavenumber k values of P(k,z) samples in Mpc/h
   * - 
     - P_k
     - real 2d
     - Galaxy position-position spectrum at samples in (Mpc/h)^{-3}
   * - matter_power_gal_intrinsic
     - z
     - real 1d
     - Redshift values of P(k,z) samples
   * - 
     - k_h
     - real 1d
     - Wavenumber k values of P(k,z) samples in Mpc/h
   * - 
     - P_k
     - real 2d
     - Fourier space correlation between galaxy position and intrinsic shape in (Mpc/h)^{-3}


