BBN
================================================

Simple prior on Omega_b h^2 from light element abundances

.. list-table::
    
   * - File
     - likelihood/bbn/bbn_ombh2.py
   * - Attribution
     - B.D Fields
   * -
     - P. Molaro
   * -
     - S. Sarkar
   * - URL
     - http://pdg.lbl.gov/2013/reviews/rpp2013-rev-bbang-nucleosynthesis.pdf
   * - Citation
     - J. Beringer et al. (Particle Data Group), Phys. Rev. D86, 010001 (2012)
   * - Rules
     - None.


"This small module was written for CosmoSIS.

Measurements of the abundances of light elements D, 3He, 4He, and 7Li
constrain the density budget at the epoch of nucleosynthesis in the first
three minutes after the big bang.
"



Assumptions
-----------

 - Standard model of Big-Bang nucleosynthesis



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
     - 0.023
     - Replace the standard value measurement omega_b h^2 = 0.023 with a custom one
   * - sigma
     - real
     - 0.002
     - Replace the standard value error 0.002 with a custom one


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
     - omega_b
     - real
     - 
     - Baryon density fraction today
   * - 
     - h0
     - real
     - 
     - Hubble parameter H0/(100 km/s/Mpc)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - BBN_LIKE
     - real
     - Gaussian likelihood value of supplied parameters


