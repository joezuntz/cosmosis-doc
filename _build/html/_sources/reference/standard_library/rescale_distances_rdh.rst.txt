rescale_distances_rdh
================================================

Rescale computed distances to be consistent with a given value of R_d * h

+-------------+--------------------------------------------------------+
| File        | utility/rescale_distances_rdh/rescale_distances_rdh.py |
+-------------+--------------------------------------------------------+
| Attribution | CosmoSIS Team                                          |
+-------------+--------------------------------------------------------+
| URL         |                                                        |
+-------------+--------------------------------------------------------+

BAO people sometimes sample using the best-constrained BAO parameter r_d * h,
where r_d is the sound horizon at the drag epoch (last scattering). This module
takes a set of distances and rescales them to be consistent with a given value of
r_d * h. This is useful for replicating, for example, the DESI BAO-only analysis.

For that reason this module is limited to rescale distances, and not, for example.
k values in a power spectrum.

In general I'd discourage people from sampling in whatever is the best-constrained
parameter for their particular analysis - it doesn't correspond to particularly
sensible priors in any other parametrization. But it can make sampling more efficient,
depending on the sampler.

Specifically, this module reads a value of rd_prime computed from a (fixed) value
of H0, e.g. by camb, and a sampled rdh_sample value, from which it computes
rd_sample = rdh_sample / h_fid. It then sets f = rd_prime / rd_sample, and muliplies
all the distance metrics by f.  H(z) is also rescaled by 1/f, and mu(z) adjust accordingly too.

This module is not intended to be used in a general way, but only in the context of
the specific BAO analysis described above.


Assumptions
-----------

 - FLRW



Setup Parameters
----------------

None


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
     - Fiducial value of H0 in km/s/Mpc/100. Should be fixed
   * - 
     - rdh
     - real
     - 
     - Sample value of R_d * h in km/s.
   * - distances
     - rs_zdrag
     - real
     - 
     - Sound horizon at drag epoch computing using fiducial h0, in Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - cosmological_parameters
     - h0
     - real
     - Updated h0
   * - distances
     - D_L
     - real 1d
     - Updated luminosity distance in Mpc
   * - 
     - D_A
     - real 1d
     - Updated angular diameter distance in Mpc
   * - 
     - D_V
     - real 1d
     - Updated BAO average distance in Mpc
   * - 
     - D_M
     - real 1d
     - Updated line of sight comoving distance in Mpc
   * - 
     - D_C
     - real 1d
     - Updated transverse comoving distance in Mpc
   * - 
     - H
     - real 1d
     - Updated Hubble parameter in km/s/Mpc
   * - 
     - mu
     - real 1d
     - Updated distance modulus
   * - 
     - rs_zsrag
     - real
     - Sound horizon at drag epoch computing using updated h0, in Mpc
   * - 
     - h0rd
     - real
     - Final value of h0 r_d, using updated h0


