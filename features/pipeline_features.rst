Pipeline Features
==================


The Consistency module
----------------------

The CosmoSIS standard library has a particularly helpful module called ``consistency``, which is designed to translate automatically between different ways of expressing cosmological parameters.  

For example, if your values file specifies both :math:`\Omega_m` and :math:`h^2` then it will calculate :math:`\omega_m \equiv \Omega_m h^2` for you automatically.  

Any sufficient choice of the parameters can be specified and the remainder will be determined.

To use this module, just include the module ``utility/consistency/consistency_interface.py`` at the start of a pipeline.



Pre- and post-scripts
---------------------

CosmoSIS can automatically run a script before executing your pipeline; if the script returns an error code then the pipeline will not be run.  

It can also run a script after the 

You could use this feature to:
- run a check before the pipeline to make sure some test result is as expected.
- download some data that is needed for a pipeline.
- postprocess results after the pipeline is complete and make some plots.

To use this feature, add lines in the ``[runtime]`` section of the parameter file:

.. code-block:: ini

    [runtime]
    pre_script=./my_pre_script.sh
    post_script=./my_post_script.sh

Your scripts can be any executable. If the pre-script has a non-zero return value then the pipeline will not run.

Making pipeline graphs
------------------------

You will need the pygraphviz tool to use this feature.  On Conda, you can install it with:

.. code-block:: ini

    conda install -c conda-forge pygraphviz

Create your graph from a complete data block like this:

.. code-block:: python

    import cosmosis
    p = cosmosis.LikelihoodPipeline("./examples/des-y1.ini")
    data = p.run_parameters(p.start_vector())
    p.make_graph(data, "des-y1.dot")


and then you can use the ``dot`` prgoram from the shell to make an image:

.. code-block:: bash

    dot -Tpng -o des.png des-y1.dot

