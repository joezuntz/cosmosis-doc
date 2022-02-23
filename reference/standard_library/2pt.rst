2pt
================================================

Generic 2-point measurement Gaussian likelihood

.. list-table::
    
   * - File
     - likelihood/2pt/2pt_like.py
   * - Attribution
     - CosmoSIS Team
   * -
     - Niall Maccrann
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - None.


This module implements a general likelihood of tomographic 2-point measuremnts
of various quantities, including galaxy density, cosmic shear, intrinsic alignments,
CMB lensing, and the various cross powers between these.

Since this is a very general problem and there are a great many different configurations
of such data, this module relies on data being in the self-describing format that 
is discussed here: https://github.com/joezuntz/2point/
This format attempts to unambiguously describe the various aspects of a tomographic
two-point measurement to the point where its likelhood can be generated automatically.

This module looks up theory measurements in specific sections depending what kind
of measurement is used. To add more data types to the file please see type_table.txt.






Assumptions
-----------

 - A Gaussian likelihood approximation for two-point measurements
 - Data supplied in a specific file format



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
     - Filename of the 2pt format FITS file to use.
   * - data_sets
     - str
     - all
     - Space-separated list of which data sets from within the file to use for likelihoods.
   * - covmat_name
     - str
     - COVMAT
     - Name of the covariance matrix extension to use in the data file.
   * - angle_range_{dataset}_{i}_{j}
     - str
     - 
     - Pair of real numbers. If set, for the given data set and pair of bins, cut down the data used to this angular range  (min and max)
   * - cut_{dataset}
     - str
     - 
     - Space-separated list of i,j pairs. (no spaces within the pair, just betwen them, e.g. cut_lss = 1,2  1,1  3,4.  Remove this bin from the likelihood.
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
   * - kind
     - str
     - cubic
     - The interpolation to do into the theory splines. See scipy.interpolate.interp1d.
   * - gaussian_covariance
     - bool
     - False
     - C_ell likelihoods only. Generate a Gaussian covariance matrix for the data.
   * - survey_area
     - real
     - 
     - If gaussian_covariance=T, the sky area of the survey
   * - number_density_shear_bin
     - real
     - 
     - If gaussian_covariance=T, the number of galaxies per bin per sq arcmin in the WL data
   * - number_density_lss_bin
     - real
     - 
     - If gaussian_covariance=T, the number of galaxies per bin per sq arcmin in the LSS data
   * - sigma_e_bin
     - real
     - 
     - If gaussian_covariance=T, the standard deviation of the intrinsic shape noise in the WL data


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
     - theta
     - real 1d
     - 
     - If a real-space measurement is used, the angle in radians of the predicted theory curves.
   * - 
     - bin_{i}_{j}
     - real 1d
     - 
     - For various i,j depending what is found in the file, the theory predictions for this value. For example, C_ell or xi(theta)


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


