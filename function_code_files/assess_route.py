import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector(r"routes1")
raster_2 = wbe.read_raster(r"dem2")
outputVector = wbe.assess_route(vector_1, raster_2, segment_length3, search_radius4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
