import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
vector_1 = wbe.read_vector('points1')
raster_5 = wbe.read_raster('base_raster5')
outputRaster = wbe.tin_interpolation(vector_1, 'field_name2', use_z3, cell_size4, raster_5, max_triangle_edge_length6)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
