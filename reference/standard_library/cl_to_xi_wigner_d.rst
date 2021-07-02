cl_to_xi_wigner_d
================================================

Compute correlation functions from power spectra

.. list-table::
    
   * - File
     - shear/cl_to_xi_wigner/wigner_cl_xi_interface.py
   * - Attribution
     - Joe Zuntz
   * -
     - Nicolas Tessore
   * - URL
     - 
   * - Citation
     - https://arxiv.org/abs/1904.09973
   * - Rules
     -



This module creates and stores transformation matrices to convert power
spectra to correlation functions.

There is a general relation [arXiv:1904.09973]

    xi(theta) = sum_l (2*l + 1)/(4pi) C_l d^l_ss'(theta)

to convert between cl and xi of spin s and s' fields, using the reduced
Wigner d-functions. This is a linear relation that can be written in matrix
form. Once the values of theta are fixed, the matrix never changes.

A complication is that the theory Cls are not computed for all integer l up
to some ell_max, so that the available values must be interpolated at the
integers. Since linear interpolation is also a linear operation, it can be
absorbed directly into the transformation matrix, which as a result has
size n_theta x n_ell even if the above sum stretches to ell_max >> n_ell.
The interpolation is currently done linearly in ell, but could perhaps be
changed to be log-linear for better results.

The transformation matrices are computed on the first evaluation, which
takes a long time if ell_max is high, since (ell_max+1) x n_theta Wigner
d-function values are calculated. However, after the first time, each
cl-to-xi conversion is a cheap n_theta x n_ell matrix multiplication, so
one might come out ahead over a long run. These matrices could in principle
even be stored to disk for given settings of ell and theta.



Assumptions
-----------

 - Input C_ell up to large ell_max 10_000 ~ 100_000.



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - corr_type
     - int or str
     - 
     - Type of the correlation function: 0/xi, 1/wtheta, 2/gammat
   * - input_section_name
     - str
     - shear_cl, galaxy_cl, or galaxy_shear_cl, depending on corr_type
     - Name of the angular power spectrum input section. See shear/spectra module. (Default: )
   * - output_section_name
     - str
     - shear_xi, galaxy_shear_xi, or galaxy_xi depending on corr_type
     - Name of the angular correlation function output section


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


