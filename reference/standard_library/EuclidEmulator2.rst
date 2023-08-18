EuclidEmulator2
================================================

Emulate the boost factors that convert the linear to non-linear power spectrum, including baryon corrections

+-------------+----------------------------------------------------------+
| File        | structure/EuclidEmulator2/euclid_emaulator2_interface.py |
+-------------+----------------------------------------------------------+
| Attribution | M. Knabenhans (library)                                  |
+-------------+----------------------------------------------------------+
|             | Pedro Carrilho (library)                                 |
+-------------+----------------------------------------------------------+
|             | Joe Zuntz (interface)                                    |
+-------------+----------------------------------------------------------+
| URL         | https://github.com/miknab/EuclidEmulator2                |
+-------------+----------------------------------------------------------+
| Citations   | MNRAS, 505, 2, 2840–2869                                 |
+-------------+----------------------------------------------------------+

Emulators like EE2 generate an approximation to the non-linear matter power spectrum
by scaling the linear matter power spectrum by a boost factor. This boost factor is
a function of redshift and wavenumber. 

The boost factor is calculated from a set of
simulations, and the emulator interpolates between these simulations to generate the
boost factor for any redshift and wavenumber.

The accuracy of the emulator is limited by the accuracy of the simulations.


Assumptions
-----------

 - z range 0-10
 - 8.73 x 10-3 h / Mpc ≤ k ≤ 9.41 h / Mpc
 - Simulation suite that went into the emulation



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - input_section
     - str
     - matter_power_lin
     - Section to use for the input linear matter power spectrum
   * - output_section
     - str
     - matter_power_nl
     - Section to use for the output non-linear matter power spectrum


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
     - A_s
     - real
     - 
     - Amplitude of the primordial power spectrum
   * - 
     - n_s
     - real
     - 
     - Spectral index of the primordial power spectrum
   * - 
     - Omega_b
     - real
     - 
     - Baryon density parameter
   * - 
     - Omega_m
     - real
     - 
     - Matter density parameter
   * - 
     - h0
     - real
     - 
     - Hubble parameter / 100 km/s/Mpc
   * - 
     - mnu
     - real
     - 
     - Sum of neutrino masses in eV
   * - 
     - w
     - real
     - 
     - Dark energy equation of state parameter
   * - 
     - wa
     - real
     - 
     - Dark energy equation of state evoluation parameter
   * - input_section
     - k_h
     - real
     - 
     - Wavenumber in h/Mpc
   * - 
     - z
     - real
     - 
     - Redshift
   * - 
     - P_k
     - real
     - 
     - Linear matter power spectrum


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - output_section
     - k_h
     - real
     - Wavenumber in h/Mpc
   * - 
     - z
     - real
     - Redshift
   * - 
     - P_k
     - real
     - Non-Linear matter power spectrum


