import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_3 = wbe.read_vector('polygons3')
wbe.select_tiles_by_polygon('input_directory1', 'output_directory2', vector_3)
wbe.check_in_license('license_id')
