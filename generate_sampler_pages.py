import os
import sys
import yaml
import glob
import tabulate

#Generate the summary page of all the samplers
#Generate the specific page for each sampler.

def name_for_sampler_page(name):
	return name

page_template = u"""The {name} sampler
--------------------------------------------------------------------

{purpose}

{info_table}

{explanation}


Installation
============

{installation}


Parameters
============

These parameters can be set in the sampler's section in the ini parameter file.  
If no default is specified then the parameter is required. A listing of "(empty)" means a blank string is the default.

{parameter_table}


"""

def parse_parameter_description(desc):
	paren, rest = desc.split(')', 1)
	paren = paren.strip()
	rest = rest.strip().strip('"')
	paren=paren.lstrip('(')
	if ';' in paren:
		dtype, default=paren.split(';')
		default=default.split('=')[1]
	else:
		dtype=paren
		default=""
	if default.strip()=="''":
		default = '(empty)'
	return dtype, default, rest



def generate_sampler_wiki(info):
	"Generate wiki markdown for a single sampler"
	info = info.copy()
	name = info['name']
	info['explanation'] = info['explanation'].replace("\n",'\n\n').strip('"')
	info['installation'] = info['installation'].replace("\n",'\n\n').strip('"')
	page_name = name_for_sampler_page(name)
	page = open('reference/samplers/{}.rst'.format(page_name), 'w')

	info_table = tabulate.tabulate([
		['Name', name],
		['Version', info['version']],
		['Author(s)', ', '.join(info['attribution'])],
		['URL', info['url']],	
		['Citation(s)', ', '.join(info['cite'])],
		['Parallelism', info['parallel']],
	], tablefmt="grid")

	table2 = []
	for pname,description in list(info['params'].items()):
		try:
			dtype, default, rest = parse_parameter_description(description)
			table2.append([pname, dtype, str(default), rest])
		except (IndexError, ValueError):
			print("ERROR: Could not parse in {0}".format(name))
			print(description)
			continue

	parameter_table = tabulate.tabulate(table2, headers=['Name', 'Type', 'Default', 'Description', ], tablefmt="grid", disable_numparse=True)

	info['name'] = name.capitalize()
	info['citations'] = ', '.join(info['cite'])
	info['authors'] = ', '.join(info['attribution'])
	info['parameter_table'] = parameter_table
	info['info_table'] = info_table

	markdown = page_template.format( 
		**info
		)
	page.write(markdown)
	page.close()



def generate_overview(infos):
	pass


def main(dirname):
	#get the base dir to work from
	sampler_dir=os.path.join(dirname, "cosmosis", "samplers")
	#Find and parse all the files
	search_path = f"{sampler_dir}/*/sampler.yaml"
	yaml_files = glob.glob(search_path)
	infos = [yaml.safe_load(open(f)) for f in yaml_files]
	#Make the ordering the same every time

	for info in infos:
		print(info['name'])
		generate_sampler_wiki(info)


if __name__ == '__main__':
	main(sys.argv[1])
