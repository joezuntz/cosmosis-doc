add_intrinsic
================================================

Sum together intrinsic aligments with shear signal

.. list-table::
    
   * - File
     - shear/add_intrinsic/add_intrinsic.py
   * - Attribution
     - CosmoSIS team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     -


Observerd shape spectra contain a sum of intrinsic and shear spectra, and the
cross-correlation between them.  This module adds together these components,
accounting for the fact that C_GI != C_IG for two bins

It may be replaced at some point with changes to the shear computation modules.


Assumptions
-----------

 - Linear sum of C_ell for IA components



Setup Parameters
----------------

None


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - shear_cl_gg
     - nbin
     - int
     - 
     - Number of tomographic bins
   * - 
     - ell
     - real 1d
     - 
     - ell samples of theory
   * - 
     - bin_{i}_{j}
     - real 1d
     - 
     - Shear-shear angular spectra C_ell for pairs of i,j values
   * - shear_cl_ii
     - bin_{i}_{j}
     - real 1d
     - 
     - Intrinsic-intrinsic angular spectra for pairs of i,j values C_ell
   * - shear_cl_gi
     - bin_{i}_{j}
     - real 1d
     - 
     - Shear-intrinsic angular spectra for pairs of i,j values C_ell
   * - 
     - bin_{j}_{i}
     - real 1d
     - 
     - Intrinsic-shear angular spectra for pairs of i,j values C_ell


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - shear_cl
     - nbin
     - int
     - Number of tomographic bins
   * - 
     - ell
     - real 1d
     - ell samples of theory
   * - 
     - bin_{i}_{j}
     - real 1d
     - Total angular spectra C_ell for pairs of i,j values


