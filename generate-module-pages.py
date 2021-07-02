import sys
import os
import yaml

yaml_filename = "module.yaml"


background = {
    "distances",
    "growth_factor",
}

boltzmann = {
    "isitgr-camb",
    "camb",
    "class",
    "mgcamb",
}

structure = {
    "CRL_Eisenstein_Hu",
    "CosmicEmu",
    "FrankenEmu",
    "Extreme_Value_Statistics",
    "Press_Schechter_MF",
    "Sheth-Tormen MF",
    "Tinker_MF",
    "extract_growth",
    "extrapolate",
    "constant_bias",
    "sigma_cpp",
    "sigma_r",
}

twopoint_maths = {
    "cl_to_corr",
    "cl_to_xi_nicaea",
    "cl_to_xi_wigner_d",
    "project_2d",
    "shear_xi",
    "wl_spectra",
    "wl_spectra_ppf",
}

twopoint_sys = {
    "add_intrinsic",
    "ia_z_powerlap",
    "apply_astrophysical_biases",
    "shear_bias",
    "kappa_beam",
    "kappa_ell_cut",
    "linear_alignments",
    "constant_bias",
    "no_bias",
    "clerkin",
}

sample_properties = {
    "Joachimi_Bridle_alpha",
    "gaussian_window",
    "load_nz",
    "load_nz_fits",
    "nz_hyperrank",
    "photoz_bias",
    "smail",
}

likelihoods = {
    "2pt",
    "6dFGS",
    "BBN",
    "BICEP2",
    "BOSS",
    "Cluster_mass",
    "JulloLikelihood",
    "Riess11",
    "Riess16",
    "WiggleZBao",
    "balmes",
    "boss_dr12",
    "fgas",
    "h0licow",
    "jla",
    "mgs_bao",
    "pantheon",
    "planck2018",
    "planck_sz",
    "strong_lens_time_delays",
    "wmap",
    "wmap_shift",
}



misc = {
    "BBN-Consistency",
    "consistency",
    "sigma8_rescale",
    "stop",
    "delete",
    "copy",
    "rename",
}


categories = {
    "Background": background,
    "Boltzmann": boltzmann,
    "Structure": structure,
    "Two-point Mathemetics": twopoint_maths,
    "Two-point Systematics": twopoint_sys,
    "Sample Properties": sample_properties,
    "Likelihoods": likelihoods,
    "Misc & Utilities": misc
}


category_blurb = {
    "Background": "These modules calculate quantities related to the average background expansion of the Universe.",
    "Boltzmann": "Boltzmann codes evolve cosmic perturbations from the early Universe through recombination and to late times, and power spectra of matter, the CMB, and other quantities.",
    "Structure": "These modules compute aspects of cosmic structure, for example by emulating matter behaviour, integrating over it, or calculating halo model quantities.",
    "Two-point Mathemetics": "These modules perform mathematical claculations associated with two-point statistics, mostly on a sphere.",
    "Two-point Systematics": "These modules compute and apply quantities associated with systematics errors on two-point (and potentially other) quantities.",
    "Sample Properties": "These modules compute properties, mostly number density, of galaxy samples.",
    "Likelihoods": "These module provide likelihoods that compare theory predictions to data",
    "Misc & Utilities": "These modules supply special utilities or calculation tools",
}



page_template = """{name}
================================================

{purpose}

.. list-table::
    
   * - File
     - {interface_path}
   * - Attribution
{attribution_lines}
   * - URL
     - {url}
   * - Citation
{citation_lines}
   * - Rules
{rule_lines}


{explanation}


Assumptions
-----------

{assumption_lines}



Setup Parameters
----------------

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
{param_lines}

Input values
----------------

.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
{input_lines}

Output values
----------------


.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
{output_lines}

"""

def make_list_lines(item):
    if not item:
        return "     -"
    if isinstance(item, str):
        item = [item]
    lines = [f"     - {item[0]}"]
    lines += [f"   * -\n     - {a}" for a in item[1:]]
    return "\n".join(lines)



def make_page_text(info):
    author_lines = [f"     - {a}" for a in info['attribution']]
    info['attribution_lines'] = make_list_lines(info['attribution'])
    info['citation_lines'] = make_list_lines(info['cite'])
    info['rule_lines'] = make_list_lines(info['rules'])

    if info['assumptions']:
        info['assumption_lines'] = "\n".join([f" - {a}" for a in info['assumptions']])
    else:
        info['assumption_lines'] = ''

    param_lines = ""
    for name, p in info['params'].items():
        p['name'] = name
        if p['default'] is None:
            p['default'] = ''

        param_lines += """   * - {name}
     - {type}
     - {default}
     - {meaning}
""".format(**p)


    input_lines = ""
    for section, keys in info['inputs'].items():
        for i, (name, p) in enumerate(keys.items()):
            p['section'] = section if i == 0 else ""
            p['name'] = name
            if p['default'] is None:
                p['default'] = ''
            input_lines += """   * - {section}
     - {name}
     - {type}
     - {default}
     - {meaning}
""".format(**p)


    output_lines = ""
    for section, keys in info['outputs'].items():
        for i, (name, p) in enumerate(keys.items()):
            p['section'] = section if i == 0 else ""
            p['name'] = name
            output_lines += """   * - {section}
     - {name}
     - {type}
     - {meaning}
""".format(**p)

    info['param_lines'] = param_lines
    info['input_lines'] = input_lines
    info['output_lines'] = output_lines


    return page_template.format(**info)


overview_template = """Standard Library Overview
==============================

The CosmoSIS standard library is a collection of modules
designed for Cosmological parameter estimation.  You can couple
together pieces of it to build analysis piplines.

"""



def make_overview(purposes):

    out = []
    template = """
{cat}
-----------------------

{blurb}

.. list-table::
   :header-rows: 1

   * - Name
     - Purpose
{module_lines}
"""

    for cat, cat_set in categories.items():
        module_lines = []
        blurb = category_blurb[cat]
        for name in cat_set:
            purpose = purposes.get(name)
            if purpose is None:
                print(f"Did not find yaml for module: {name}")
                continue
            link = f":doc:`{name} <standard_library/{name}>` "
            module_lines.append(f"   * - {link}")
            module_lines.append(f"     - {purpose}")
        module_lines = "\n".join(module_lines)
        out.append(template.format(cat=cat, module_lines=module_lines, blurb=blurb))

    with open("reference/standard_library_overview.rst", "w") as f:
        f.write(overview_template)
        f.write("\n\n".join(out))


def main(source_dir):
    n = len(source_dir)
    m = len(yaml_filename)
    purposes = {}

    for (dirpath, dirnames, filenames) in os.walk(source_dir):
        if 'cosmosis-des-library' in dirpath:
            continue
        if yaml_filename in filenames:
            yaml_path = os.path.join(dirpath, yaml_filename)
            directory = yaml_path[n+1:-m]
            if not directory:
                continue
            print(directory)
            with open(yaml_path) as f:
                y = yaml.safe_load(f)

            y['interface_path'] = os.path.join(directory, y['interface'])
            page_text = make_page_text(y)
            name = y['name']
            with open(f"./reference/standard_library/{name}.rst", 'w') as f:
                f.write(page_text)

            purposes[name] = y['purpose']
            for cat, cat_set in categories.items():
                if name in cat_set:
                    break
            else:
                print("Note: module has no category and will not appear in listing:", name, yaml_path)

    make_overview(purposes)



if __name__ == '__main__':
    main(sys.argv[1])