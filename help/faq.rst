Frequently Asked Questions
--------------------------


**When I run under MPI my output file comes out wrong with some lines too short and some repeated**

To run cosmosis under MPI you also need to pass it the --mpi flag, not just use mpirun, e.g.:

.. code-block:: bash

    mpirun -n 4 cosmosis --mpi params.ini

---------------------------------------


**How do I create a new module?**

See :ref:`Tutorial 6: Writing new modules`


---------------------------------------


**How does my new calculation or likelihood code call CosmoSIS?**

It usually doesn't.  CosmoSIS calls your code.  Physics or likelihood calculations are wrapped as CosmoSIS modules, a pipeline element that can plug together, and from there into other modules.

You can call CosmoSIS from other code if you like - see :ref:`Scripting`

---------------------------------------

**CAMB says it's failing to find the parameter w but it's definitely there**

You may need to change:

.. code-block:: ini

    w = -1

to:

.. code-block:: ini

    w = -1.0

------------------------------------------------


**I used git to update the cosmosis standard library and now things don't work**

You may need to run ``make clean`` before running ``make``.

---------------------------------------


**I'm getting a GSL interpolation error when running cosmic shear analyses**

Your n(z) needs to go all the way down to z=0, and no higher than zmax that you gave CAMB.

---------------------------------------


**The axis labels look wrong - they have weird subscripts in the middle of words**

You're using a parameter that cosmosis doesn't know the latex name for.    

For example, say you used a new parameter "m_max" in a section called "galaxies".

Make a new file with the parameters names in called a new file something like ```my-latex.ini```:

.. code-block:: ini

    [galaxies]
    m_max = M_\mathrm{max}


Then run the ``cosmosis-postprocess`` command with the flag ```--more-latex=my-latex.ini```

---------------------------------------


**How can I customize my contour plot colors and line styles?**

Use a "tweak", a set of commands which are run after the plotting is complete to customize one or more plots.  [Demo 8](Demo8) has an explanation of tweaks in general.  Here's a specific example for customizing a plot with two contours on.

Put this text in a file ``contour_tweaks.py`` and then run your postprocess command with the flag ``--extra contour_tweaks.py``:


.. code-block:: python

    from cosmosis.postprocessing.plots import Tweaks
    import pylab

    class ModifyContours(Tweaks):
        # This could also be a list of files.  Just put the base part in here,
        # not the directory, prefix, or suffix.
        filename="2D_cosmological_parameters--omega_m_cosmological_parameters--h0"

        def run(self):
            ax = pylab.gca()

            # each set has two contours in it, inner and outer 
            contour_set_1 = ax.collections[:2]
            contour_set_2 = ax.collections[2:4]

            # set the properties of the contour face and line
            for f in contour_set_1:
                f.set(linestyle=':', linewidth=3, facecolor='none', edgecolor='k', alpha=1.0)

            # you could do the same for contour set 2, etc.,  here.
            # just remember that 2 will always be drawn on top of 1; you may
            #need to choose the order of chain files on the command line accordingly

---------------------------------------

**How can I save a parameter that I marginalize over analytically, or generate in some other way**

If you have an extra parameter that is derived from your chain, for example one marginalized analytically or derived from other parameters, you can save it in the output chains along with the sampled parameters

In the pipeline section of your parameter ini file, set::

    [pipeline]
    extra_output = section_name/param_name   section_name2/param_name2

This would save a parameter ``param_name`` that you write to the data block in the ``section_name`` section.


---------------------------------------

**How can I check convergence of the emcee sampler**

One quick check for convergence of emcee is to plot each parameter the chain as points.  If it has converged then the various chains should all gradually diffuse out from the starting position and then all come to a similar deviation from the mean.  If the chains all still have a gradual drift across the chain, for example if they are all still moving outwards by the end of the chain, then that indicates non-convergence.

If you'd like you can also use the acor module to test convergence as in emcee.  Install acor using ``pip install acor`` and then you can use ``acor.acor(data)`` from python - you will need to reshape the chain to make it ``nwalker * nsample``.


---------------------------------------

**How can I improve emcee convergence**

There is an alpha parameter for emcee, but we do not currently expose it because it does not usually help convergence.  Instead the best way is usually to improve burn-in.  If you can guess a good distribution of starting points for the chain (one per walker; for example, from an earlier chain, or guessing) then you can set ``start_points`` to the name of a file with columns being the parameters and rows being the different starting points.


---------------------------------------

**What parameters does the cosmosis data block include**

The data block does not include a fixed set of parameters. Instead it can contain anything you want to put into it. At the start of a pipeline (i.e. at the start of a single likelihood evaluation) it will contain just the parameters put into it from the values file; after each module is run more things will be added.

