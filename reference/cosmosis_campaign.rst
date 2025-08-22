Command line flags for cosmosis-campaign
----------------------------------------

CosmoSIS includes a campaign management system for running multiple related analyses efficiently. The :code:`cosmosis-campaign` tool lets you define and manage collections of related runs.

You can view command line flags for cosmosis-campaign using the command::

    cosmosis-campaign --help

Overview
========

The campaign system allows you to:

* Define collections of related CosmoSIS runs in YAML format
* Automatically generate parameter, values, and priors files for each run
* Submit jobs to batch systems like SLURM
* Track the status of multiple runs
* Create hierarchical run structures where runs inherit from parent runs

Campaign files are written in YAML format and specify a collection of runs, each with their own parameter modifications, environment variables, and submission settings.

Usage
=====

List all available runs in a campaign file::

    cosmosis-campaign campaign.yaml --list

Show the complete configuration for a specific run::

    cosmosis-campaign campaign.yaml --cat run_name

Check the status of runs (shows completion status and sample counts)::

    cosmosis-campaign campaign.yaml --status
    cosmosis-campaign campaign.yaml --status run1 run2  # specific runs only

Test a run using the test sampler (useful for debugging)::

    cosmosis-campaign campaign.yaml --test run_name
    cosmosis-campaign campaign.yaml --test run_name --pdb  # with debugger

Run a specific analysis::

    cosmosis-campaign campaign.yaml --run run_name
    cosmosis-campaign campaign.yaml --run run_name --mpi  # with MPI

Submit a run to a batch system::

    cosmosis-campaign campaign.yaml --submit run_name

Campaign File Format
====================

Campaign files are written in YAML format with the following structure::

    output_dir: ./output
    output_name: "{name}"  # Format string for output files

    include:
      - other_campaign.yaml  # Include runs from other files

    components:
      component_name:
        params:
          - "runtime.sampler=emcee"
        values:
          - "cosmological_parameters.omega_m=0.25 0.3 0.35"
        pipeline:
          - "after camb pk_to_cl"

    submission:
      submit: sbatch
      cancel: scancel
      template: |
        #!/bin/bash
        #SBATCH --job-name={job_name}
        #SBATCH --time={time}
        #SBATCH --nodes={nodes}
        #SBATCH --ntasks={tasks}
        #SBATCH --cpus-per-task={cores_per_task}
        #SBATCH --output={log}

        {command}
      time: "01:00:00"
      nodes: 1
      tasks: 1
      cores_per_task: 1

    runs:
      - name: baseline
        base: params.ini
        params:
          - "runtime.sampler=emcee"
        values:
          - "cosmological_parameters.omega_m=0.25 0.3 0.35"

      - name: with_neutrinos
        parent: baseline
        values:
          - "cosmological_parameters.massive_nu=3"
          - "cosmological_parameters.mnu=0.0 0.06 0.6"

      - name: different_sampler
        parent: baseline
        components:
          - component_name
        params:
          - "runtime.sampler=multinest"

Run Configuration
=================

Each run can specify:

* **base**: Base parameter file to start from
* **parent**: Name of parent run to inherit from (alternative to base)
* **components**: List of reusable components to include
* **params**: List of modifications to the main parameter file
* **values**: List of modifications to the values file  
* **priors**: List of modifications to the priors file
* **pipeline**: List of modifications to the pipeline modules
* **env**: Dictionary of environment variables to set
* **submission**: Override submission parameters for this specific run

Parameter modifications use the format :code:`section.option=value`. Pipeline modifications support operations like :code:`after`, :code:`before`, :code:`replace`, :code:`delete`, and :code:`append`.

Environment Variables
====================

Environment variables can be set at the global level or per-run, and support expansion in parameter values. This is useful for pointing to different data files or setting compilation flags::

    env:
      DATA_DIR: /path/to/data
      HALOFIT: takahashi

    runs:
      - name: test_run
        base: params.ini
        values:
          - "camb.feedback=3"
        env:
          DATA_DIR: /different/path  # Override global setting

Inheritance
===========

Runs can inherit from parent runs, allowing you to build hierarchical campaigns where later runs build on earlier ones. Child runs inherit all settings from their parent and can override any of them.

This is particularly useful for parameter studies where you want to systematically vary one parameter while keeping others fixed.