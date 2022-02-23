Riess21
================================================

Likelihood of hubble parameter H0 from Riess et al supernova sample

.. list-table::
    
   * - File
     - likelihood/riess21/riess21.py
   * - Attribution
     - Riess et al (measurement)
   * -
     - CosmoSIS team (code)
   * - URL
     - 
   * - Citation
     - Riess et al, ApJLett, 908, 1
   * - Rules
     - None.


This small module was written for CosmoSIS.

Supernova type IA measurements are a standard(izable) candle 
that can be used to probe the relation between luminosity distance 
and redshift.  At low redshifts this directly probes the Hubble parameter,
H0.

The Riess et al 1% solution measurement of H0 is used in this module.



Assumptions
-----------

 - FRW cosmological model
 - Riess et al data set



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - mean
     - real
     - 0.732
     - Replace the standard value measurement H0 = 0.732 with a custom one for simulations
   * - sigma
     - real
     - 0.013
     - Replace the standard value error on H0 of 0.013 with a custom one


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
     - h0
     - real
     - 
     - Hubble parameter H0/(100 km/s/Mpc)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - RIESS21_LIKE
     - real
     - Gaussian likelihood value of supplied parameters


