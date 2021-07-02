consistency
================================================

Deduce missing cosmological parameters and check consistency

.. list-table::
    
   * - File
     - utility/consistency/consistency_interface.py
   * - Attribution
     - CosmoSIS Team
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - Please maintain attribution.


"There are various ways of parameterizing cosmologies with different advantages
in different contexts.  This module takes a set of cosmological parameters and
tries to use them to deduce the remaining parameters.  For example, if you specify
ombh2 and h then it computes omega_b.  It has a fairly full set of relations to do this.

If you specify inconsistent parameters (e.g. omega values that do not add up to 1)
then an error status is returned.

The following relations are used:

omega_m = ommh2/h/h

omega_b = ombh2/h/h

omega_c = omch2/h/h

omega_nu = omnuh2/h/h

ommh2 = omega_m*h*h

ombh2 = omega_b*h*h

omch2 = omega_c*h*h

omnuh2 = omega_nu*h*h

omch2 = ommh2-ombh2

ommh2 = omch2+ombh2

baryon = omega_b/omega_m

omega_b = omega_m*baryon_fraction

omega_m = omega_b/baryon_fraction

baryon_fraction = ombh2/ommh2

ombh2 = ommh2*baryon_fraction

ommh2 = ombh2/baryon_fraction

omega_m = omega_b+omega_c

h = hubble/100

hubble = h*100

omega_lambda = 1-omega_m-omega_k-omega_nu

omega_m = 1-omega_lambda-omega_k-omega_nu

omega_k = 1-omega_m-omega_lambda-omega_nu

omega_nu = 1-omega_m-omega_lambda-omega_k"



Assumptions
-----------

 - LCDM parameterization
 - First pass: tries no assumptions
 - Second pass: tries omega_nu=0
 - Third pass: tries omega_nu=0 and omega_k=0



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
     - Whether to print how derived parameters were calculated and what assumptions used


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
     - Matter density fraction of critical
   * - 
     - omega_b
     - real
     - 
     - Baryon density fraction of critical
   * - 
     - omega_c
     - real
     - 
     - CDM density fraction of critical
   * - 
     - omega_k
     - real
     - 
     - Curvature pseudo-density fraction of critical
   * - 
     - omega_nu
     - real
     - 
     - Massive neutrino density fraction of critical
   * - 
     - omega_lambda
     - real
     - 
     - Dark energy density fraction of critical
   * - 
     - ommh2
     - real
     - 
     - Physical density omega_m * h^2
   * - 
     - ombh2
     - real
     - 
     - Physical density omega_b * h^2
   * - 
     - omch2
     - real
     - 
     - Physical density omega_c * h^2
   * - 
     - omnuh2
     - real
     - 
     - Physical density omega_nu * h^2
   * - 
     - baryon_fraction
     - real
     - 
     - Ratio omega_b/omega_m
   * - 
     - hubble
     - real
     - 
     - Hubble parameter H_0 in km/s/Mpc
   * - 
     - h
     - real
     - 
     - Dimensionless Hubble h = H_0 / 100 km/s/Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - cosmological_parameters
     - omega_m
     - real
     - Matter density fraction of critical
   * - 
     - omega_b
     - real
     - Baryon density fraction of critical
   * - 
     - omega_c
     - real
     - CDM density fraction of critical
   * - 
     - omega_k
     - real
     - Curvature pseudo-density fraction of critical
   * - 
     - omega_nu
     - real
     - Massive neutrino density fraction of critical
   * - 
     - omega_lambda
     - real
     - Dark energy density fraction of critical
   * - 
     - ommh2
     - real
     - Physical density omega_m * h^2
   * - 
     - ombh2
     - real
     - Physical density omega_b * h^2
   * - 
     - omch2
     - real
     - Physical density omega_c * h^2
   * - 
     - omnuh2
     - real
     - Physical density omega_nu * h^2
   * - 
     - baryon_fraction
     - real
     - Ratio omega_b/omega_m
   * - 
     - hubble
     - real
     - Hubble parameter H_0 in km/s/Mpc
   * - 
     - h
     - real
     - Dimensionless Hubble h = H_0 / 100 km/s/Mpc


