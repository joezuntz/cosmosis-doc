strong_lens_time_delays
================================================



.. list-table::
    
   * - File
     - strong_lensing/time_delay_lenses/time_delay_interface.py
   * - Attribution
     - Bonvin et al, MNRAS, 465, 4, p.4914-4930
   * - URL
     - 
   * - Citation
     - http://arxiv.org/pdf/1306.4732v2.pdf and http://arxiv.org/pdf/0910.2773v2.pdf
   * - Rules
     -


"
The likelihood of a strong lensing time-delay system as
modelled in http://arxiv.org/pdf/1306.4732v2.pdf
and http://arxiv.org/pdf/0910.2773v2.pdf

 "



Assumptions
-----------

 - Strong lensing modelling details.



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - lens_name
     - str
     - None
     - Name of lens to use. B1608 and RXJ1131 are accepted, if 'None', user must set remaining parameter manually
   * - z_d
     - real
     - 
     - Only if lens_name='None'. Distance to the lens
   * - z_s
     - real
     - 
     - Only if lens_name='None'. Distance to the source
   * - lambda_d
     - real
     - 
     - Only if lens_name='None'. See 0910.2773v2 equation 5
   * - mu_d
     - real
     - 
     - Only if lens_name='None'. See 0910.2773v2 equation 5
   * - sigma_d
     - real
     - 
     - Only if lens_name='None'. See 0910.2773v2 equation 5
   * - name
     - str
     - 
     - Name for the strong lens


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - distances
     - z
     - real 1d
     - 
     - Redshifts of samples
   * - 
     - d_m
     - real 1d
     - 
     - Co-moving distance in Mpc
   * - cosmological_parameters
     - omega_k
     - real
     - 0.0
     - Curvature density fraction today
   * - 
     - hubble
     - real
     - 
     - Hubble parameter H0 (km/s/Mpc)


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - B1608_like
     - real
     - Only if lens_name=B1608. Likelihood of B1608 system
   * - 
     - RXJ1131_like
     - real
     - Only if lens_name=RXJ1131. Likelihood of RXJ1131 system
   * - 
     - name_like
     - real
     - General case, name from ini file. Likelihood of named system


