Cluster_mass
================================================

Likelihood of z=1.59 Cluster mass from Santos et al. 2011

.. list-table::
    
   * - File
     - likelihood/cluster_mass/cluster_mass.py
   * - Attribution
     - Santos et al. 2011 (measurement)
   * -
     - Harrison & Coles 2012
   * -
     - CosmoSIS team (code)
   * - URL
     - 
   * - Citation
     - Santos et al. 2011 
   * -
     - Harrison & Coles 2012 
   * - Rules
     -


"This small module was written for CosmoSIS.
    The Extreme Value statistics module (evs) should be run in the pipeline prior to this module.
"



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
   * - mean
     - real
     - 
     - Mass in M_sun/h
   * - sigma
     - real
     - 
     - Error in M_sun/h


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - clusters
     - M_max
     - real
     - 
     - Mass (M_sun/h)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - likelihoods
     - MAXMASS_LIKE
     - real
     - Gaussian likelihood value of supplied parameters


