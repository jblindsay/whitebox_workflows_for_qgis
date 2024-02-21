import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
rasters_1 = wbe.read_rasters(images1)
vector_2 = wbe.read_vector('points2')
wbe.image_stack_profile(rasters_1, vector_2, 'output_html_file3')
wbe.check_in_license('license_id')
