extrapolate
================================================

Simple log-linear extrapolation of P(k) to high k

+-------------+--------------------------------------------+
| File        | boltzmann/extrapolate/extrapolate_power.py |
+-------------+--------------------------------------------+
| Attribution | CosmoSIS Team                              |
+-------------+--------------------------------------------+
| URL         | https://bitbucket.org/joezuntz/cosmosis    |
+-------------+--------------------------------------------+

It is sometimes useful to extend matter power spectra P(k) to high values
of k. These values are unphysical but are useful for numerical stability.

This module does a simple linear extrapolation in log-log space of P(k)
out to a specified kmin and kmax.  If the data already extends that far then
it does not do anything.

It tries both linear and non-linear spectra but does not complain if either or 
both are not present.


Assumptions
-----------

 - Linear extrapolation in log-space of P(k); this is not a great approximation



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - kmax
     - real
     - 
     - The max wavenumber k to extrapolate to
   * - kmin
     - real
     - 1.0e10
     - The min wavenumber k to extrapolate to (default is high enough for no extrapolation)
   * - nmin
     - int
     - 50
     - The number of points to add at low k
   * - nmax
     - int
     - 200
     - The number of points to add at high k
   * - npoint
     - int
     - 3
     - The number of end k-samples to use to fit the slope at the end


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - matter_power_lin
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - 
     - Inpu k wavenumbers of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - 
     - Matter power spectrum at samples in (Mpc/h)^-3.
   * - matter_power_nl
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - 
     - Inpu k wavenumbers of samples in Mpc/h.
   * - 
     - p_k
     - real 2d
     - 
     - Matter power spectrum at samples in (Mpc/h)^-3.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - matter_power_lin
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - Inpu k wavenumbers of samples in Mpc/h, extended to kmax
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3, extended to kmax
   * - matter_power_nl
     - z
     - real 1d
     - Redshifts of samples
   * - 
     - k_h
     - real 1d
     - Inpu k wavenumbers of samples in Mpc/h, extended to kmax
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3, extended to kmax


