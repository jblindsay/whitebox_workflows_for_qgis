import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = wbe.read_lidar(r"input_lidar1")
outputRaster = wbe.lidar_radial_basis_function_interpolation(lidar_1, 'interpolation_parameter2', 'returns_included3', cell_size4, num_points5, excluded_classes6, min_elev7, max_elev8, 'func_type9', 'poly_order10', weight11)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
