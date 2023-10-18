act-dr6-lens
================================================

CMB Lensing from ACT DR6 data.

+-------------+------------------------------------------------------------+
| File        | likelihood/act-dr6-lens/act_dr6_lenslike_interface.py      |
+-------------+------------------------------------------------------------+
| Attribution | Mat Madhavacheril, ACT Collaboration (Library)             |
+-------------+------------------------------------------------------------+
|             | Ian Harrison, David Dzingeleski, CosmoSIS Team (Interface) |
+-------------+------------------------------------------------------------+
| URL         | https://github.com/ACTCollaboration/act_dr6_lenslike       |
+-------------+------------------------------------------------------------+
| Citations   | https://doi.org/10.48550/arXiv.2304.05203                  |
+-------------+------------------------------------------------------------+
|             | https://doi.org/10.48550/arXiv.2304.05202                  |
+-------------+------------------------------------------------------------+

This is the lensing likelihood from the ACT DR6 data release. What is supplied here is only the CosmoSIS interface
to the standalone act_dr6_lenslike python module. This should be obtainable through running: pip install act_dr6_lenslike.


Assumptions
-----------

 - act_dr6_lenslike python module
 - ACT DR6 lensing data



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_directory
     - str
     - [module dir]/data
     - Directory to search for data
   * - variant
     - str
     - act_baseline
     - The variant of the DR6 lensing likelihood to use. Options are act_baseline, act_extended, actplanck_baseline, actplanck_extended, act_polonly, act_cibdeproj, act_cinpaint
   * - lens_only
     - bool
     - False
     - If False then a covariance matrix will be used which has been CMB marginalized.
   * - like_only
     - bool
     - False
     - If set to True then only the likelihood will be stored. If True then the lensing theory spectra calculated by the likelihood will be saved to the CosmoSIS data block, along with the data, covariance and inverse covariance.
   * - mock
     - bool
     - False
     - If True, use a set of simulated Cls at default DR6 accuracy instead of the data.
   * - nsims_act
     - int
     - 792
     - The number of simulations used to create the ACT portion of the covariance matrix.
   * - nsims_planck
     - int
     - 400
     - The number of simulations used to create the Planck portion of the covariance matrix.
   * - like_corrections
     - bool
     - True
     - If set to True, will apply appropriate likelihood norm corrections.
   * - trim_lmax
     - int
     - 2998
     - Maximum L to use from the lensing kk spectra.
   * - apply_hartlap
     - bool
     - True
     - Choose whether to apply a Hartlap correction to the covariance matrix.
   * - scale_cov
     - str
     - 
     - A value /as a string/ by which to scale the covariance matrix by a given value (for e.g. making forecasts).
   * - varying_cmb_alens
     - bool
     - False
     - Whether or not to divide the lensing theory spectrum by an A_lens parameter, if one is being used.


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - cmb_cl
     - ell
     - real 1d
     - 
     - CMB power spectrum ell values of other inputs
   * - 
     - tt
     - real 1d
     - 
     - Lensed CMB temperature power spectrum in ell(ell+1)/2pi units
   * - 
     - te
     - real 1d
     - 
     - Lensed CMB temperature-E-mode polarization cross power spectrum in ell(ell+1)/2pi units
   * - 
     - ee
     - real 1d
     - 
     - Lensed CMB E-mode polaration power spectrum in ell(ell+1)/2pi units
   * - 
     - bb
     - real 1d
     - 
     - Lensed CMB B-mode polaration power spectrum in ell(ell+1)/2pi units
   * - 
     - pp
     - real 1d
     - 
     - CMB lensing phi-phi power spectrum in ell(ell+1)/2pi units


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - act_dr6_lens_like
     - real
     - ACT DR6 lensing likelihood for given selection
   * - data_vector
     - act_dr6_lens_data
     - real 1d
     - Binned CLkk data, only if like_only=False
   * - 
     - act_dr6_lens_covariance
     - real 2d
     - Used covariance matrix, only if like_only=False
   * - 
     - act_dr6_lens_inverse_covariance
     - real 2d
     - Used inverse covariance matrix, only if like_only=False


