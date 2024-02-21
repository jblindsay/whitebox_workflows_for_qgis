import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('base1')
outputVector = wbe.rectangular_grid_from_raster_base(raster_1, width2, height3, x_origin4, y_origin5)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
