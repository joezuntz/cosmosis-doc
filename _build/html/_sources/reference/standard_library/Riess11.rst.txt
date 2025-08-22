Riess11
================================================

Likelihood of hubble parameter H0 from Riess et al supernova sample

+-------------+-----------------------------------------------------------------------+
| File        | likelihood/riess11/riess11.py                                         |
+-------------+-----------------------------------------------------------------------+
| Attribution | Riess et al (measurement)                                             |
+-------------+-----------------------------------------------------------------------+
|             | CosmoSIS team (code)                                                  |
+-------------+-----------------------------------------------------------------------+
| URL         | http://pdg.lbl.gov/2013/reviews/rpp2013-rev-bbang-nucleosynthesis.pdf |
+-------------+-----------------------------------------------------------------------+
| Citations   | Riess et al, ApJ, 730, 2, 119 (2011)                                  |
+-------------+-----------------------------------------------------------------------+
|             | Riess et al, ApJ, 732, 2, 129 (2011)                                  |
+-------------+-----------------------------------------------------------------------+

This small module was written for CosmoSIS.

Supernova type IA measurements are a standard(izable) candle 
that can be used to probe the relation between luminosity distance 
and redshift.  At low redshifts this directly probes the Hubble parameter,
H0.

The Riess et al 3% solution measurement of H0 is used in this module.



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
     - 0.738
     - Replace the standard value measurement H0 = 0.738 with a custom one for simulations
   * - sigma
     - real
     - 0.024
     - Replace the standard value error on H0 of 0.024 with a custom one


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
     - RIESS_LIKE
     - real
     - Gaussian likelihood value of supplied parameters


