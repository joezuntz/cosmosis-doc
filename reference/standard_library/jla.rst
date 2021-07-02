jla
================================================

Supernova likelihood for SDSS-II/SNLS3

.. list-table::
    
   * - File
     - supernovae/jla_v3/jla.so
   * - Attribution
     - Marc Betoule
   * - URL
     - http://supernovae.in2p3.fr/sdss_snls_jla/ReadMe.html
   * - Citation
     - http://arxiv.org/abs/1401.4064
   * - Rules
     -


"This JLA code uses 731 supernovae from the JLA SDSS-II/SNLS3 sample 
to get a likelihood of a given theory mu(z).

Systematic error propagation is done with a collection of separate 
covariance matrices for the various light-curve parameters.

You can copy the standard parameters to use for this from demos/demo5.ini
"



Assumptions
-----------

 - SALT2 used to fit light curves
 - Akima interpolation between mu(z) samples



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_dir
     - str
     - 
     - Dir for other files. Use cosmosis-standard-library/supernovae/jla_v3/data (unless trying a different data set)
   * - data_file
     - str
     - 
     - Dir for other files. Use jla_lcparams.txt (unless trying a different data set)
   * - scriptmcut
     - str
     - 
     - Dir for other files. Use 10.0
   * - mag_covmat_file
     - str
     - 
     - Dir for other files. Use jla_v0_covmatrix.dat
   * - stretch_covmat_file
     - str
     - 
     - Dir for other files. Use jla_va_covmatrix.dat
   * - colour_covmat_file
     - str
     - 
     - Dir for other files. Use jla_vb_covmatrix.dat
   * - mag_stretch_covmat_file
     - str
     - 
     - Dir for other files. Use jla_v0a_covmatrix.dat
   * - mag_colour_covmat_file
     - str
     - 
     - Dir for other files. Use jla_v0b_covmatrix.dat
   * - stretch_colour_covmat_file
     - str
     - 
     - Dir for other files. Use jla_vab_covmatrix.dat


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - distances
     - z
     - real 1d
     - 
     - Redshift sample values for theory
   * - 
     - mu
     - real 1d
     - 
     - Theory distance modulus at sample redshifts
   * - supernova_params
     - alpha
     - real
     - 
     - SN shape parameter coefficient
   * - 
     - beta
     - real
     - 
     - SN color parameter coefficient
   * - 
     - M
     - real
     - 
     - SN magnitude parameter baseline value; leave this fixed and vary deltaM.
   * - 
     - deltaM
     - real
     - 
     - SN magnitude parameter where M_actual = M + deltaM


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - JLA_LIKE
     - real
     - Gaussian likelihood for this data set and theory mu(z)


