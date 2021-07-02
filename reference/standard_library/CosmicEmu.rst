CosmicEmu
================================================

Emulate N-body simulations to compute nonlinear matter power

.. list-table::
    
   * - File
     - structure/cosmic_emu/interface.so
   * - Attribution
     - Katrin Heitmann
   * -
     - Derek Bingham
   * -
     - Earl Lawrence
   * -
     - Steven Bergner
   * -
     - Salman Habib
   * -
     - David Higdon
   * -
     - Adrian Pope
   * -
     - Rahul Biswas
   * -
     - Hal Finkel
   * -
     - Nicholas Frontiere
   * -
     - Suman Bhattacharya
   * - URL
     - http://www.hep.anl.gov/cosmology/CosmicEmu/emu.html
   * - Citation
     - The Mira-Titan Universe: Precision Predictions for Dark Energy Surveys, ApJ, 820, 2 (2016), arXiv:1508.02654
   * - Rules
     -



CosmicEmu is an emulator designed to interpolate among a collection
of numerical N-body simulations called Mira-Titan.

It uses a Gaussian Process interpolation between a set of simulations
arranged in a lattice in parameter space.

Each simulation yields a non-linear matter power spectrum P(k,z), and
the interpolation is between these spectra, so the output should be a
reasonable (1% accuracy) value of P(k,z) for the given parameters.

The simulations and the whole process are explained in detail in the paper
above.



Assumptions
-----------

 - w0waCDM and the Mira-Titan simulation assumptions



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
     - 2.0
     - Maximum output redshift
   * - nz
     - int
     - 50
     - Number of redshift samples.  Note that the code will be interpolating between sample values


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
     - Physical baryon content
   * - 
     - ommh2
     - real
     - 
     - Physical matter content
   * - 
     - w
     - real
     - -1.0
     - Dark energy equation of state
   * - 
     - wa
     - real
     - 0.0
     - Dark energy equation of state derivative
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
     - Power spectrum normalization


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
     - Wavenumbers k of samples in Mpc/h
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3


