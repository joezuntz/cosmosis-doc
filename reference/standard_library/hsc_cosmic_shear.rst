hsc_cosmic_shear
================================================

Likelihoods of the HSC Year 3 cosmic shear data

+-------------+------------------------------------------------------+
| File        | likelihood/hsc_cosmic_shear/hsc_cosmic_shear_like.py |
+-------------+------------------------------------------------------+
| Attribution | HSC Collaboration (data)                             |
+-------------+------------------------------------------------------+
|             | Roohi Dalal                                          |
+-------------+------------------------------------------------------+
|             | Xiangchong                                           |
+-------------+------------------------------------------------------+
| URL         |                                                      |
+-------------+------------------------------------------------------+
| Citations   | https://doi.org/10.48550/arXiv.2304.00701            |
+-------------+------------------------------------------------------+

Dalal et al presented measuremets of the cosmic shear E-mode power spectrum
made using three years of data from the  Hyper Suprime-Cam (HSC) survey.
This module implements the likelihood of that data, using the sacc format.
This module is a subclass of the sacc_like likelihood in likelihood/sacc_like.
See the documentation for that module for more details.

Note that the analysis presented in Dalal et al used 
the power spectrum from the linear BACCO emulator and pyhmcode2016, the
interfaces for which are not public immediately. They will be released soon.


Assumptions
-----------

 - HSC measurements of cosmic shear power spectra



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_file
     - str
     - 
     - Filename of the sacc file to use.
   * - data_sets
     - str
     - all
     - Space-separated list of which data sets from within the file to use for likelihoods.
   * - keep_tracers
     - str
     - 
     - Regular expression to select tracers to use.
   * - angle_range_{dataset}_{i}_{j}
     - str
     - 
     - Pair of real numbers. If set, for the given data set and pair of bins, cut down the data used to this angular range  (min and max)
   * - cut_{dataset}
     - str
     - 
     - Space-separated list of i,j pairs. (no spaces within the pair, just betwen them, e.g. cut_lss = 1,2  1,1  3,4.  Remove this bin from the likelihood.
   * - {name}_section
     - str
     - Various depending on name.
     - For each {name} in the data types used from the file, a cosmosis block section to look for the theory predictions in.
   * - save_theory
     - str
     - 
     - If set, save the theory predictions used in the likelihood to this sacc file.
   * - save_realization
     - str
     - 
     - If set, save a simulated data set to this sacc file.
   * - covariance_realizations
     - int
     - -1
     - If >0, assume that the Covariance matrix was estimated from a set of MC simulations and should thus have the Anderson-Hartlap factor applied to increase its size. If zero, assume infinite number of realizations.
   * - sellentin
     - bool
     - False
     - If set, use the Sellentin-Heavens 2016 change to the likelihood to account for this distribution of the covariance estimates. This changes the likelihood to a student's-t form. Note that this invalidates the simulated data sets used for the ABC sampler.
   * - like_name
     - str
     - 2pt
     - The name of the likelihood to save.
   * - likelihood_only
     - bool
     - False
     - Skip saving the covariance, inverse, simulation, etc. Saves some time.
   * - kind
     - str
     - cubic
     - The interpolation to do into the theory splines. See scipy.interpolate.interp1d.


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - shear_cl
     - ell
     - real 1d
     - 
     - If a Fourier-space measurement is used, the angular wave-number of the predicted theory curves.  The name of the section here depends on the data type used from the file. It might be galaxy_cl or shear_cl, for example.
   * - 
     - bin_{i}_{j}
     - real 1d
     - 
     - For various i,j depending what is found in the file, the theory predictions for this value. For example, C_ell.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - 2pt_like
     - real
     - Gaussian likelihood value. Name can be changed in parameter file (see above) for this and the other outputs below.
   * - data_vector
     - 2pt_data
     - real 1d
     - The full vector of data points used in the likelihood
   * - 
     - 2pt_theory
     - real 1d
     - The full vector of theory points used in the likelihood
   * - 
     - 2pt_covariance
     - real 2d
     - The covariance matrix used
   * - 
     - 2pt_inverse_covariance
     - real 2d
     - The inverse covariance matrix (precision matrix) used.
   * - 
     - 2pt_simulation
     - real 1d
     - A simulated data set from the given theory and covariance matrix.
   * - 
     - 2pt_angle
     - real 1d
     - The angular scale used for each data point.
   * - 
     - 2pt_bin1
     - int 1d
     - The first bin index used for each data point
   * - 
     - 2pt_bin2
     - int 1d
     - The second bin index used for each data point


