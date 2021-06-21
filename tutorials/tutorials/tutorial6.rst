Tutorial 6: Two-Point Pipelines
-------------------------------

CosmoSIS has been widely used in weak lensing and galaxy clustering science.

This tutorial shows how to build pipelines for two-point correlation function likelihoods.  You can find the code to run this in the cosmosis-standard-library example ``examples/des-y1.ini``.  This 


Science Overview
================

The general sequence of calculations for 2-point likelihoods is:
- Compute the 3D matter power spectra P(k, z)
- Determine galaxy source number density n(z)
- Use the Limber equation (or a more precise equivalent) to integrate these two together and get the 2D power spectra C_ell
- Apply various astrophysical biases to the C_ell
- Use a Hankel transform (or a more precise equivalent) to convert from Fourier space C_ell to real space correlation functions
- Compare the correlation functions to measurements

CosmoSIS has modules for each of these phases


Matter Power
============

In this version of CosmoSIS the linear and non-linear matter power calculations are usually done with the ``camb`` module.  This takes the cosmological parameters as input and computes the linear and non-linear matter power spectra, and background values like distances as a function of redshift.



Number Density
==============

The number densities of sources are typically uncertain for photometric cosmology.  So there are typically two steps in specifying the distribution to actually be used: (i) providing a fixed baseline distribution, and (ii) mutating that distribution according to some parameters.

For 3x2pt cosmology (clustering and lensing combined) this must be done for both the clustering and lensing samples independently, if there are errors on both.

The modules ``load_nz`` and ``load_nz_fits`` can be used to load number densities from a text file or a FITS file (in the DES format) respectively and provide them at each iteration. Then  ``photoz_bias`` and ``photoz_distortion`` can be used to distort the n(z) after it has been loaded.




C_ell Calculation
=================

The CosmoSIS standard library module ``project_2d`` can be used to
integrate 3D power spectra (such as matter or galaxy power spectra)
with a pair of kernels into 2D power spectra using the Limber integral.

This is an approximation which often applies at small scales and when
using a broad enough kernel.

In a flat cosmology the Limber integral is:

.. math::
    C^{12}_\ell =  A \int_0^{\chi_1} W_1(\chi) W_2(\chi) P(k=(l+0.5)/\chi, z(\chi)) / chi^2 d\chi

where the two W functions are kernels that describe the response of the statistic to
with distance and P is a 3D power spectrum.  Different quantities can be calculated using different
choices for the W and P functions.

For galaxy clustering spectra, P is the galaxy power spectrum and
the W functions are the galaxy number densities n(z).

For weak lensing spectra, P is the matter power spectrum and the W functions
are given by:

.. math::
    W^{\mathrm{WL}}_\chi =  \frac{3}{2}\Omega_m H_0^2 a^{-1}(\chi) \chi \frac{1}{\bar{n}} \int_\chi^\infty \mathrm{d}\chi_s n(\chi_s) \frac{\chi_s - \chi}{\chi_s}

This quantitiy is calculated in the module.


Galaxy Bias
===========


Shear Calibration Bias
======================


Intrinsic Alignments
====================