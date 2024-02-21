import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('input1')
outputVector = wbe.layer_footprint_raster(raster_1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
