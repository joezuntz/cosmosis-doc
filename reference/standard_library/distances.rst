distances
================================================

Output cosmological distance measures for dynamical dark energy

.. list-table::
    
   * - File
     - background/dynamical_de_distances/distances.py
   * - Attribution
     - CosmoSIS team (code)
   * - URL
     - 
   * - Citation
     - Linder, E.V. 2003. Phys. Rev. Lett. 90:091301
   * -
     - Huterer, D., Turner, M.S. 2001. Phys. Rev. D64:123527
   * -
     - Wetterich, C. 2004 Physics Letters B, Volume 594
   * - Rules
     - None.


This small module was written for CosmoSIS. This module computes the angular diameter distance, luminosity distance,
and distance modulus for three different parametrisations of dark energy. w = w0 +(1-a)wa, w = w0+(ap-a)wa and and 2 parameter
EDE w(a) model from Wetterich 2004.


Assumptions
-----------

None



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - verbose
     - bool
     - False
     - Whether to provide additional feedback
   * - w_model
     - int
     - 0
     - Model choice. 0 for (w0,wa), 1 for (w0,wa,ap), 2 for EDE model (w0,ode_e)
   * - zmin
     - real
     - 0.0
     - The minimum redshift at which to calculate the distance
   * - zmax
     - real
     - 0.0
     - The maximum redshift at which to calculate the distance
   * - dz
     - real
     - 0.01
     - The spacing between output redshift samples


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
     - Hubble parameter H0 / (100 km/s/Mpc)
   * - 
     - omega_k
     - real
     - 0.0
     - Curvature density fraction today
   * - 
     - omega_b
     - real
     - 
     - Baryon density fraction today
   * - 
     - omega_c
     - real
     - 
     - CDM density fraction today
   * - 
     - w0
     - real
     - -1.0
     - Equation of state w(z=0) of dark energy
   * - 
     - wa
     - real
     - 0.0
     - Equation of state parameter w(a) = w_0 + w_a*(1-a)
   * - 
     - ap
     - real
     - 
     - Pivot scale factor w(a) = w_0 + w_a*(ap-a)
   * - 
     - ode_e
     - real
     - 
     - Early dark energy parameter


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - distances
     - nz
     - int
     - Number of background z samples
   * - 
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - d_a
     - real 1d
     - Angular diameter distance in Mpc
   * - 
     - d_m
     - real 1d
     - Co-moving distance in Mpc
   * - 
     - d_l
     - real 1d
     - Luminosity distance in Mpc
   * - 
     - mu
     - real 1d
     - Distance modulus


