cl_to_corr
================================================

Compute correlation functions xi+, xi-, w, and gamma_t from C_ell

.. list-table::
    
   * - File
     - shear/cl_to_corr/cl_to_corr.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


"
The correlation functions are related to the spectra via Bessel functions:
\xi_{+}(theta) = \int_0^\infty C^{ss}_\ell J_{0}(\ell \theta) \ell d\ell / 2\pi
\xi_{-}(theta) = \int_0^\infty C^{ss}_\ell J_{4}(\ell \theta) \ell d\ell / 2\pi
  w{-}(theta) = \int_0^\infty C^{gg}_\ell J_{4}(\ell \theta) \ell d\ell / 2\pi
\gamma_t(theta) = \int_0^\infty C^{gs}_\ell J_{(0,4)}(\ell \theta) \ell d\ell / 2\pi

where s=shear and g=galaxy position.
In this module that integral is done via a Hankel Transform.
"



Assumptions
-----------

 - Input C_ell sufficiently well-sampled over chosen range
 - Ell and theta values consistently chosen



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - corr_type
     - str
     - 
     - Either w, gamma, or xi depending which transforms you want
   * - input_section_name
     - str
     - 
     - Name of the angular power spectrum input section. See shear/spectra module. (Default: 'shear_cl', 'galaxy_cl', or 'galaxy_shear_cl' depending on corr_type)
   * - output_section_name
     - str
     - 
     - Name of the angular correlation function output section (Default: 'shear_xi', 'galaxy_xi', or'galaxy_shear_xi' depending on corr_type)
   * - n_transform
     - int
     - 8192
     - Number of points in the transform.
   * - ell_min_extrapolate
     - real
     - 0.0001
     - Minimum value of ell to extrapolate the input ell to in the transform.
   * - ell_max_extrapolate
     - real
     - 5000000.0
     - Maximum value of ell to extrapolate the input ell to in the transform.
   * - theta_min
     - real
     - 0.1
     - Minimum value of output theta values to go to, in arcmin
   * - theta_max
     - real
     - 1000
     - Maximum value of output theta values to go to, in arcmin


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
     - The number of redshift bins in thesecond quantity
   * - 
     - nbin
     - int
     - 
     - Number of redshift bins used if nbin_a or b not found.
   * - 
     - bin_{i}_{j}
     - real 1d
     - 
     - C_ell (no l(l+1) factor) for bin i and j. Only need j<=i for modes 0 and 1.


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
     - xi_plus(theta) bin i and j, only if mode=xi Only stores j<=i.
   * - 
     - ximinus_i_j
     - real 1d
     - xi_minus(theta) bin i and j, only if mode=xi. Only stores j<=i.
   * - 
     - bin_i_j
     - real 1d
     - w(theta) or gamma_t(theta) for bin i and j, only if mode=w or gamma respectively. Only stores j<=i.
   * - 
     - nbin_a
     - int
     - Number of i tomographic bins
   * - 
     - nbin_b
     - int
     - Number of j tomographic bins


