Command line flags for cosmosis-sample-fisher
---------------------------------------------

The :code:`cosmosis-sample-fisher` tool generates samples from a Fisher matrix produced by the CosmoSIS Fisher sampler.

You can view command line flags for cosmosis-sample-fisher using the command::

    cosmosis-sample-fisher --help

Purpose
=======

The Fisher sampler in CosmoSIS computes the Fisher information matrix, which provides an estimate of the parameter covariance matrix near the maximum likelihood point. The :code:`cosmosis-sample-fisher` tool uses this Fisher matrix to generate Gaussian samples that approximate the posterior distribution.

This is useful for:

* Quick parameter estimation when the posterior is approximately Gaussian
* Generating starting points for MCMC chains
* Forecasting parameter constraints
* Validating MCMC results against Fisher matrix predictions

Usage
=====

Generate samples from a Fisher matrix::

    cosmosis-sample-fisher fisher_file.txt values_file.ini priors_file.ini num_samples output_file.txt

The tool will:

1. Load the Fisher matrix from the fisher_file
2. Invert it to get the parameter covariance matrix
3. Load parameter definitions from the values and priors files
4. Generate the requested number of samples from a multivariate Gaussian
5. Apply prior cuts to ensure all samples are within the allowed parameter ranges
6. Save the samples to the output file

Arguments
=========

* **fisher_file**: Output file from a CosmoSIS Fisher sampler run containing the Fisher matrix
* **values_file**: The values.ini file that defines parameter ranges  
* **priors_file**: The priors.ini file that defines parameter priors
* **num_samples**: Number of samples to generate (integer)
* **output_file**: Name of the file to save the samples to

The output file will contain samples in the same format as other CosmoSIS samplers, with one sample per row and one column per parameter.

Requirements
============

* The Fisher matrix file must be output from the CosmoSIS Fisher sampler
* The values and priors files must define the same parameters as were used in the Fisher analysis
* Only samples that fall within the prior ranges will be kept, so more samples than requested may need to be generated internally

Example
=======

::

    # First run Fisher analysis
    cosmosis fisher_params.ini

    # Then generate samples from the Fisher matrix
    cosmosis-sample-fisher output/fisher.txt values.ini priors.ini 10000 fisher_samples.txt

This generates 10,000 samples from the Fisher matrix approximation to the posterior.