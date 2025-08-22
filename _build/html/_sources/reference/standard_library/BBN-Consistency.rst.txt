BBN-Consistency
================================================

Compute consistent Helium fraction from baryon density given BBN

+-------------+--------------------------------------------+
| File        | utility/bbn_consistency/bbn_consistency.py |
+-------------+--------------------------------------------+
| Attribution | CosmoSIS Team                              |
+-------------+--------------------------------------------+
| URL         | http://parthenope.na.infn.it/              |
+-------------+--------------------------------------------+
| Citations   | Comp.Phys.Commun.178:956-971,2008          |
+-------------+--------------------------------------------+


The Big Bang Nucleosynthesis model describes how the 
light elements were generated in the primordial universe.  For a given
value of Omega_b h**2 and number of neutrinos the theory can predict
the helium abundance.

This module sets the helium mass fraction (YHe) from the mean baryon density (ombh2)
and number of neutrinos (delta_neff), based on a table interpolation from those calculations.

This module should go into the pipeline after consistency and
before any physics modules. It's effectively an optional consistency module.




Assumptions
-----------

 - Standard Big Bang Nucleosynthesis
 - ombh2 within the range of the input data



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data
     - str
     - included
     - Filename for ombh2,DeltaN,YHe data. ( file)
   * - input_name
     - str
     - delta_neff
     - Which parameter to start from, either massless_nu or delta_neff


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
     - ombh2
     - real
     - 
     - Physical matter density parameter
   * - 
     - delta_neff
     - real
     - 0.0
     - Extra contribution to neutrino number density (if input_name == delta_neff)
   * - 
     - massive_nu
     - real
     - 
     - Effective number of massive neutrinos (if input_name == massless_nu)
   * - 
     - massless_nu
     - int
     - 
     - Number of massless neutrinos (if input_name == massless_nu)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - cosmological_parameters
     - yhe
     - real
     - Cosmological helium fraction


