sigma_r
================================================

Compute anisotropy dispersion sigma(R,z)

.. list-table::
    
   * - File
     - boltzmann/sigmar/sigmar.py
   * - Attribution
     - Scott Dodelson
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


"sigma(R,z) is the variance of cosmic density fluctuations on scales
down to 8 Mpc/h.

In Fourier space is given by sigma(R,z) = \int_0^\infty W^2(k R) k^2 P(k,z) / (2 \pi)^2 dk

The P(k,z) used could in general be linear or non-linear, but usually when people
say sigma they mean the non-linear variant.
"



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
   * - matter_power
     - str
     - matter_power_lin
     - Name of section to get P(k,z) from, e.g. matter_power_lin, matter_power_nl
   * - crop_klim
     - bool
     - True
     - Crops the klimits of the sigma integral to max(0.01/R, kmin), min(100/R, kmax)


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

   * - sigmar
     - R
     - real 1d
     - Scale R of output in Mpc/h
   * - 
     - z
     - real 1d
     - Redshift of output
   * - 
     - sigma2
     - real 2d
     - Variance sigma^2(R,z)


