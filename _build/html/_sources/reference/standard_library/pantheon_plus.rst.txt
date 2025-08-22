pantheon_plus
================================================

Likelihood of the Pantheon+ supernova analysis optionally combined with the SH0ES H0 measurement

+-------------+-------------------------------------------------+
| File        | likelihood/pantheon_plus/pantheon_plus_shoes.py |
+-------------+-------------------------------------------------+
| Attribution | Dillon Brout                                    |
+-------------+-------------------------------------------------+
| URL         | https://pantheonplussh0es.github.io/            |
+-------------+-------------------------------------------------+
| Citations   | ApJ 938 110 (2022)                              |
+-------------+-------------------------------------------------+
|             | Adam G. Riess et al 2022 ApJL 934 L7            |
+-------------+-------------------------------------------------+

Supernova IA can be used as standardisable candles, letting us estimate a redshift-distance relation.
The Pantheon+ sample collected together 1701 light curves of 1550 distinct Type Ia supernovae
This module uses that data set to constrain the distance modulus vs redshift relation.
This version can optionally also include SH0ES HST measurements of H0 from Cepheid variables over 40 years of data.


Assumptions
-----------

 - Pantheon+ statistical and systematic analysis



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - include_shoes
     - bool
     - 
     - Whether to include SH0ES H0 measurements. Note that the parameter name has an o not a zero.
   * - data_file
     - str
     - module_dir/Pantheon+SH0ES.dat
     - Optional. File containing supernova measurements
   * - covmat_file
     - str
     - Pantheon+SH0ES_STAT+SYS.cov_compressed.gz
     - Optional. File containing supernova measurements
   * - x_name
     - str
     - z
     - Datablock name for input theory redshift
   * - y_section
     - str
     - distances
     - Datablock section for input theory distance modulus
   * - y_name
     - str
     - mu
     - Datablock name for input theory distance modulus
   * - like_name
     - str
     - pantheon
     - Named for the saved output likelihood
   * - likelihood_only
     - bool
     - False
     - Skip saving everything except the likelihood.  This prevents you from using e.g. the Fisher matrix sampler but can be faster for quick likelihoods

   * - include_norm
     - bool
     - False
     - Include the normalizing constant at the start of the likelihood.  May be needed when comparing models.


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
     - Redshifts z of calculated theory D_A(z)
   * - 
     - D_A
     - real 1d
     - 
     - Angular diameter distance D_A(z)
   * - supernova_params
     - M
     - real
     - 
     - SN IA absolute magnitude


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - pantheon_like
     - real
     - Gaussian likelihood value of supplied theory mu(z) and M
   * - data_vector
     - pantheon_covariance
     - real 2d
     - Fixed covariance matrix, only if likelihood_only=F
   * - 
     - pantheon_data
     - real 1d
     - Fixed data vector mu_obs, only if likelihood_only=F
   * - 
     - pantheon_simulation
     - real 1d
     - Simulated data vector including simulated noise for e.g. ABC, only if likelihood_only=F
   * - 
     - pantheon_theory
     - real 1d
     - Predicted theory values mu_theory(z_obs) only if likelihood_only=F
   * - 
     - pantheon_chi2
     - real
     - chi^2 value, only if likelihood_only=F


