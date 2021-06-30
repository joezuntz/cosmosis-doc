planck_sz
================================================

Prior on sigma_8 * Omega_M ** 0.3 from Planck SZ cluster counts

.. list-table::
    
   * - File
     - likelihood/sz/sz.py
   * - Attribution
     - Planck collaboration (measurement)
   * -
     - CosmoSIS team (code)
   * - URL
     - 
   * - Citation
     - arXiv:1303.5080, Planck 2013 results. XX. Cosmology from Sunyaev-Zeldovich cluster counts
   * - Rules
     - None.


"This small module was written for CosmoSIS.

CMB data like that from Planck can be used to make counts of clusters using
the Sunyaev-Zeldovich effect, in which hot gas in the clusters scatters
CMB photons and causes a decrement (below 217 GHz) or increment (above 217 GHz).

The number of clusters in the universe of a given mass is sensitive to the 
mass density and the overall amount structure in the universe.  The full calculation
is very involved, but in a LCDM universe with some assumptions about Halo behaviour
it can be reduced to a constraint on sigma_8 * Omega_M ** 0.3

"



Assumptions
-----------

 - Planck SZ data
 - SZ signal Y - Mass relation calibrated from X-ray data
 - Flat LCDM
 - Tinker et al halo distribution



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - measured_value
     - real
     - 0.764
     - Replace the standard value measurement sigma_8 * Omega_M ** 0.3 = 0.764 with a custom one for simulations


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
     - omega_m
     - real
     - 
     - Matter density fraction at redshift 0
   * - 
     - sigma_8
     - real
     - 
     - Matter fluctuation dispersion down to 8 Mpc/h


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - likelihoods
     - SZ_LIKE
     - real
     - Gaussian likelihood value of supplied parameters


