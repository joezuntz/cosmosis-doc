class
================================================

Boltzmann and background integrator for BG, CMB, matter power, and more

.. list-table::
    
   * - File
     - boltzmann/class/class_interface.py
   * - Attribution
     - Julien Lesgourgues
   * -
     - Thomas Tram
   * -
     - Benjamin Audren
   * -
     - Simon Prunet
   * -
     - Jesus Torrado
   * -
     - Miguel Zumalacarregui
   * -
     - etc
   * - URL
     - http://class-code.net
   * - Citation
     - http://arxiv.org/abs/1104.2932
   * -
     - JCAP 07 (2011) 034
   * -
     - http://arxiv.org/abs/1104.2934
   * -
     - JCAP 09 (2011) 032
   * - Rules
     - You can use CLASS freely, provided that in your publications, you cite at least the paper CLASS II: Approximation schemes. Feel free to cite more CLASS papers!


CLASS is one of the standard cosmology codes for evolving perturbations
in the primordial universe into CMB and other power spectra, as
well as various other quantities. This is a very preliminary interface 
to the general and powerful CLASS code. 

See http://class-code.net for a fuller description and the github repository
https://github.com/lesgourg/class_public for the latest public code.

You should also check out the MontePython sampler code, which uses CLASS
to do similar inference to CosmoSIS.


This version of CLASS has been modified very slightly to be able to output at 
more redshifts and to use the cosmosis build system.

The CosmoSIS team packaged this module into cosmosis form so any issues
running it here please ask us first.


Assumptions
-----------

 - The LCDM model
 - Various choices for approximations and implementations of the Boltzmann and related equations



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - lmax
     - int
     - 2000
     - Max angular frequency ell to use for cmb calculation
   * - kmax
     - int
     - 50.0
     - The max wavenumber k to use for P(k,z) calculation
   * - zmax
     - real
     - 4.0
     - Max redshift to save P(k,z) and distances


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
     - Physical baryon density fraction today, Omega_b * h**2
   * - 
     - omch2
     - real
     - 
     - Physical cdm density fraction today, Omega_c * h**2
   * - 
     - h0
     - real
     - 
     - Hubble parameter H0 / 100 km/s/Mpc
   * - 
     - tau
     - real
     - 
     - Optical depth to last-scattering
   * - 
     - n_s
     - real
     - 
     - Scalar spectral index
   * - 
     - A_s
     - real
     - 
     - Scalar spectrum primordial amplitude
   * - 
     - massless_nu
     - real
     - 3.046
     - Effective number of massless neutrinos
   * - 
     - t_cmb
     - real
     - 2.726
     - The CMB temperature today in Kelvin


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - cosmological_parameters
     - sigma_8
     - real
     - Amplitude of linear matter power at 8/h Mpc at z=0.  Only calculated if mode=all
   * - distances
     - nz
     - int
     - Number of z samples
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
     - age
     - real
     - Age of universe in GYr
   * - 
     - rs_zdrag
     - real
     - Sound horizon size at zdrag. Only if mode!=background
   * - matter_power_lin
     - z
     - real 1d
     - Redshifts of samples. Only if mode=all
   * - 
     - k_h
     - real 1d
     - K wavenumbers of samples in Mpc/h. Only if mode=all
   * - 
     - p_k
     - real 2d
     - Matter power spectrum at samples in (Mpc/h)^-3. Only if mode=all
   * - cmb_cl
     - ell
     - int 1d
     - Angular frequencies. Only if mode=cmb or all
   * - 
     - tt
     - real 1d
     - ell * (ell+1) C_ell^TT / 2 pi in mu K^2. Only if mode=cmb or all
   * - 
     - ee
     - real 1d
     - ell * (ell+1) C_ell^EE / 2 pi in mu K^2. Only if mode=cmb or all
   * - 
     - bb
     - real 1d
     - ell * (ell+1) C_ell^BB / 2 pi in mu K^2. Only if mode=cmb or all
   * - 
     - te
     - real 1d
     - ell * (ell+1) C_ell^TE / 2 pi in mu K^2. Only if mode=cmb or all


