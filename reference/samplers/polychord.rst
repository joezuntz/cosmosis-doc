The Polychord sampler
--------------------------------------------------------------------

Nested sampling

+-------------+-----------------------------------------------------+
| Name        | polychord                                           |
+-------------+-----------------------------------------------------+
| Version     | 1.14                                                |
+-------------+-----------------------------------------------------+
| Author(s)   | Will Handley, Mike Hobson, Anthony Lasenby          |
+-------------+-----------------------------------------------------+
| URL         | https://ccpforge.cse.rl.ac.uk/gf/project/polychord/ |
+-------------+-----------------------------------------------------+
| Citation(s) | arXiv:1502.01856, arXiv:1506.00171                  |
+-------------+-----------------------------------------------------+
| Parallelism | parallel                                            |
+-------------+-----------------------------------------------------+

Nested sampling is a method designed to calculate the Bayesian Evidence of a distribution, for use in comparing multiple models to see which fit the data better. PolyChord is an alternative to MultiNest, specialised to scale to higher dimensions, and able to exploite a hierarchy of parameter speeds.

The evidence is the integral of the likelihood over the prior; it is equivalent to the probability of the model given the data (marginalizing over the specific parameter values): B = P(D|M) = \int P(D|Mp) P(p|M) dp

Nested sampling is an efficient method for evaluating this integral using members of an ensemble of live points and steadily replacing the lowest likelihood point with a new one  from a gradually shrinking proposal so and evaluating the integral in horizontal slices.

PolyChord is a particularly sophisticated implementation of this which can cope  with multi-modal distributions using a k-means clustering algorithm and a proposal made from an affine-invariant slice sampling informed by the covariance of individual modes

The output from PolyChord is not a set of posterior samples, but rather a set of weighted samples - when making histograms or parameter estimates these must be included.

The primary PolyChord parameter is the number of live points in the ensemble. Run time is linear in the number of live points. Unlike MultiNest, PolyChord will still produce sensible results even using relatively low numbers of live points ~O(5*nDims), but needs more in order to infer accurate evidences. A good strategy is to begin with a low number of live points for experimental runs, and scale up for production quality runs.

One odd feature of the PolyChord output is that it doesn't save any results until it has done a complete run through the parameter space.  It then starts again on a second run,  and sometimes a third depending on the parameters.  So don't worry if you don't see any lines in the output file for a while.




Installation
============

No special installation required; everything is packaged with CosmoSIS




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| Name                        | Type                 | Description                                                                                          | Default   |
+=============================+======================+======================================================================================================+===========+
| max_iterations              | integer, default=-1  | Maximum number of samples to take, default unlimited                                                 |           |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| live_points                 | integer, default=100 | Number of live points in the ensemble                                                                |           |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| num_repeats                 | integer, default=0   | The length of the slice sampling chain to produce a new sample, default=3*nslow                      |           |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| feedback                    | integer              | Verbosity level                                                                                      | 1         |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| polychord_outfile_root      | str                  | In addition to CosmoSIS output, save a collection of PolyChord output files                          | (empty)   |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| base_dir                    | str                  | Root dir to store the output files                                                                   | '.'       |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| resume                      | bool                 | If you previously set multinest_outfile_root you can restart an interrupted chain with this setting  | F         |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| compression_factor          | float                | ) Frequency of printed output, dumping and clustering from inside PolyChord                          | exp(-1    |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| random_seed                 | integer              | Seed to use for random proposal; -1 to generate from current time.  Allows re-running chains exactly | -1        |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| log_zero                    | float                | Log-probabilities lower than this value are considered to be -infinity                               | -1e6      |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| tolerance                   | float                | Target error on evidence                                                                             | 0.1       |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| nprior                      | integer, default=-1  | The number of prior samples to draw before starting compression - default=-1                         |           |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| boost_posteriors            | float                | What factor should we bulk up the posterior points by (using inter-chain points)                     | 0.0       |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| weighted_posteriors         | bool                 | Whether to calculate weighted posteriors                                                             | T         |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| equally_weighted_posteriors | bool                 | Whether to calculate equally weighted posteriors                                                     | T         |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| cluster_posteriors          | bool                 | Whether to calculate clustered posteriors                                                            | T         |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+
| fast_fraction               | float                | Fraction of time to spend in fast params                                                             | 0.5       |
+-----------------------------+----------------------+------------------------------------------------------------------------------------------------------+-----------+


