JulloLikelihood
================================================

Likelihood of Jullo et al (2012) measurements of a galaxy bias sample

.. list-table::
    
   * - File
     - likelihood/jullo_bias/jullo.py
   * - Attribution
     - Lucy Clerkin
   * -
     - CosmoSIS Team
   * - URL
     - http://www.sdss3.org
   * - Citation
     - http://arxiv.org/abs/1202.6491
   * - Rules
     -


Galaxy bias refers to the relative density of galaxies compared to underlying dark matter,
and can be a function of scale and/or redshift.

Jullo et al made measurements of galaxy bias for high and low mass samples.

This module compares a predicted b(z) or b(k,z) from theory to these measurements.



Assumptions
-----------

 - COSMOS survey galaxy samples



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - mass
     - str
     - 
     - Low or high.  Choose which Jullo sample to work with


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - bias_field
     - z
     - real 1d
     - 
     - Redshift of bias samples
   * - 
     - k_h
     - real 1d
     - 
     - Wavenumber of samples in k_h. If not present then b(z) only is assumed
   * - 
     - b
     - real 1d or real 2d
     - 
     - Bias as a function of either k and z or just z


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - likelihoods
     - JULLO_LIKE
     - real
     - Likelihood of supplied bias model


