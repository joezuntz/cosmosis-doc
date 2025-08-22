Extreme_Value_Statistics
================================================

PDF of the maximum cluster mass given cosmological parameters

+-------------+---------------------------------------+
| File        | likelihood/cluster_evs/cluster_evs.py |
+-------------+---------------------------------------+
| Attribution | Harrison & Coles 2012                 |
+-------------+---------------------------------------+
|             | CosmoSIS team (code)                  |
+-------------+---------------------------------------+
| URL         |                                       |
+-------------+---------------------------------------+
| Citations   | Harrison and Coles, MNRAS 421 2012    |
+-------------+---------------------------------------+

Computes the likelihood of the largest observed cluster near
the specified redshift range being M_max, as loaded from the datablock, 
given the mass function.

Requires the mass function calculated from M_min to M_max, for example 
by mf_tinker module, run withwith redshift_zero=0 to generate dndlnm. 

Optionally, can also generate a full PDF with output_pdf=T



Assumptions
-----------

 - FRW cosmological model



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - redshift
     - real
     - 
     - Output z of cluster where integration limits: zmin = z - 0.02, zmax = z + 0.02
   * - output_pdf
     - bool
     - False
     - If True, output PDF for range of masses, only recommended for test runs
   * - frac
     - real
     - 1.0
     - Fraction of the sky observed between zmin and zmax
   * - M_min
     - real
     - 1.0E14
     - Minimum mass for PDF in M_sun/h
   * - M_max
     - real
     - 2.0E15
     - Maximum mass for PDF in M_sun/h
   * - n_m
     - int
     - 100
     - Number of log-spaced masses for PDF


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
   * - 
     - omega_m
     - real
     - 
     - Omega matter
   * - distances
     - z
     - real 1d
     - 
     - Redshifts
   * - 
     - d_a
     - real
     - 
     - Angular diameter distance as a function of z
   * - mass_function
     - z
     - real 1d
     - 
     - Redshifts
   * - 
     - r_h
     - real 1d
     - 
     - Radii (Mpc/h)
   * - 
     - dndlnmh
     - real 1d
     - 
     - Mass function (h^3 Mpc^-3)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - evs
     - m
     - real 1d
     - Mass (M_sun/h) (if output_pdf=True)
   * - 
     - logphi
     - real 1d
     - Log of PDF (if output_pdf=True)
   * - likelihoods
     - evs_like
     - real
     - Likelihood of M_max


