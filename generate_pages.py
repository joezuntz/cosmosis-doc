import generate_sampler_pages
import generate_module_pages
import tempfile
import os

def shallow_clone(repo, dest):
    cmd = "git clone --depth 1 {} {}".format(repo, dest)
    os.system(cmd)

def main():
    os.makedirs("reference/standard_library", exist_ok=True)
    os.makedirs("reference/samplers", exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        cosmosis_dir = os.path.join(tmpdir, 'cosmosis')
        shallow_clone('https://github.com/joezuntz/cosmosis', cosmosis_dir)
        generate_sampler_pages.main(cosmosis_dir)

        csl_dir = os.path.join(tmpdir, 'cosmosis-standard-library')
        shallow_clone('https://github.com/joezuntz/cosmosis-standard-library', csl_dir)
        generate_module_pages.main(csl_dir)

if __name__ == '__main__':
    main()
