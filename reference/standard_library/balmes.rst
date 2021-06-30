balmes
================================================



.. list-table::
    
   * - File
     - strong_lensing/balmes_corasaniti/balmes.py
   * - Attribution
     - I. Balmes & P.S. Corasaniti
   * - URL
     - 
   * - Citation
     - arXiv:1206.5801 
   * - Rules
     - Please cite the relevant papers if you use this module.


"
Balmes & Corasaniti measured H0 using strong lensing systems.

This module uses a likelihood tabulated from their paper.
 "



Assumptions
-----------

 - Strong lensing modelling details



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
     - modue_dir/balmes.txt
     - Dir for data files. Data file containing 2 columns H0 and P. You should use the file taken from arXiv:1206.5801 and provided in CosmoSIS under the name balmes.txt unless you want to use a different dataset


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
     - h0
     - real
     - 
     - Hubble parameter/100 km/s/Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - likelihoods
     - balmes_sl_like
     - real 1d
     - Likelihood of this strong lensing system given h0


