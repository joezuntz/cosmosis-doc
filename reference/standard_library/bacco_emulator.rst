bacco_emulator
================================================

Emulate the non-linear, baryonified, matter power spectrum

+-------------+------------------------------------------------+
| File        | structure/baccoemu/baccoemu_interface.py       |
+-------------+------------------------------------------------+
| Attribution | Giovanni Aricò                                 |
+-------------+------------------------------------------------+
|             | Raul E. Angulo                                 |
+-------------+------------------------------------------------+
|             | Sergio Contreras                               |
+-------------+------------------------------------------------+
|             | Lurdes Ondaro-Mallea                           |
+-------------+------------------------------------------------+
|             | Marcos Pellejero-Ibañez                        |
+-------------+------------------------------------------------+
|             | Matteo Zennaro                                 |
+-------------+------------------------------------------------+
|             | Jens Stücker                                   |
+-------------+------------------------------------------------+
|             | Simon Samuroff                                 |
+-------------+------------------------------------------------+
| URL         | https://bitbucket.org/rangulo/baccoemu         |
+-------------+------------------------------------------------+
| Citations   | https://doi.org/10.1093/mnras/stab1911         |
+-------------+------------------------------------------------+
|             | https://doi.org/10.1093/mnras/stab2018         |
+-------------+------------------------------------------------+
|             | https://doi.org/10.12688/openreseurope.14310.2 |
+-------------+------------------------------------------------+

Baccoemu is a collection of cosmological neural-network emulators for large-scale structure statistics
in a wide cosmological parameter space, including dynamical dark energy and massive neutrinos. 
These emulators were developed as part of the Bacco project.

We imported the Bacco Emulator code into this directory because the PyPI version of the code is not recent,
and it has some dependencies that we would like to install from conda-forge rather than PyPI (tensorflow).
We have to make one change to it to make it work on python 3.8 and 3.9 - replacing the progressbar2
library with TQDM. A patch file with this change is included.

The license for this package says copyright belongs to the python packaging authority, but that seems unlikely.


Assumptions
-----------

 - Neural network emulation of NL baryonic power effcts
 - w0waCDM cosmology



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - mode
     - str
     - pk_nl_only
     - What to emulate; the NL DM-only power, the baryonic boost, or both. Choose from 'nonlinear', 'baryons', 'nonlinear+baryons'. If 'baryons' is chosen then the NL power is read from the block (e.g. from camb). Otherwise the NL power is emulated.


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
   * - matter_power_nl
     - z
     - real 1d
     - 
     - Redshifts of samples. Only if mode = = "baryons".
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumbers k of samples in Mpc/h. Only if mode = = "baryons".
   * - 
     - p_k
     - real 2d
     - 
     - Linear power spectrum at samples in (Mpc/h)^-3. Only if mode = = "baryons".
   * - cosmological_parameters
     - A_s
     - real
     - 
     - Amplitude of the primordial power spectrum.
   * - 
     - omega_c
     - real
     - 
     - Cold dark matter density parameter
   * - 
     - omega_b
     - real
     - 
     - Baryon density parameter
   * - 
     - n_s
     - real
     - 
     - Primordial power spectrum spectral index.
   * - 
     - h0
     - real
     - 
     - Hubble parameter.
   * - 
     - mnu
     - real
     - 
     - Sum of neutrino masses in eV.
   * - 
     - w0
     - real
     - -1.0
     - Dark energy equation of state parameter at z=0
   * - 
     - wa
     - real
     - 0.0
     - Dark energy equation of state rate of change with scale factor
   * - baryon_parameters
     - M_c
     - real
     - 
     - Gas mass parameter; log scale in Msun/h. Range 9.0 to 15.0
   * - 
     - eta
     - real
     - 
     - Ejected gas density exponential cut-off scale, in range -0.698 to 0.698
   * - 
     - beta
     - real
     - 
     - Gas mass index parameter; log scale, in range -1.0 to 0.698
   * - 
     - M1_z0_cen
     - real
     - 
     - characteristic halo mass scale for central galaxies, in range 9.0 to 13.0; log scale in Msun/h
   * - 
     - theta_out
     - real
     - 
     - Scaling of r200 to give outer power-law profile scale of hot gas radius. Range 0.0 to 0.477
   * - 
     - theta_inn
     - real
     - 
     - Scaling of r200 to give inner power-law profile scale of hot gas radius. Range -2.0 to -0.522
   * - 
     - M_inn
     - real
     - 
     - Characteristic mass of inner hot gas; log scale in Msun/h. Range 9.0 to 13.5.


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
     - Non-linear power spectrum at samples in (Mpc/h)^-3, potentially including baryon corrections.


