consistency
================================================

Deduce missing cosmological parameters and check consistency

+-------------+----------------------------------------------+
| File        | utility/consistency/consistency_interface.py |
+-------------+----------------------------------------------+
| Attribution | CosmoSIS Team                                |
+-------------+----------------------------------------------+
| URL         |                                              |
+-------------+----------------------------------------------+

There are various ways of parameterizing cosmologies with different advantages
in different contexts.  This module takes a set of cosmological parameters and
tries to use them to deduce the remaining parameters.  For example, if you specify
ombh2 and h then it computes omega_b.  It has a fairly full set of relations to do this.

If you specify inconsistent parameters (e.g. omega values that do not add up to 1)
then an error status is returned.

You can set an option to also calculate the Hubble parameter from the CosmoMC theta
parameter, and vice versa.  This is off by default as it's a little slower.
It uses the camb code directly so should match up.

The standard set of relations is in consistency.py and relates the standard LCDM
parameters, including massive neutrinos.

It also converts log1e10As or A_s_1e9 to A_s, and (S_8, Omega_m) to (sigma_8, Omega_m).


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
   * - cosmomc_theta
     - bool
     - False
     - Whether to add relations that calculate H0 from the CosmoMC theta parameter
   * - relations_file
     - str
     - 
     - Path to an alternative parameter relations file. Relations should be specified in the form 'new_parameter=parameter_b*parameter_b' with one per line.

   * - extra_relations
     - str
     - 
     - Extra relations to be added to the default list. Relations should be specified in the form 'new_parameter=parameter_b*parameter_b,new_parameter2=parameter_d/parameter_e' 



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
   * - 
     - log1e10As
     - real
     - 
     - log (10**10 * A_s) parameter. Ignored if not present
   * - 
     - A_s_1e9
     - real
     - 
     - 10**9 * A_s parameter. Ignored if not present
   * - 
     - S_8
     - real
     - 
     - sigma_8 * (omega_m/0.3)**0.5 parameter. Ignored if not present.


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
   * - 
     - A_s
     - real
     - Amplitude of primordial fluctuations. Only if log1e10As or A_s_1e9 is present on input.
   * - 
     - sigma_8
     - real
     - RMS mass fluctuation in 8 Mpc/h spheres. Only if S_8 is present on input.


