import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector(r"points1")
raster_8 = None
if r"base_raster8" != "None":
    raster_8 = wbe.read_raster(r"base_raster8")
outputRaster = wbe.idw_interpolation(vector_1, 'field_name2', use_z3, weight4, radius5, min_points6, cell_size7, raster_8)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
