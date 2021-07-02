constant_bias
================================================

Apply a galaxy bias constant with k and z.

.. list-table::
    
   * - File
     - bias/constant_bias/constant_bias.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


"Galaxy bias relates the distribution of galaxies to the underlying (dark) matter
field whose skeleton they trace.

The matter power spectrum of galaxies is related to that of matter by a bias:

P_gal(k,z) = b^2(k,z,...) P_m(k,z)

where the most general bias is a function of wavenumber k, redshift z, galaxy type,
and a whole host of other values.  Realistic bias models can be complicated; the purpose
of this module is to act as a placeholder, usually when testing pipelines or forecasting.

In this module, b is just a single constant number.  It generates the galaxy power and
matter-galaxy cross-power from the non-linear power spectrum.

Optionally, if it finds you have generated the matter-intrinsic alignment cross-power,
it will calculate and save the galaxy-intrinsic cross power from it.
"



Assumptions
-----------

 - Galaxy bias constant with k and z



Setup Parameters
----------------

No parameters


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - galaxy_bias
     - b
     - real
     - 
     - Constant galaxy bias value.
   * - matter_power_nl
     - k_h
     - real 1d
     - 
     - Wavenumber samples in h/Mpc for NL power
   * - 
     - z
     - real 1d
     - 
     - Redshift samples for NL power
   * - 
     - P_k
     - real 2d
     - 
     - Nonlinear matter power grid
   * - matter_intrinsic_power
     - k_h
     - real 1d
     - 
     - Optional wavenumber in h/Mpc for matter-intrinsic cross-power
   * - 
     - z
     - real 1d
     - 
     - Optional redshift for matter-intrinsic cross-power
   * - 
     - P_k
     - real 2d
     - 
     - Optional nonlinear matter-intrinsic cross-power


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
     - Wavenumber in h/Mpc of galaxy density power
   * - 
     - z
     - real 1d
     - Redshift of galaxy density power
   * - 
     - P_k
     - real 2d
     - Galaxy density power spectrum
   * - matter_galaxy_power
     - k_h
     - real 1d
     - Wavenumber in h/Mpc of matter-galaxy cross-power
   * - 
     - z
     - real 1d
     - Redshift of matter-galaxy cross-power
   * - 
     - P_k
     - real 2d
     - Matter-galaxy cross power
   * - galaxy_intrinsic_power
     - k_h
     - real 1d
     - Wavenumber in h/Mpc of matter-intrinsic power (if computed)
   * - 
     - z
     - real 1d
     - Redshift of matter-intrinsic power (if computed)
   * - 
     - P_k
     - real 2d
     - Non-linear cross galaxy-intrinsic power spectrum (if computed)


