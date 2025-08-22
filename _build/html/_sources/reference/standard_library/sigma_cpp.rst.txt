sigma_cpp
================================================

Compute anisotropy dispersion sigma(R,z) in cpp

+-------------+----------------------------------+
| File        | boltzmann/sigma_cpp/sigma_cpp.py |
+-------------+----------------------------------+
| Attribution | Michel Aguena                    |
+-------------+----------------------------------+
| URL         |                                  |
+-------------+----------------------------------+

sigma(R,z) is the variance of cosmic density fluctuations on scales
down to 8 Mpc/h.

In Fourier space is given by :math:`sigma(R,z) = \int_0^\infty W^2(k R) k^2 P(k,z) / (2 \pi)^2 dk`

The P(k,z) used could in general be linear or non-linear, but usually when people
say sigma they mean the non-linear variant.


Assumptions
-----------

 - minimal assumptions; sigma computed directly from P(k,z)



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - zmin
     - real
     - 
     - Minimum redshift to generate values for
   * - zmax
     - real
     - 
     - Maximum redshift to generate values for
   * - dz
     - real
     - 
     - Output redshift sample spacing
   * - z
     - real
     - 
     - Values of redshift to generate values for, overwrites (zmin, zmax, dz)
   * - logmmin
     - real
     - 
     - Minimum value of log10(Mass) [in M_sun/h] to generate values for
   * - logmmax
     - real
     - 
     - Maximum value of log10(Mass) [in M_sun/h] to generate values for
   * - dlogm
     - real
     - 
     - log10(Mass) spacing
   * - logm
     - real
     - 
     - Values of log10(Mass) [in M_sun/h] to generate values for, overwrites (logmmin, logmmax, dlogm)
   * - rmin
     - real
     - 
     - Minimum scale R in Mpc/h to generate values for
   * - rmax
     - real
     - 
     - Maximum scale R in Mpc/h to generate values for
   * - dr
     - real
     - 
     - Scale R spacing
   * - r
     - real
     - 
     - Values of R [Mpc/h] to generate values for, overwrites (rmin, rmax, dr)
   * - matter_power
     - str
     - matter_power_lin
     - Name of section to get P(k,z) from, e.g. matter_power_lin, matter_power_nl
   * - use_m
     - bool
     - False
     - Uses the mass values as a base for the computation instead of R
   * - verbose
     - bool
     - False
     - Prints details of the computation


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
     - k_h
     - real 1d
     - 
     - Sample values of linear spectrum in Mpc/h.  Section name specified by parameter in ini file.
   * - 
     - z
     - real 1d
     - 
     - Redshift of linear spectrum samples.  Section name specified by parameter in ini file.
   * - 
     - P_k
     - real 2d
     - 
     - Linear spectrum in (Mpc/h)^{-3}.  Section name specified by parameter in ini file.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - sigma_cpp
     - R
     - real 1d
     - Scale R of output samples in Mpc/h
   * - 
     - logm
     - real 1d
     - log10(Mass) samples [in M_sun/h]; matches R
   * - 
     - z
     - real 1d
     - Redshift of output samples
   * - 
     - sigma
     - real 2d
     - Variance sigma(R,z) of samples


