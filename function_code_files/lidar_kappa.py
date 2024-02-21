import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
lidar_1 = wbe.read_lidar('input_lidar11')
lidar_2 = wbe.read_lidar('input_lidar22')
outputRaster = wbe.lidar_kappa(lidar_1, lidar_2, 'output_html_file3', cell_size4, output_class_accuracy5)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
