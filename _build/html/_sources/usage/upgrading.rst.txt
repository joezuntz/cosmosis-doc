Upgrading from the previous CosmoSIS Version
============================================

You may have used the old CosmoSIS version that was hosted on BitBucket.org.

There are a few changes you need to make for the new version.

Repositories
-------------
The old version of CosmoSIS expected you to download both the main cosmosis repository
and the cosmosis-standard-library.  Now you only download the standard library, unless
you are working on a new sampler.

See the instructions on the :doc:`installation page <../intro/installation>` for details.

Module paths
------------

In the old CosmoSIS you usually had to specify the ``file`` parameters in your main parameter file starting
with ``$COSMOSIS_SRC_DIR/cosmosis-standard-library/``.  You would now typically run chains from the standard
library directory and remove that prefix.  If you were running from a different directory you would use the path
to the standard library as the ``root`` parameter in the ``[runtime]`` section.


Camb & Halofit
--------------

The CAMB module has been replaced with one which uses the camb python package.  A few
parameter names have changed - see the  :doc:`new camb module reference <../reference/standard_library/camb>`
for a full listing.

Additionally, the Halofit modules that were previously separate are now accessed directly through camb.


Two-Point Calculations
----------------------

The project_2d module for calculating the 2D power spectra C_ell has been upgraded. You can mostly
use it as you did before, but the parameters ``n_ell``, ``ell_min`` and ``ell_max`` should now be
``n_ell_logspaced`` ``ell_min_logspaced`` and ``ell_max_logspaced`` instead. There are also many additional
options available now to compute other combinations including biased galaxy samples and non-Limber values.

See :doc:`the project_2d reference <../reference/standard_library/project_2d>` for more details, or see the DES-Y3
example.
