Sheth-Tormen MF
================================================

Code to compute the Sheth-Tormen mass function given Pk from CAMB, based on Komatsu's CRL

+-----------+----------------------------------------------+
| File      | mass_function/mf_shethtormen/st_mf_module.so |
+-----------+----------------------------------------------+
| URL       | http://www.mpa-garching.mpg.de/~komatsu/crl/ |
+-----------+----------------------------------------------+
| Citations | http://www.mpa-garching.mpg.de/~komatsu/crl/ |
+-----------+----------------------------------------------+

This module calculates the Sheth-Tormen mass function given the linear matter power spectrum.


Assumptions
-----------

 - CAMB must be run to output linear matter Pk



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - feedback
     - int
     - 0
     - Amount of output to print.  0 for no feedback.  1 for basic.
   * - redshift_0
     - int
     - 0
     - 1 outputs only z=0 mf. 0 outputs mass functions for each Pk in datablock


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
     - k
     - real 1d
     - 
     - Sample values of linear spectrum in Mpc/h
   * - 
     - z
     - real 1d
     - 
     - Redshift of linear spectrum samples
   * - 
     - P
     - real 2d
     - 
     - Linear spectrum in (Mpc/h)^{-3}


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - mass_function
     - r_h
     - real 1d
     - R in (h^-1 Mpc)
   * - 
     - m_h
     - real 1d
     - Mass in (omega_matter h^-1 M_solar)
   * - 
     - dndlnrh
     - real 2d
     - Dn/dlnRh (h^3 Mpc^-3)
   * - 
     - dndlnmh
     - real 2d
     - Dn/dlnMh (h^3 Mpc^-3)


