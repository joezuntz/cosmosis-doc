sigma8_rescale
================================================

Rescale structure measures to use a specified sigma_8

.. list-table::
    
   * - File
     - utility/sample_sigma8/sigma8_rescale.py
   * - Attribution
     - Susana Fernandez
   * -
     - Jack Elvin-Poole
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


Boltzmann codes like CAMB and CLASS typically take a primordial power spectrum
amplitude A_s as an input parameter defining the amplitude of cosmic structure
fluctutations.

Late-time data sets more naturally measure a late-time amplitude, and the measure
sigma_8 is usually instead for these data.  If all other cosmological parameters
are fixed A_s ~ sigma_8^2, but when other parameters can vary they are not
perfectly equivalent.

This module enables you to sample over sigma_8 while still passing A_s into a
Boltzmann code.  It does this by using an input value sigma8_input, which can
be sampled over, and a fixed fiducial A_s value.  After the Boltzmann code is run
and sigma_8 for the fiducial amplitude calculated, the CMB and matter power spectra
are scaled by (sigma8_input**2)/(sigma8_boltzmann**2), and sigma_8 is overwritten.



Assumptions
-----------

 - Spectra scale quadratically with sigma_8



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description


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
     - sigma_8
     - real
     - 
     - Late time amplitude sigma_8 as output from CAMB or another Boltzmann code
   * - 
     - sigma8_input
     - real
     - 
     - The desired sigma_8, usually from the sampler
   * - 
     - A_s
     - real
     - 
     - The fixed fiducial primordial amplitude
   * - cmb_cl
     - TT
     - real 1d
     - 
     - CMB TT power spectrum
   * - 
     - EE
     - real 1d
     - 
     - CMB EE power spectrum
   * - 
     - BB
     - real 1d
     - 
     - CMB BB power spectrum
   * - 
     - TE
     - real 1d
     - 
     - CMB TE power spectrum
   * - matter_power_lin
     - P_K
     - real 2d
     - 
     - Matter power spectrum P(k,z)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - cosmological_parameters
     - sigma_8
     - real
     - Re-scaled sigma_8, set to sigma_8_input
   * - 
     - A_s
     - real
     - Rescaled A_s
   * - cmb_cl
     - TT
     - real 1d
     - Rescaled CMB TT power spectrum
   * - 
     - EE
     - real 1d
     - Rescaled CMB EE power spectrum
   * - 
     - BB
     - real 1d
     - Rescaled CMB BB power spectrum
   * - 
     - TE
     - real 1d
     - Rescaled CMB TE power spectrum
   * - matter_power_lin
     - P_K
     - real 1d
     - Rescaled matter power spectrum P(k,z)


