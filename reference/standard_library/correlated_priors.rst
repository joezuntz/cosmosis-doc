correlated_priors
================================================

Include correlations between nusiance parameters

+-------------+-------------------------------------------------------+
| File        | number_density/correlated_priors/correlated_priors.py |
+-------------+-------------------------------------------------------+
| Attribution | Tilman Troester                                       |
+-------------+-------------------------------------------------------+
|             | Chieh-An Lin                                          |
+-------------+-------------------------------------------------------+
|             | Marika Asgari                                         |
+-------------+-------------------------------------------------------+
|             | Catherine Heymans                                     |
+-------------+-------------------------------------------------------+
| URL         |                                                       |
+-------------+-------------------------------------------------------+

This module converts a set of uncorrelated parameters into a set of correlated ones following a covariance matrix. The covariance matrix is provided in block ascii format. The matrix must be ordered to match the order of the input parameter list. The output parameters are updated with the cholesky decomposition of the covariance matrix multiplied by the values of the input parameters. The output parameters are then passed to the downstream modules.
A typical example usage is converting from uncorrelated nuisance parameters following normal distributions to multivariate normal ones.
In future this functionality should be included in the cosmosis core.


Assumptions
-----------

 - A covariance matrix for the correlated parameters is provided in block ascii format. The matrix must be ordered to match the order of the input parameter list



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description

   * - uncorrelated_parameters
     - str
     - 
     - The list of parameter names for the uncorrelated parameters that the sampler will vary. The parameters should be in the form "section1/param1  section2/param2 ..."
   * - output_parameters
     - str
     - 
     - The list of parameter names for the output sample of correlated parameters. These must be named following the relevant expectation of the downstream modules. For example the parameter for photo-z bias in bin i is expected to be called bias_i. The parameters should be in the form "section1/param1  section2/param2 ..."
   * - covariance
     - str
     - 
     - Location of the covariance matrix defining the correlation between the parameters


Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description

   * - input_parameters_sections
     - names
     - real
     - 
     - The input parameter. The sections and names are defined in the uncorrelated_parameters parameter.


Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description

   * - section1
     - name1
     - real
     - The values of the output paramaters, which have the appropriate correlations.  The sections and names are defined in the output_parameters parameter.


