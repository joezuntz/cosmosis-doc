photoz_bias
================================================

Modify a set of loaded n(z) distributions with a multiplicative or additive bias

.. list-table::
    
   * - File
     - number_density/photoz_bias/photoz_bias.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


Photometric redshift distributions can contain biases - the actual distribution
of galaxies in a survey can be different to the estimated one.

This bias can remain even after calibration with a spectroscopic sample, or by other methods.

This module models the simplest possible type of n(z) bias - a simple shift in z by a multiplicative
or additive factor. The idea is that the shift parameter should be marginalized in sampling over to 
account for this bias.  Note that this is *not* the same as simply widening the n(z).

Ranges or priors should be put on the size of the bias that reflect your knowledge of remaining
possible biases.

The mode is:
n(z) -> n(z-b) or n(z*(1-b))


Assumptions
-----------

 - Simple photo-z bias models: n(z) -> n(z-b) or n(z*(1-b))



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - mode
     - str
     - 
     - 'multiplicative' or 'additive', depending on what kind of bias model you want
   * - sample
     - str
     - 
     - If set, look for n(z) in the section called sample, and error parameters in sample_errors
   * - bias_section
     - str
     - 
     - If set, look for input parameters in this named section instead of wl_photoz_errors. If not set but sample is set, look in sample_errors
   * - interpolation
     - str
     - cubic
     - Type of interpolation to use in scipy.interpolate.interp1d
   * - per_bin
     - bool
     - True
     - Whether to use one value per bin, If False, use one value for all bins.


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - wl_number_density
     - nbin
     - int
     - 
     - Number of redshift bins
   * - 
     - z
     - real 1d
     - 
     - Redshift sample points of n(z) estimates
   * - 
     - bin_i
     - real 1d
     - 
     - n(z)for i=1..nbin. n(z) estimates
   * - wl_photoz_errors
     - bias_i
     - real
     - 
     - For i=1..nbin if per_bin=T or i=0 otherwise. Bias delta-z for this bin.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - wl_number_density
     - bin_i
     - real 1d
     - n(z) for i=1..nbin. Modified n(z) estimates replaced old value


