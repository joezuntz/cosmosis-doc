CRL_Eisenstein_Hu
================================================

Komatsu's CRL code to compute the power spectrum using EH fitting formula.

.. list-table::
    
   * - File
     - structure/crl_eisenstein_hu/nowiggle_module.so
   * - Attribution
     - Komatsu-CRL
   * - URL
     - http://www.mpa-garching.mpg.de/~komatsu/crl/
   * - Citation
     - http://www.mpa-garching.mpg.de/~komatsu/crl/
   * -
     -  Eisenstein and Hu, ApJ, 496, 605 (1998)
   * - Rules
     -


"This module uses Eiichiro Komatsu's CRL code to calculate the power spectrum
without BAO in it following Eisenstein and Hu, ApJ, 496, 605 (1998). 
This is faster but less accurate than a Boltzmann code like CAMB.

The CosmoSIS seam modified this slightly to remove some copyrighted 
N*merical R*cipes code.
"



Assumptions
-----------

 - DEPENDENCIES: You need to run a module to compute the growth rate before this one.



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - zmin
     - real
     - 0.0
     - Min value of redshift to save P(k,z)
   * - zmax
     - real
     - 5.0
     - Max value of redshift to save P(k,z)
   * - nz_steps
     - int
     - 800
     - Number of steps used between zmin-zmax
   * - kmin
     - real
     - 1e-05
     - Min value of k_h (Mpc/h) to save P(k,z)
   * - kmax
     - real
     - 10.0
     - Min value of k_h (Mpc/h) to save P(k,z)
   * - nk_steps
     - int
     - 800
     - Number of steps used between kmin-kmax


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - growth_parameters
     - d_z
     - real 1d
     - 
     - Linear growth factor D(z)
   * - 
     - f_z
     - real 1d
     - 
     - Linear growth rate f(z)
   * - 
     - z
     - real 1d
     - 
     - Redshift of samples
   * - cosmological_parameters
     - omega_b
     - real
     - 
     - Baryon content
   * - 
     - omega_m
     - real
     - 
     - Matter content
   * - 
     - w
     - real
     - -1
     - Dark energy EoS.
   * - 
     - h0
     - real
     - 
     - Hubble/100km/s/Mpc
   * - 
     - n_s
     - real
     - 
     - Scalar spectral index
   * - 
     - n_run
     - real
     - -1
     - Scalar spectral index running.
   * - 
     - a_s
     - real
     - 
     - Primordial amplitude


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - matter_power_no_bao
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - K wavenumbers of samples in Mpc/h
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3


