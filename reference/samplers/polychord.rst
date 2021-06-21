The Polychord sampler
--------------------------------------------------------------------

Ensemble Nested sampling

+--------------+------------------------------------------------------+
| | Name       | | polychord                                          |
+--------------+------------------------------------------------------+
| | Version    | | 1,14                                               |
+--------------+------------------------------------------------------+
| | Author(s)  | | Will Handley,Mike Hobson,Anthony Lasenby           |
+--------------+------------------------------------------------------+
| | URL        | | https://ccpforge.cse.rl.ac.uk/gf/project/polychord/|
+--------------+------------------------------------------------------+
| | Citation(s)| |  arXiv:1502.01856, arXiv:1506.00171                |
+--------------+------------------------------------------------------+
| | Parallelism| | parallel                                           |
+--------------+------------------------------------------------------+

Nested sampling is a method designed to calculate the Bayesian Evidence of a distribution, for use in comparing multiple models to see which fit the data better. PolyChord is an alternative to MultiNest, specialised to scale to higher dimensions, and able to exploite a hierarchy of parameter speeds.

The evidence is the integral of the likelihood over the prior; it is equivalent to the probability of the model given the data (marginalizing over the specific parameter values): B = P(D|M) = \int P(D|Mp) P(p|M) dp

Nested sampling is an efficient method for evaluating this integral using members of an ensemble of live points and steadily replacing the lowest likelihood point with a new one from a gradually shrinking proposal so and evaluating the integral in horizontal slices.

PolyChord is a particularly sophisticated implementation of this which can cope with multi-modal distributions using a k-means clustering algorithm and a proposal made from an affine-invariant slice sampling informed by the covariance of individual modes

The output from PolyChord is not a set of posterior samples, but rather a set of weighted samples - when making histograms or parameter estimates these must be included.

The primary PolyChord parameter is the number of live points in the ensemble. Run time is linear in the number of live points. Unlike MultiNest, PolyChord will still produce sensible results even using relatively low numbers of live points ~O(5*nDims), but needs more in order to infer accurate evidences. A good strategy is to begin with a low number of live points for experimental runs, and scale up for production quality runs.

One odd feature of the PolyChord output is that it doesn't save any results until it has done a complete run through the parameter space. It then starts again on a second run, and sometimes a third depending on the parameters. So don't worry if you don't see any lines in the output file for a while.


Installation
============

No special installation required; everything is packaged with CosmoSIS




Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

+--------------------------------+----------+---------------------------------------------------------------+----------+
| | Parameter                    | | Type   | | Meaning                                                     | | Default|
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | live_points                  | | integer| | Number of live points in the ensemble                       |          |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | random_seed                  | | integer| | Seed to use for random proposal; -1 to generate from current| | -1     |
|                                |          | | time.  Allows re-running chains exactly                     |          |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | feedback                     | | int    | | Logging level  (default 1, increase for more info)          | | T      |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | resume                       | | bool   | | If you previously set multinest_outfile_root you can restart| | F      |
|                                |          | | an interrupted chain with this setting                      |          |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | polychord_outfile_root       | | str    | | In addition to CosmoSIS output, save a collection of        | | (empty)|
|                                |          | | polychord output files                                      |          |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | tolerance                    | | float  | | Target tolerance in Z error                                 | | 0.1    |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | compression_factor           | | float  | | How often to print progress, (default=1/e, max=1)           | | 0.3678 |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | base_dir                     | | str    | | Base directory for output                                   | | 200    |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | max_iterations               | | integer| | Maximum number of samples to take                           | | "."    |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | num_repeats                  | | integer| | Number of slice-sampling steps each new sample              | | 3N     |
|                                |          | | Helps with curved degeneracies and thin "corners".          |          |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | nprior                       | | integer| | Number of prior samples drawn before starting compression   | | 10nlive|
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | log_zero                     | | float  | | Log-probabilities lower than this value are considered to be| | -1e6   |
|                                |          | | -infinity                                                   |          |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | weighted_posteriors          | | bool   | | Whether to save weighted posteriors in outfile_root         | | T      |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | equally_weighted_posteriors  | | bool   | | Whether to save equally weighted posteriors in outfile_root | | T      |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | cluster_posteriors           | | bool   | | Whether to check for and explore multi-modality             | | T      |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | fast_fraction                | | float  | | Fraction of time to spend in fast subspaces                 | | 0.5    |
+--------------------------------+----------+---------------------------------------------------------------+----------+
| | boost_posteriors             | | float  | | Increase number of posterior samples                        | | 0.0    |
+--------------------------------+----------+---------------------------------------------------------------+----------+

