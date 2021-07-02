planck2018
================================================

Likelihood function of CMB from Planck 2015 data

.. list-table::
    
   * - File
     - likelihood/planck2018/planck_interface.so
   * - Attribution
     - The Planck Collaboration
   * - URL
     - 
   * - Citation
     - Planck collaboration, Aghanim et al, arXiv:1907.12875
   * - Rules
     - "Likelihood released by Planck Collaboration and packaged by cosmosis team.   Contact the latter with problems in the first instance.  Different papers should be cited depending which data sets are used with this module. "



The Planck space telescope has provided the most powerful current
 CMB data from quadrupole to sub-degree scales.

 The Planck Collaboration released a likelihood code (the PLC) to which one passes
 both a file containing the data to be used, the theory spectra to compare to that 
 data, and a set of nuisance parameters that the code uses (somewhat opaquely) to 
 model the effects of foreground components, secondary anisotropies, and Planck beams and 
 gains.  For more details see the papers by the Planck collaboration and web documentation.

 https://pla.esac.esa.int/#cosmology

 We do not describe the nuisance parameters in detail here; reasonable ranges and values
 for them are given in the Planck papers; they should be marginalized over in full
 analysis.  Different parameters are used for different data sets.

 The cosmosis team wrote the wrapper which connects the PLC into
 cosmosis.

 Important caveats about which likelihood files you can use together, and what priors
 you should use on nuisance parameters, are available here:
 https://wiki.cosmos.esa.int/planck-legacy-archive/index.php/CMB_spectrum_%26_Likelihood_Code

 This version contains a different version of the same fix developed for the 3.01 release.



Assumptions
-----------

 - Highly accurate CMB calculations are required
 - In the high-ell regime models for the foregrounds and secondary anisotropies are assumed
 - Planck foreground models



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_1
     - str
     - 
     - File path to a Planck likelihood (clik/plik) file. Need at least one of lensing_1 or data_1.
   * - data_2
     - str
     - 
     - Additional likelihood files.  data_3, etc. are allowed
   * - lensing_1
     - str
     - 
     - File path to a Planck lensing likelihood (clik/plik) file. Need at least one of lensing_1 or data_1.
   * - lensing_2
     - str
     - 
     - Additional lensing files.  lensing_3, etc. are allowed.
   * - save_separate_likelihoods
     - bool
     - False
     - If true, save planck_like_1, planck_like_2, etc as well as the total. Note that this means you should explicitly set which likelihoods are included in the parameter file.


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
     - int 1d
     - 
     - Angular frequencies for CMB spectra
   * - 
     - tt
     - real 1d
     - 
     - Temperature spectra in l*(l+1) C_ell / uK^2 (if using TT data)
   * - 
     - ee
     - real 1d
     - 
     - E-mode polarization spectra in l*(l+1) C_ell / uK^2 (if using pol data)
   * - 
     - bb
     - real 1d
     - 
     - B-mode polarization spectra in l*(l+1) C_ell / uK^2 (if using pol data)
   * - 
     - te
     - real 1d
     - 
     - Cross spectra in l*(l+1) C_ell / uK^2 (if using pol data)
   * - 
     - pp
     - real 1d
     - 
     - phi-phi spectra in l*(l+1) C_ell (if using lensing)
   * - planck
     - nuisance_parameters
     - real
     - 
     - Various nuisance parameters are accepted depending on the likelihood file.  See Planck documentation or try running on an file and missing ones will be reported.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - planck_1_like
     - real
     - Only if data_1 specified and save_separate_likelihoods. Log-likelihood from first file
   * - 
     - planck_2_like
     - real
     - Only if data_2 specified and save_separate_likelihoods. Log-likelihood from second file.  Can also get planck_3_like etc.
   * - 
     - planck_lensing_1_like
     - real
     - Only if lensing_1 specified and save_separate_likelihoods. Log-likelihood from first lensing file.
   * - 
     - planck_lensing_2_like
     - real
     - Only if lensing_2 specified and save_separate_likelihoods. Log-likelihood from second lensing file.  Can also get planck_lensing_3_like etc.
   * - 
     - planck2018_like
     - real
     - Sum of all Planck log-likelihoods


