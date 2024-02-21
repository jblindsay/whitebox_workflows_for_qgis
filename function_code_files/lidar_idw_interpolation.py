import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
lidar_1 = wbe.read_lidar('input_lidar1')
outputRaster = wbe.lidar_idw_interpolation(lidar_1, 'interpolation_parameter2', 'returns_included3', cell_size4, idw_weight5, search_radius6, excluded_classes7, min_elev8, max_elev9)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
