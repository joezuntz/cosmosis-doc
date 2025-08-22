The List sampler
--------------------------------------------------------------------

Re-run existing chain samples

+-------------+-----------------------------------------+
| Name        | list                                    |
+-------------+-----------------------------------------+
| Version     | 1.0                                     |
+-------------+-----------------------------------------+
| Author(s)   | CosmoSIS Team                           |
+-------------+-----------------------------------------+
| URL         | https://bitbucket.org/joezuntz/cosmosis |
+-------------+-----------------------------------------+
| Citation(s) |                                         |
+-------------+-----------------------------------------+
| Parallelism | embarrassing                            |
+-------------+-----------------------------------------+

This is perhaps the second simplest sampler - it simply takes all its samples from a list in a file and runs them all with the new pipeline.

This could probably be replaced with an importance sampler, and may be merged into it in future.




Installation
============

No special installation required; everything is packaged with CosmoSIS




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+----------+---------------------+-----------+----------------------------------------------------------------------------------+
| Name     | Type                | Default   | Description                                                                      |
+==========+=====================+===========+==================================================================================+
| filename | string              |           | cosmosis-format chain of input samples                                           |
+----------+---------------------+-----------+----------------------------------------------------------------------------------+
| save     | string              | (empty)   | if present the base-name to save the cosmology output from each sample           |
+----------+---------------------+-----------+----------------------------------------------------------------------------------+
| burn     | int, default=0      |           | Number of samples to skip from the start of the input file                       |
+----------+---------------------+-----------+----------------------------------------------------------------------------------+
| thin     | int, default=1      |           | Process only every n'th samples from the input file                              |
+----------+---------------------+-----------+----------------------------------------------------------------------------------+
| limits   | bool, default=False |           | Respect the parameter prior limits in the values file; otherwise use all samples |
+----------+---------------------+-----------+----------------------------------------------------------------------------------+


