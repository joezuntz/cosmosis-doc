no_bias
================================================

Generate galaxy power P(k) as though galaxies were unbiased DM tracers

+-------------+-------------------------+
| File        | bias/no_bias/no_bias.py |
+-------------+-------------------------+
| Attribution | CosmoSIS Team           |
+-------------+-------------------------+
| URL         |                         |
+-------------+-------------------------+

Galaxy bias relates the distribution of galaxies to the underlying (dark) matter
field whose skeleton they trace.

The matter power spectrum of galaxies is related to that of matter by a bias:

P_gal(k,z) = b(k,z,...) P_m(k,z)

where the most general bias is a function of wavenumber k, redshift z, galaxy type,
and a whole host of other values.  Realistic bias models can be complicated; the purpose
of this module is to act as a placeholder, usually when testing pipelines or forecasting.

In this module, b=1.  It generates the galaxy power and
matter-galaxy cross-power from the non-linear power spectrum, just by copying them.

This can be useful if you plan to apply a more complicated bias model to calculated
observables later, for example.

Optionally, if it finds you have generated the matter-intrinsic alignment cross-power,
it will calculate the galaxy-intrinsic cross power from it.



Assumptions
-----------

 - Unit galaxy bias; at all scales and redshifts galaxies perfectly trace dark matter



Setup Parameters
----------------

None


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
     - k_h
     - real 1d
     - 
     - Wavenumber in h/Mpc of NL matter power
   * - 
     - z
     - real 1d
     - 
     - Redshift of NL matter power
   * - 
     - P_k
     - real 2d
     - 
     - Nonlinear matter power
   * - matter_intrinsic_power
     - k_h
     - real 1d
     - 
     - Wavenumber in h/Mpc of matter-intrinsic power (optional)
   * - 
     - z
     - real 1d
     - 
     - Optional, redshift
   * - 
     - P_k
     - real 2d
     - 
     - Optional, nonlinear matter power


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - galaxy_power
     - k_h
     - real 1d
     - Wavenumber in h/Mpc
   * - 
     - z
     - real 1d
     - Redshift
   * - 
     - P_k
     - real 2d
     - Galaxy power
   * - matter_galaxy_power
     - k_h
     - real 1d
     - Wavenumber in h/Mpc
   * - 
     - z
     - real 1d
     - Redshift
   * - 
     - P_k
     - real 2d
     - Matter-galaxy cross power
   * - galaxy_intrinsic_power
     - k_h
     - real 1d
     - Only if matter_intrinsic_power found, wavenumber in h/Mpc
   * - 
     - z
     - real 1d
     - Only if matter_intrinsic_power found, optional, redshift
   * - 
     - P_k
     - real 2d
     - Only if matter_intrinsic_power found, optional, nonlinear matter power


