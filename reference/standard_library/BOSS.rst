BOSS
================================================

Compute the likelihood of supplied fsigma8(z=0.57), H(z=0.57), D_a(z=0.57), omegamh2, bsigma8(z=0.57)

+-------------+--------------------------------+
| File        | likelihood/boss/boss_rsd.py    |
+-------------+--------------------------------+
| Attribution | SDSS-III BOSS Team             |
+-------------+--------------------------------+
| URL         | http://www.sdss3.org           |
+-------------+--------------------------------+
| Citations   | http://arxiv.org/abs/1303.4486 |
+-------------+--------------------------------+

This module calculates the likelihood using the CMASS only results from 
Chuang et al. 2013 for fsigma8(z=0.57), H(z=0.57), D_a(z=0.57), omegamh2, bsigma8(z=0.57).
There are two modes: mode=0 give the fsigma8(z=0.57) likelihood only; mode=1 give the more general BOSS likelihood.


Assumptions
-----------

 - SDSS-III CMASS DR9 dataset
 - When using mode = 1 CAMB must be run to output distance parameters and sigma8
 - The transfer function must be scale-independent to use this simple formulation: no MG, massive nu, for example.



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - mode
     - int
     - 0
     - Mode=0 for a f*sigma8 likelihood only. mode=1 uses the full results, a likelihood of H(z), D_A(z), ommh2, b * sigma_8, f * sigma_8]
   * - feedback
     - int
     - 
     - Amount of output to print.  0 for no feedback.  1 for basic (default = 0)
   * - mean
     - real
     - 0.428
     - Mean of f * sigma8
   * - sigma
     - real
     - 0.066
     - Error bar on f * sigma8
   * - redshift
     - real
     - 0.57
     - Redshift if measurement


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - growth_parameters
     - d_z
     - real 1d
     - 
     - Linear growth factor D(z)
   * - 
     - f_z
     - real 1d
     - 
     - Linear growth rate f(z)
   * - 
     - z
     - real 1d
     - 
     - Redshift of samples
   * - cosmological_parameters
     - omega_m
     - real
     - 
     - Baryon + CDM density fraction today
   * - 
     - sigma_8
     - real
     - 
     - Amplitude of linear matter power at 8/h Mpc at z=0
   * - 
     - bias
     - real
     - 
     - Galaxy bias
   * - 
     - h0
     - real
     - 
     - Hubble parameter H0/(100 km/s/Mpc)
   * - distances
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - d_a
     - real 1d
     - 
     - Angular diameter distance in Mpc
   * - 
     - h
     - real 1d
     - 
     - Hubble parameter with in units of Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - BOSS_LIKE
     - real
     - Likelihood of supplied fsigma8(z=0.57), H(z=0.57), D_a(z=0.57), omegamh2, bsigma8(z=0.57)


