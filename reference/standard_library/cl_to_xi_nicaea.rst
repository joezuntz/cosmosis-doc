cl_to_xi_nicaea
================================================

Compute WL correlation functions xi+, xi- from C_ell

+-------------+-------------------------------------------+
| File        | shear/cl_to_xi_nicaea/nicaea_interface.so |
+-------------+-------------------------------------------+
| Attribution | Martin Kilbinger                          |
+-------------+-------------------------------------------+
|             | Nicaea Team                               |
+-------------+-------------------------------------------+
| URL         |                                           |
+-------------+-------------------------------------------+
| Citations   | http://arxiv.org/abs/0810.5129            |
+-------------+-------------------------------------------+


The correlation functions are related to the spectra via Bessel functions:
:math:`\xi_{(+/-)}(\theta) = \int_0^\infty C_\ell J_{(0/4)}(\ell \theta) \ell d\ell / 2\pi`

In this module that integral is done via a Hankel Transform.

This module is a part of the Nicaea code, with the interface written by Niall
Maccrann.  It avoids the ringing problems of the alternative cl_to_xi code but
generates results only on a fixed range in theta .

The output theta values will always be from about 2.0e-07 to 1.0e+04 radians, but
only in part of that regime, from about 1 to a few hundred arcmin, will the results
be numerically valid.  The input ell must include the corresponding range, and
will be extrapolated linearlly before that and cubically after it.




Assumptions
-----------

 - Input C_ell sufficiently well-sampled over standard pre-defined range



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - corr_type
     - int
     - 
     - Either 0 (to do shear EE C_ell -> xi+(theta) and xi-(theta)), or 1 (to convert galaxy position C_ell to w(theta)) or 2 (to convert the cross galaxy position-shear C_ell to gamma_t(theta))
   * - input_section_name
     - str
     - 
     - Name of the angular power spectrum input section. See shear/spectra module. (Default: 'shear_cl', 'galaxy_cl', or 'galaxy_shear_cl' depending on corr_type)
   * - output_section_name
     - str
     - 
     - Name of the angular correlation function output section (Default: 'shear_xi', 'galaxy_shear_xi', or 'galaxy_xi' depending on corr_type)


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - input_section_name
     - ell
     - real 1d
     - 
     - Sample ell values for input C_ell
   * - 
     - nbin_a
     - int
     - 
     - The number of redshift bins in the first quantity
   * - 
     - nbin_b
     - int
     - 
     - The number of redshift bins in the second quantity
   * - 
     - nbin
     - int
     - 
     - Number of redshift bins used if nbin_a or b not found.
   * - 
     - bin_i_j
     - real 1d
     - 
     - S C_ell (no l(l+1) factor) for bin i and j. Only need j<=i for modes 0 and 1.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - output_section_name
     - theta
     - real 1d
     - Sample theta values for output xi(theta)
   * - 
     - xiplus_i_j
     - real 1d
     - xi_plus(theta) bin i and j, only if mode=0 Only stores j<=i.
   * - 
     - ximinus_i_j
     - real 1d
     - xi_minus(theta) bin i and j, only if mode=0. Only stores j<=i.
   * - 
     - bin_i_j
     - real 1d
     - w(theta) or gamma_t(theta) for bin i and j, only if mode=1 or 2 respectively. Only stores j<=i.
   * - 
     - nbin_a
     - int
     - Number of i tomographic bins
   * - 
     - nbin_b
     - int
     - Number of j tomographic bins


