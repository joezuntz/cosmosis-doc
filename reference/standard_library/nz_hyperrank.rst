nz_hyperrank
================================================

Load, rank, and sample a set of density n(z) realisations from a FITS file

.. list-table::
    
   * - File
     - number_density/nz_hyperrank/nz_hyperrank.py
   * - Attribution
     - Juan P. Cordero, Ian Harrison
   * - URL
     - 
   * - Citation
     -
   * - Rules
     - If you use a file from a particular survey you should cite that survey


"This module is designed to work with the number density part of the FITS
files described in:
http://github.com/joezuntz/2point/

Uncertainty in the redshift distributions is usually described by a nuisance
parameter which allows the mean of the distribution to be shifted from a fiducial
central value.
This value is then marginalized in the pipeline.
But higher order distribution moments which are not captured by this paramterization
can propagate into the cosmological parameters and its uncertainty ignored.

An empirical approach to solve this is to provide multiple realisations of the
redshift distributions n(z) containing realistic samples of the higher order moments.
as well as the small redshift scale variance.
We can then sample from them directly rather than using nuisance to capture the
full effect of the shapes of the redshift distributions, as well as their internal
correlation.

This module extends the load_nz_fits module to read multiple realisations, one per
extension.
It then ranks the realisations depending on the selected mode and maps it to a continuous
hyper-parameter which can be sampled in the pipeline.
The ranking is intended to provide a meaningful metric in the n(z) space, allowing
for better sampling efficiency over random sampling of the realisations.
"



Assumptions
-----------

 - Realisations are provided in FITS extensions NZ_{NAME}_realisation_{NUMBER}



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
   * - mode
     - str
     - 
     - Ranking mode, use to define how the realisations are mapped to the hyperparameter. It has to be one of the following: no-rank, unified, separate, inv-chi-unified, inv-chi-separate, random, external
   * - nz_file
     - str
     - 
     - Absolute or relative path to an n(z) file
   * - data_set
     - str
     - 
     - Names of the extensions prefixes in the FITS files to load and save to the block
   * - n_bins
     - int
     - 
     - Number of tomographic bins
   * - n_hist
     - int
     - 
     - Number of redshift histogram bins at which n(z) is evaluated
   * - n_realisations
     - int
     - 
     - Number of realisations contained in the FITS file, numbered from 0 to n_realisations-1
   * - external_ranking_filename
     - str
     - 
     - Path to a plain text file with a 1D array of length = n_realisations with values to be ranked


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
   * - ranks
     - rank_hyperparm_i
     - real
     - 
     - Hyperparameter mapped to a redshift distribution. If mode is separate, then i = 1...n_bins


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
   * - wl_number_density
     - nz
     - int
     - Number of redshift samples
   * - 
     - nbin
     - int
     - Number of bins
   * - 
     - z
     - real 1d
     - Redshift sample values
   * - 
     - bin_
     - real 1d
     - n(z) at redshift sample values.  bin_1, bin_2, ...


