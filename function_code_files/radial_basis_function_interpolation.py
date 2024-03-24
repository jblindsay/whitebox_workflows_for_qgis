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
raster_7 = wbe.read_raster(r"base_raster7")
outputRaster = wbe.radial_basis_function_interpolation(vector_1, 'field_name2', use_z3, radius4, min_points5, cell_size6, raster_7, 'func_type8', 'poly_order9', weight10)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
