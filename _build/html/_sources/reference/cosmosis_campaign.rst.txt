cosmosis-campaign
-----------------

The :code:`cosmosis-campaign` tool manages collections of related CosmoSIS runs. For detailed information about campaigns, see :doc:`../features/campaign`.

You can view command line flags for cosmosis-campaign using the command::

    cosmosis-campaign --help

Command Line Options
====================

* :code:`--list` or :code:`-l` - List the names of all runs in the campaign
* :code:`--cat <name>` or :code:`-c <name>` - Print the ini files that would be generated for a given run  
* :code:`--run <name>` or :code:`-r <name>` - Launch a run
* :code:`--test <name>` or :code:`-t <name>` - Run a pipeline using the test sampler to check it works
* :code:`--status` or :code:`-s` - Show the status of all runs, or a single run if given a name
* :code:`--mpi` - Run under MPI (use with :code:`--run`)
* :code:`--submit <name>` - Submit a run to a batch system