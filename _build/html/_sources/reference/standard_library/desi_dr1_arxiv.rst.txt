desi_dr1_arxiv
================================================

DESI BAO likelihood from DR1 data

+-------------+---------------------------------------------------+
| File        | likelihood/bao/desi1-dr1-arxiv/desi1_dr1_arxiv.py |
+-------------+---------------------------------------------------+
| Attribution | DESI Team (data)                                  |
+-------------+---------------------------------------------------+
|             | CosmoSIS Team (module)                            |
+-------------+---------------------------------------------------+
| URL         | https://www.desi.lbl.gov/                         |
+-------------+---------------------------------------------------+
| Citations   | https://arxiv.org/abs/2404.03002                  |
+-------------+---------------------------------------------------+

The DESI DR1 release provided measurements of the sound horizon imprint on
galaxy and quasar clustering, and the Lyman alpha forest. This module
provides a likelihood for these measurements, assuming a Gaussian likelihood
for the data, as presented in the DESI DR1 arXiv paper.


Assumptions
-----------

 - DESI reconstruction and measurements of BAO data
 - Gaussian likelihood



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - desi_data_sets
     - None
     - str
     - Choice of which DESI data set(s) to include. Comma-separated string of choices from: BGS LRG1 LRG2 LRG3+ELG1 ELG2 QSO Lya QSO


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
     - rs_zdrag
     - real
     - 
     - Sound horizon at drag epoch of last scattering
   * - 
     - z
     - real 1d
     - 
     - Sample points in redshift of distance theory prediction
   * - 
     - d_v
     - real 1d
     - 
     - Angular average of comoving angular diameter and line of sight distance in Mpc
   * - 
     - d_m
     - real 1d
     - 
     - Co-moving distance in Mpc
   * - 
     - h
     - real 1d
     - 
     - Hubble parameter as function of distance in units of Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - desi_bao_like
     - real
     - Gaussian likelihood value.
   * - data_vector
     - desi_bao_data
     - real 1d
     - The full vector of data points used in the likelihood
   * - 
     - desi_bao_theory
     - real 1d
     - The full vector of theory points used in the likelihood
   * - 
     - desi_bao_covariance
     - real 2d
     - The covariance matrix used
   * - 
     - desi_bao_inverse_covariance
     - real 2d
     - The inverse covariance matrix (precision matrix) used.
   * - 
     - desi_bao_simulation
     - real 1d
     - A simulated data set from the given theory and covariance matrix.
   * - 
     - desi_bao_chi2
     - real
     - Chi-squared value for the data and theory
   * - 
     - desi_bao_n
     - int
     - Number of data points used


