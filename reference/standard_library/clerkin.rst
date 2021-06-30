clerkin
================================================

Compute galaxy bias as function of k, z for 3-parameter Clerkin et al 2014 model

.. list-table::
    
   * - File
     - bias/clerkin/clerkin_interface.py
   * - Attribution
     - L. Clerkin
   * - URL
     - 
   * - Citation
     - arXiv:1405.5521
   * -
     - Cole et al, MNRAS, 362, 2, 505–534
   * - Rules
     - Please cite the relevant papers if you use this module.


"The GTD bias model provides a benchmark expression for 
the redshift evolution of galaxy bias on large scales. 
This is crucial for rigorous comparison or combination 
of results. Choice of biasing model has a significant 
impact on cosmological parameter constraints, and an 
incorrect bias model will cause a shift in measured 
values of cosmological parameters. The three parameter 
GTD model, which encompasses several common bias models, 
has been shown to outperform the popular approach of a 
binned constant bias in obtaining unbiased estimates of 
cosmological parameters.

The GTD model is:
b(z) = c + (b_0 - c) / D(z)^alpha

where D(z) is the growth factor.

The Q model is:
b(k) = (1+Q k^2) / (a+A k)
 
This module creates bias fields and/or scales power spectra, 
depending on the chosen  options

The version of this model without redshift dependence is from Cole et al.

"



Assumptions
-----------

 - 3-parameter bias model from Clerkin et al l 2014



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - bias_only
     - bool
     - False
     - ) If set, do not use the matter power spectrum, just save the bias field
   * - model
     - str
     - gtd
     - Model choice. gtd, q, or q-gtd to use the GTD three-parameter model (z evolution only), the 2-parameter Q model (k scale only), or both
   * - suffix
     - str
     - ''
     - A suffix to append to the output section names below


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - galaxy_bias
     - b0
     - real
     - 
     - Bias at z=0 if GTD model used
   * - 
     - c
     - real
     - 
     - Bias parameter for GTD model
   * - 
     - alpha
     - real
     - 
     - Power law index for growth in GTD model
   * - 
     - Q
     - real
     - 
     - Numerator parameter in Q model
   * - 
     - A
     - real
     - 
     - Denominator parameter in Q model
   * - matter_power_nl
     - k_h
     - real 1d
     - 
     - Wavenumber in h/Mpc only if mode=power or both
   * - 
     - z
     - real 1d
     - 
     - Redshift only if mode=power or both
   * - 
     - P_k
     - real 2d
     - 
     - Nonlinear matter power only if mode=power or both


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - galaxy_power
     - k_h
     - real 1d
     - Wavenumber in h/Mpc, only if bias_only=F
   * - 
     - z
     - real 1d
     - Redshift, only if bias_only=F
   * - 
     - P_k
     - real 2d
     - Galaxy power, only if bias_only=F
   * - matter_galaxy_power
     - k_h
     - real 1d
     - Wavenumber in h/Mpc, only if bias_only=F
   * - 
     - z
     - real 1d
     - Redshift, only if bias_only=F
   * - 
     - P_k
     - real 2d
     - Matter-galaxy cross power, only if bias_only=F
   * - bias_field
     - k_h
     - real 1d
     - Wavenumber samples in h/Mpc of bias b(k, z)
   * - 
     - z
     - real 1d
     - Redshift samples
   * - 
     - b
     - real 2d
     - Galaxy bias b(k, z)
   * - 
     - r
     - real 2d
     - Stochastic bias r(k, z); identically 1 for these models.


