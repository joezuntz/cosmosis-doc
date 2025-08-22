FrankenEmu
================================================

Emulate N-body simulations to compute nonlinear matter power

+-------------+------------------------------------------------------------+
| File        | structure/FrankenEmu/interface.so                          |
+-------------+------------------------------------------------------------+
| Attribution | Suman Bhattacharya                                         |
+-------------+------------------------------------------------------------+
|             | Salman Habib                                               |
+-------------+------------------------------------------------------------+
|             | Katrin Heitmann                                            |
+-------------+------------------------------------------------------------+
|             | David Higdon                                               |
+-------------+------------------------------------------------------------+
|             | Juliana Kwan                                               |
+-------------+------------------------------------------------------------+
|             | Earl Lawrence                                              |
+-------------+------------------------------------------------------------+
|             | Christian Wagner                                           |
+-------------+------------------------------------------------------------+
|             | Brian Williams                                             |
+-------------+------------------------------------------------------------+
|             | Martin White                                               |
+-------------+------------------------------------------------------------+
| URL         | http://www.hep.anl.gov/cosmology/CosmicEmu/emu.html        |
+-------------+------------------------------------------------------------+
| Citations   | The Coyote Universe Extended, arXiv:1304.7849              |
+-------------+------------------------------------------------------------+
|             | Coyote Universe I: ApJ 715, 104 (2010), arXiv:0812.1052    |
+-------------+------------------------------------------------------------+
|             | Coyote Universe II: ApJ 705, 156 (2009), arXiv:0902.0429   |
+-------------+------------------------------------------------------------+
|             | Coyote Universe III: ApJ 713, 1322 (2010), arXiv:0912.4490 |
+-------------+------------------------------------------------------------+


FrankenEmu is an emulator designed to interpolate among a collection
of numerical N-body simulations called the Coyote Universe.

It uses a Gaussian Process interpolation between a set of simulations
arranged in a Latin Hypercube in parameter space.

Each simulation yields a non-linear matter power spectrum P(k,z), and
the interpolation is between these spectra, so the output should be a
reasonable (1% accuracy) value of P(k,z) for the given parameters.

The simulations and the whole process are explained in detail in the papers
above.



Assumptions
-----------

 - LCDM in the form of the Coyote Universe simulations



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - dz
     - real
     - 0.01
     - Spacing in redshift of output
   * - nz
     - int
     - 300
     - Number of redshift samples.  Need nz*dz<=4.0
   * - do_distances
     - bool
     - True
     - Whether to also calculate cosmological distances


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
     - ombh2
     - real
     - 
     - Baryon content
   * - 
     - ommh2
     - real
     - 
     - Matter content
   * - 
     - w
     - real
     - 
     - Dark energy EoS.
   * - 
     - h0
     - real
     - 
     - Hubble/100km/s/Mpc
   * - 
     - n_s
     - real
     - 
     - Scalar spectral index
   * - 
     - sigma_8
     - real
     - 
     - Matter power amplitude


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
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - K wavenumbers of samples in Mpc/h
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3
   * - distances
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - a
     - real 1d
     - Scale factor of samples
   * - 
     - d_a
     - real 1d
     - Angular diameter distance in Mpc
   * - 
     - d_m
     - real 1d
     - Co-moving distance in Mpc
   * - 
     - h
     - real 1d
     - Hubble parameter with in units of c/Mpc


