import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
vector_1 = wbe.read_vector('lines_vector1')
raster_2 = wbe.read_raster('surface2')
wbe.profile(vector_1, raster_2, 'output_html_file3')
wbe.check_in_license('license_id')
