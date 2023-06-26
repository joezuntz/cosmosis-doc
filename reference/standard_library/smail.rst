smail
================================================

Compute window functions for photometric n(z)

.. list-table::
    
   * - File
     - number_density/smail/photometric_smail.py
   * - Attribution
     - Donnacha Kirk
   * -
     - Simon Samuroff
   * -
     - Jessica Muir
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - You can do what you want with this file


This module takes inputs that specify the underlying spectroscopic (true) redshift
distribution of the galaxies in the survey.  It then convolves this with a photometric
error sigma(z) = sigma_0 (1+z) and optionally biases it.  It computes bin edges in the
survey assuming equal numbers in each.

You can also specify fixed bin edges.



Assumptions
-----------

 - Underlying true number density has Smail distribution
 - Photometric errors are sigma(z) = sigma_0 (1+z)
 - Bias fixed with redshift (if included)
 - Galaxies evenly divided between bins



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - nbin
     - int
     - 
     - Number of redshift bins with equal number of gals in each
   * - zmin
     - real
     - 0.0
     - Minimum redshift to compute
   * - zmax
     - real
     - 4.0
     - Maximum redshift to compute
   * - dz
     - real
     - 0.01
     - Spacing of samples to compute n(z) at.
   * - enforce_equal_numbers
     - bool
     - F
     - No matter how n(z) gets divided, specify that each bin has equal number density
   * - z_edges
     - real 1d
     - None
     - "Manually specified redshift bin edges. If nbin - 1 values passed,
these are the bounds of photometric selection for those nbin bins.
If 2 values are passed, they specify a minimum and maximum redshift between
which galaxies are divided into equal number samples. "



Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - number_density_params
     - alpha
     - real
     - 
     - Smail distribution parameter. n(z) = z^{alpha} exp{-(z/z0)^beta}
   * - 
     - beta
     - real
     - 
     - Smail distribution parameter
   * - 
     - z0
     - real
     - 
     - Smail distribution parameter
   * - 
     - sigz
     - real
     - 
     - Photometric error at z=0
   * - 
     - ngal
     - real
     - 
     - Total number density of galaxies per square arcmin
   * - 
     - bias
     - real
     - 
     - Bias on all photometric measurements


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - wl_number_density
     - nz
     - int
     - Number of redshift samples
   * - 
     - nbin
     - int
     - Number of bins
   * - 
     - z
     - real 1d
     - Redshift sample values
   * - 
     - bin_{i}
     - real 1d
     - n(z) at redshift sample values.  bin_1, bin_2, ...
   * - 
     - edge_{i}
     - real 1d
     - The nominal edges of the redshift bins (i.e. edges if no photometric errors)
   * - 
     - ngal_{i}
     - real
     - number density of redshift bin i


