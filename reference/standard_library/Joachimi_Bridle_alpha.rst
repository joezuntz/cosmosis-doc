Joachimi_Bridle_alpha
================================================

Calculate the gradient of the galaxy luminosity function at the limiting magnitude of the survey.

.. list-table::
    
   * - File
     - luminosity_function/Joachimi_Bridle_alpha/interface.py
   * - Attribution
     - CosmoSIS team
   * -
     - Simon Samuroff
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


"
The gradient of the cumulative galaxy luminosity function \alpha is sensitive to both redshift and magnitude limit of the survey 
considered. Joachimi & Bridle (2010) extend the fitting function of Blake & Bridle (2005) to obtain a polynomial \alpha(z, r_lim) 
at a range of redshifts, where z_i is the median in redshift bin i and r_lim is the r-band magnitude limit. Note that the fitting is based on ground-based
data from the COMBO-17 survey. See Joachimi & Bridle (2010) for discussion of its applicability. 
"



Assumptions
-----------

 - The galaxy luminosity function is well approximated by the fitting function of Blake & Bridle (2005).
 - The limiting r-band magnitude r_lim>16.9 



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - magnitude_limit
     - real
     - 24.0
     - Limiting r-band magnitude of the survey considered.
   * - binned_alpha
     - bool
     - True
     - Compute alpha in the survey redshift bins, rather than as a continuous funtion of redshift.


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - wl_num_density
     - Nz
     - int
     - 
     - Number of points used to evaluate the distribution in each redshift bin.
   * - 
     - nzbin
     - int
     - 
     - Number of survey redshift bins.
   * - 
     - zmax
     - real
     - 
     - Maximum redshift of the redshift distributions.
   * - 
     - bin_{i}
     - real 1d
     - 
     - An array of Nz points evenly sampled from the galaxy redshift distribution in bin i in the range z={0...zmax}. The index ranges i={0, 1, ..., nzbin}.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - galaxy_luminosity_function
     - z
     - real 1d
     - Redshift values of alpha(z) samples
   * - 
     - alpha
     - real 1d
     - Gradient of the logarithmic cumulative galaxy luminosity function at the limiting magnitude.
   * - 
     - z_binned
     - real 1d
     - Median values of the n(z) in the survey redshift bins.
   * - 
     - alpha_binned
     - real 1d
     - Gradient of the logarithmic cumulative galaxy luminosity function at the limiting magnitude, evaluated at the median redshift of each bin.


