wmap
================================================

Likelihood function of CMB from WMAP

.. list-table::
    
   * - File
     - likelihood/wmap9/wmap_interface.so
   * - Attribution
     - The WMAP Collaboration
   * - URL
     - 
   * - Citation
     - Hinshaw et al, ApJS, 208, 2, 19, 25
   * - Rules
     - "Likelihood released by WMAP Collaboration and packaged by cosmosis team.   Contact the latter with problems in the first instance. "



"The Wilkinson Microwave Anisotropy Probe measured the temperature
and polarization of the CMB over the full sky in the K, Ka, Q, V, and W
microwave bands.  

The WMAP produced this likelihood code, which takes in theory spectra
for TT, EE, BB, and TE spectra and compares it to WMAP data.

The method used for the likelihood is different in different ell regimes
and for different spectra.
"



Assumptions
-----------

 - WMAP 9 year data



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
     - int 1d
     - 
     - Integer vector of angular frequencies for CMB spectra
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


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - likelihoods
     - wmap9_like
     - real
     - Combined log-likelihood from all WMAP components


