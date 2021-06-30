BICEP2
================================================

Compute the likelihood of the supplied CMB power spectra

.. list-table::
    
   * - File
     - likelihood/bicep2/bicep_interface.py
   * - Attribution
     - BICEP2 Team
   * - URL
     - http://bicepkeck.org
   * - Citation
     - http://arxiv.org/abs/1403.4302
   * -
     - http://arxiv.org/abs/1403.3985
   * - Rules
     -


"The 2014 BICEP2 results are a detection of cosmological B-modes
on the scales that indicate a primordial gravitational wave bump.

This module wraps the likelihood code released by the BICEP2 team.

WARNING: The BICEP 2014 results are generally considered to be incorrect;
this module is for historical interest only.

"



Assumptions
-----------

 - CAMB or other CMB code must be set up to do lensing and include high k modes
 - BICEP2 2014-03-14 dataset



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description


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
     - Angular wavenumbers for the input spectra
   * - 
     - EE
     - real 1d
     - 
     - EE CMB power spectrum, at wavenumbers from ell
   * - 
     - BB
     - real 1d
     - 
     - BB CMB power spectraum, at wavenumbers from ell


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - likelihoods
     - BICEP_LIKe
     - real
     - Likelihood of supplied spectra from BICEP2


