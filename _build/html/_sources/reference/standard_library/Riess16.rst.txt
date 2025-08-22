Riess16
================================================

Likelihood of hubble parameter H0 from Riess et al 2.4% supernova sample

+-------------+------------------------------------------------------------------+
| File        | likelihood/riess16/riess11.py                                    |
+-------------+------------------------------------------------------------------+
| Attribution | Riess et al (measurement)                                        |
+-------------+------------------------------------------------------------------+
|             | CosmoSIS team (code)                                             |
+-------------+------------------------------------------------------------------+
| URL         | http://iopscience.iop.org/article/10.3847/0004-637X/826/1/56/pdf |
+-------------+------------------------------------------------------------------+
| Citations   | Riess et al, ApJ, 826, 56, 31 (2016)                             |
+-------------+------------------------------------------------------------------+

This small module was written for CosmoSIS.

Supernova type IA measurements are a standard(izable) candle 
that can be used to probe the relation between luminosity distance 
and redshift.  At low redshifts this directly probes the Hubble parameter,
H0.

The Riess et al 2.4% solution measurement of H0 is used in this module.



Assumptions
-----------

 - FRW cosmological model
 - Riess et al 2016 data set



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
     - 0.7324
     - Replace the standard value measurement h = 0.7324 with a custom one for simulations
   * - sigma
     - real
     - 0.0174
     - Replace the standard value error on h of 0.0174 with a custom one


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
     - RIESS16_LIKE
     - real
     - Gaussian likelihood value of supplied parameters


