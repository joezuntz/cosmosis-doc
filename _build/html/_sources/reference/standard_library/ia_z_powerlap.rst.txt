ia_z_powerlap
================================================



+-------------+--------------------------------------------------+
| File        | intrinsic_alignments/z_powerlaw/ia_z_powerlaw.py |
+-------------+--------------------------------------------------+
| Attribution | CosmoSIS team                                    |
+-------------+--------------------------------------------------+
|             | Niall Maccrann                                   |
+-------------+--------------------------------------------------+
| URL         |                                                  |
+-------------+--------------------------------------------------+


Basic models of intrinsic alignments assume a specific simple evolution with redshift.
This module takes an existing model of the IA power spectra and modifies them by giving
them additional evolution in z.

Specifically, it takes P_II and P_GI (e.g. as calculated by the la_model module)
and modifies them to:

P_II(k,z) -> (1+z)^alpha P_II(k,z)
P_GI(k,z) -> (1+z)^alpha P_GI(k,z)




Assumptions
-----------

 - Modify the intrinsic alignment power spectra to have a power-law dependence in (1+z)



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - name
     - str
     - 
     - A suffix to use for the input/output sections


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - intrinsic_alignment_parameters
     - alpha
     - real
     - 
     - Power law index to apply.
   * - intrinsic_power
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P(k,z) samples in units of Mpc/h
   * - 
     - z
     - real 1d
     - 
     - Redshift values of P(k,z) samples
   * - 
     - P_K
     - real 2d
     - 
     - Spectrum of intrinsic-intrinsic power at samples in (Mpc/h)^{-3}
   * - matter_intrinsic_power
     - k_h
     - real 1d
     - 
     - Wavenumber k values of P(k,z) samples in units of Mpc/h
   * - 
     - z
     - real 1d
     - 
     - Array; redshift values of P(k,z) samples
   * - 
     - P_K
     - real 2d
     - 
     - Spectrum of matter-intrinsic cross-power at samples in (Mpc/h)^{-3}


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - intrinsic_power
     - k_h
     - real 1d
     - Wavenumber k values of P(k,z) samples in units of Mpc/h (unchanged from input)
   * - 
     - z
     - real 1d
     - Redshift values of P(k,z) samples (unchanged from input)
   * - 
     - P_K
     - real 2d
     - ; updated spectrum of intrinsic-intrinsic power at samples in (Mpc/h)^{-3}
   * - matter_intrinsic_power
     - k_h
     - real 1d
     - Wavenumber k values of P(k,z) samples in units of Mpc/h (unchanged from input)
   * - 
     - z
     - real 1d
     - Redshift values of P(k,z) samples (unchanged from input)
   * - 
     - P_K
     - real 2d
     - Updated spectrum of matter-intrinsic cross-power at samples in (Mpc/h)^{-3}


