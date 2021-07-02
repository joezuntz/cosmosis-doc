fgas
================================================

Likelihood of galaxy cluster gas-mass fractions

.. list-table::
    
   * - File
     - likelihood/fgas/fgas.so
   * - Attribution
     - Adam Mantz
   * - URL
     - http://www.slac.stanford.edu/~amantz/work/fgas14/
   * - Citation
     - Mantz et al., MNRAS, 440:2077 (2014)
   * -
     - http://arxiv.org/abs/1402.6212
   * - Rules
     - MIT license


Cluster gas mass fractions are a standard quantity whose value is related
to the cosmic baryon mass fraction and whose apparent evolution depends
on the expansion of the Universe.



Assumptions
-----------





Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - numdatasets
     - int
     - 0
     - Number of fgas data tables
   * - dataset{N}
     - str
     - 
     - Path to each data file, with N=1,2,...
   * - cl_cal_mean
     - real
     - 0.9
     - Mean of a Gaussian prior to be applied to the fgas calibration nuisance parameter. This will be deprecated once the gravitational lensing data that we use to direcly constrain this parameter are included in a future version.
   * - cl_cal_sd
     - real
     - 0.09
     - Standard deviation of a Gaussian prior to be applied to the fgas calibration nuisance parameter. This will be deprecated once the gravitational lensing data that we use to direcly constrain this parameter are included in a future version.
   * - fgas_rslope_mean
     - real
     - 0.442
     - Mean of a Gaussian prior to be applied to the power-law slope of the cluster fgas profile.
   * - fgas_rslope_sd
     - real
     - 0.035
     - Standard deviation of a Gaussian prior to be applied to the power-law slope of the cluster fgas profile.
   * - cl_lenssys_mean
     - real
     - 1.0
     - Mean of a Gaussian prior to be applied to the weak lensing calibration nuisance parameter.
   * - cl_lenssys_sd
     - real
     - 0.069
     - Standard deviation of a Gaussian prior to be applied to the weak lensing calibration nuisance parameter.


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - cosmological_parameters
     - baryon_fraction
     - real
     - 
     - Cosmic baryon mass fraction
   * - 
     - yhe
     - real
     - 
     - Primordial helium mass fraction
   * - distances
     - z
     - real 1d
     - 
     - Redshift
   * - 
     - D_A
     - real 1d
     - 
     - Angular diameter distance
   * - 
     - D_L
     - real 1d
     - 
     - Luminosity distance
   * - 
     - H
     - real 1d
     - 
     - Hubble parameter
   * - fgas
     - U_gas_0
     - real
     - 
     - Redshift-zero value of fgas, normalized to the cosmic baryon fraction
   * - 
     - U_gas_1
     - real
     - 
     - Linear-with-redshift evolution of fgas
   * - 
     - fgas_scatter
     - real
     - 
     - Log-normal intrinsic scatter in fgas
   * - 
     - fgas_rslope
     - real
     - 
     - Power-law slope of the cluster fgas profile
   * - 
     - cl_cal
     - real
     - 
     - Calibration nuisance parameter
   * - 
     - cl_calev
     - real
     - 
     - Linear-in-redshift evolution of the calibration
   * - 
     - cl_calscat
     - real
     - 
     - Intrinsic scatter in the calibration (e.g. due to non-thermal pressure)
   * - 
     - cl_lenssys
     - real
     - 
     - Nuisance parameter for weak graviational lensing masses
   * - 
     - cl_lnMwl_{N}
     - real
     - 
     - With N=1,2,...,12 log masses for the clusters where we have gravitational lensing data


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - fgas_like
     - real
     - Likelihood of the galaxy cluster gas-mass fractions


