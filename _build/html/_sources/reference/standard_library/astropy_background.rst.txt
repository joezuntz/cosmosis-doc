astropy_background
================================================

Calculate background cosmology using astropy

+-------------+---------------------------------------------------------+
| File        | background/astropy_background/astropy_background.py     |
+-------------+---------------------------------------------------------+
| Attribution | CosmoSIS Team (interface)                               |
+-------------+---------------------------------------------------------+
|             | Astropy Team (library)                                  |
+-------------+---------------------------------------------------------+
| URL         | https://docs.astropy.org/en/stable/cosmology/index.html |
+-------------+---------------------------------------------------------+
| Citations   | The Astropy Collaboration et al 2022 ApJ 935 167        |
+-------------+---------------------------------------------------------+

The astropy cosmology library can compute background evolution distances as a function
of redshift for a range of different cosmologies:

- FlatLambdaCDM
- FlatwCDM
- Flatw0waCDM
- LambdaCDM
- wCDM
- w0waCDM
- w0wzCDM
- w0wzCDM
- wpwaCDM

This module requires the user to choose one of these models and then will read
the appropriate parameters for that model and compute a range of distance measures.


Assumptions
-----------

 - Various depending on model choice



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - zmax
     - real
     - 
     - Maximum redshift to compute distances to
   * - nz
     - real
     - 
     - Number of redshift sample points to compute distances to
   * - model
     - str
     - 
     - Name of the astropy model to use


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
     - hubble
     - real
     - 
     - Hubble parameter today in km/s/Mpc
   * - 
     - omega_m
     - real
     - 
     - Dark matter density fraction today
   * - 
     - omega_lambda
     - real
     - 
     - Dark energy density fraction today. Only for some models.
   * - 
     - w
     - real
     - 
     - Dark energy equation of state today. Only for some models.
   * - 
     - wa
     - real
     - 
     - Dark energy equation of state scale factor derivative. Only for some models.
   * - 
     - wz
     - real
     - 
     - Dark energy equation of state redshift derivative today. Only for some models.
   * - 
     - zp
     - real
     - 
     - Redshift pivot for wpwaCDM model
   * - 
     - wp
     - real
     - 
     - Dark energy equation of state at zp for wpwaCDM model


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - distances
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
     - Co-moving transverse distance in Mpc
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
     - d_v
     - real 1d
     - Comoving volume in Mpc^3
   * - 
     - d_c
     - real 1d
     - Comoving line-of-sight distance in Mpc


