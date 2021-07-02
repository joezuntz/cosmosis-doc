WiggleZBao
================================================

Compute the likelihood of the supplied expansion history against WiggleZ BAO data

.. list-table::
    
   * - File
     - likelihood/wigglez_bao/wigglez_bao.py
   * - Attribution
     - WiggleZ Team
   * -
     - MontePython Team
   * - URL
     - http://www.smp.uq.edu.au/wigglez-data/
   * - Citation
     - MNRAS 441, 3524 (2014)
   * - Rules
     -


"This module gives a likelihood of the redshift-distance and redshift-Hubble
relations in combined form D_v = (da**2 * (1+z)**2 * dr)**(1./3.) 
where dr = z / H. It uses the sound horizon at last-scatter rs_zdrag and 
the predicted expansion since last scattering to predict the BAO size
at the redshifts at which the WiggleZ survey measured them.

A correlated Gaussian likelihood is then returned."



Assumptions
-----------

 - WiggleZ dark energy survey data set
 - FLRW metric and standard BAO size



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - data_file
     - str
     - included file
     - Path to file with measured z - D_v values in
   * - weight_file
     - str
     - included file
     - Path to inverse covariance matrix file
   * - rs_fiducial
     - real
     - 148.6
     - Fiducial value of sound horizon at last scattering used in making data
   * - verbose
     - bool
     - False
     - Print extra output


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
     - d_a
     - real 1d
     - 
     - Angular diameter distance in Mpc
   * - 
     - h
     - real 1d
     - 
     - Hubble parameter with in units of Mpc
   * - 
     - rz_zdrag
     - real
     - 
     - Sound horizon at last scattering in Mpc


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - likelihoods
     - wigglez_bao_like
     - real
     - Likelihood of supplied expansion history


