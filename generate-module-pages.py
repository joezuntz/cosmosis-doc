import sys
import os
import yaml
import tabulate

yaml_filename = "module.yaml"



background = {
    "distances",
    "growth_factor",
    "log_w_model",
    "astropy_background",
    "rescale_distances_rdh",
}

boltzmann = {
    "isitgr-camb",
    "camb",
    "class",
    "mgcamb",
}

emulators = {
    "bacco_emulator",
    "CosmicEmu",
    "EuclidEmulator2",
    "FrankenEmu",
}


structure = {
    "CRL_Eisenstein_Hu",
    # "pyhmcode",
    "Extreme_Value_Statistics",
    "Press_Schechter_MF",
    "Sheth-Tormen MF",
    "Tinker_MF",
    "extract_growth",
    "extrapolate",
    "constant_bias",
    "sigma_cpp",
    "sigma_r",
    "NLfactor",
}

twopoint_maths = {
    "cl_to_corr",
    "cl_to_xi_nicaea",
    "cl_to_xi_wigner_d",
    "project_2d",
    "cosebis",
    "wl_spectra",
    "wl_spectra_ppf",
}

twopoint_sys = {
    "add_intrinsic",
    "ia_z_powerlaw",
    "apply_astrophysical_biases",
    "shear_bias",
    "kappa_beam",
    "kappa_ell_cut",
    "linear_alignments",
    "constant_bias",
    "no_bias",
    "clerkin",
    "add_magnification",
    "baryonic",
}

sample_properties = {
    "Joachimi_Bridle_alpha",
    "gaussian_window",
    "load_nz",
    "load_nz_fits",
    "photoz_bias",
    "smail",
    "nz_multirank",
}

likelihoods = {
    "2pt",
    "6dFGS",
    "act-dr6-lens",
    "BBN",
    "BICEP2",
    "BOSS",
    "Cluster_mass",
    "desi_dr1_arxiv",
    "JulloLikelihood",
    "Riess11",
    "Riess16",
    "WiggleZBao",
    "balmes",
    "boss_dr12",
    "fgas",
    "h0licow",
    "hsc_cosmic_shear",
    "jla",
    "mgs_bao",
    "pantheon",
    "pantheon_plus",
    "planck2018",
    "planck_py",
    "planck_sz",
    "strong_lens_time_delays",
    "wmap",
    "wmap_shift",
    "eboss_dr16_lrg",
    "eboss_dr16_qso",
    "mgs",
    "boss_dr12_lrg_reanalyze",
    "eboss_dr16_elg",
    "eboss_dr16_lya",
    "Riess21",
    "sacc_like",
    "lrg",
    "qso",
    "eboss_dr14_lya",
    "des-y3-bao",
    "tdcosmo",
}



misc = {
    "fast_pt",
    "BBN-Consistency",
    "w0wa_sum_prior",
    "consistency",
    "sigma8_rescale",
    "stop",
    "delete",
    "copy",
    "rename",
    "correlated_priors",
}


categories = {
    "Background": background,
    "Boltzmann": boltzmann,
    "Emulators": emulators,
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
    "Emulators": "These modules emulate aspects of cosmic structure based on fits to simulations.",
    "Structure": "These modules compute aspects of cosmic structure, for example by integrating over cosmic structure, or calculating halo model quantities.",
    "Two-point Mathemetics": "These modules perform mathematical claculations associated with two-point statistics, mostly on a sphere.",
    "Two-point Systematics": "These modules compute and apply quantities associated with systematics errors on two-point (and potentially other) quantities.",
    "Sample Properties": "These modules compute properties, mostly number density, of galaxy samples.",
    "Likelihoods": "These module provide likelihoods that compare theory predictions to data",
    "Misc & Utilities": "These modules supply special utilities or calculation tools",
}



page_template = """{name}
================================================

{purpose}

{main_table}

{explanation}


Assumptions
-----------

{assumption_lines}



Setup Parameters
----------------

{param_head}
{param_lines}

Input values
----------------

{input_head}
{input_lines}

Output values
----------------


{output_head}
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

param_head1 = """.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Default
     - Description
"""

input_head1 = """.. list-table::
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Default
     - Description
"""

output_head1 = """.. list-table:: Output values
   :header-rows: 1

   * - Section
     - Name
     - Type
     - Description
"""

#    * - File
#      - {interface_path}
#    * - Attribution
# {attribution_lines}
#    * - URL
#      - {url}
#    * - Citation
# {citation_lines}
#    * - Rules
# {rule_lines}


def make_page_text(info):
    author_lines = [f"     - {a}" for a in info['attribution']]

    rows = [
        ["File", info['interface_path']],
    ]
    if info['attribution']:
        rows.append(["Attribution", info['attribution'][0]])
        for r in info['attribution'][1:]:
            rows.append(["", r])

    rows.append(["URL", info['url']])
    if info['cite']:
        rows.append(["Citations", info['cite'][0]])
        for r in info['cite'][1:]:
            rows.append(["", r])

    info['main_table'] = tabulate.tabulate(rows, tablefmt="grid")

    info['rule_lines'] = make_list_lines(info['rules'])

    if (not info['assumptions']) or (len(info['assumptions']) == 1 and not info['assumptions'][0].strip()):
        info['assumption_lines'] = 'None'
    else:
        info['assumption_lines'] = "\n".join([f" - {a}" for a in info['assumptions']])

    info['param_head'] = param_head1 if info['params'] else "None"
    info['input_head'] = input_head1 if info['inputs'] else "None"
    info['output_head'] = output_head1 if info['outputs'] else "None"

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

    info['explanation'] = info['explanation'].strip().strip("\"'")

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
            link = f":doc:`{name} <../reference/standard_library/{name}>` "
            module_lines.append(f"   * - {link}")
            module_lines.append(f"     - {purpose}")
        module_lines = "\n".join(module_lines)
        out.append(template.format(cat=cat, module_lines=module_lines, blurb=blurb))

    with open("usage/standard_library_overview.rst", "w") as f:
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