pantheon
================================================

Likelihood of the Pantheon supernova analysis

.. list-table::
    
   * - File
     - likelihood/pantheon/pantheon.py
   * - Attribution
     - Scolnic et al (measurement)
   * -
     - CosmoSIS team (code)
   * - URL
     - http://dx.doi.org/10.17909/T95Q4X
   * - Citation
     - Scolnic et al, ApJ, 859, 28
   * - Rules
     - None.


" Supernova IA can be used as standardisable candles,
letting us estimate a redshift-distance relation.

The Pantheon sample collected together a combined SN IA
sample from the Pan-Starrs1, Medium Deep Survey, SDSS,
SNLS, and various HST data sets into a joint analysis.

This module uses that data set to constrain the distance modulus
vs redshift relation.

There are two Pantheon data variants - this version uses the
compressed (binned) version since it is much smaller and faster
to use and produces nearly identical results to the full version.
You can separately download and use the full version files if you
wish.

The Pantheon data release was analyzed with a much more complex code
in CosmoMC, but almost all of the machinery in that code was unusued,
because the various systematic effects that it implements were subsumed
into a single systematic covariance matrix.  This code therefore omits
that machinery for simlicitiy.
"



Assumptions
-----------

 - Pantheon statistical and systematic analysis



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
     - module_dir/lcparam_DS17f.txt
     - Optional. File containing supernova measurements
   * - covmat_file
     - str
     - module_dir/lcparam_DS17f.txt
     - Optional. File containing supernova measurements
   * - x_section
     - str
     - distances
     - Datablock section for input theory redshift
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
     - Redshifts of calculated theory mu(z)
   * - 
     - mu
     - real 1d
     - 
     - Distance modulus mu(z) at given redshifts
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


