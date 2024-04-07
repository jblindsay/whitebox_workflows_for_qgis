import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = None
if r"input_lidar1" != "None":
    lidar_1 = wbe.read_lidar(r"input_lidar1")
outputLidar = wbe.lidar_ground_point_filter(lidar_1, search_radius2, min_neighbours3, slope_threshold4, height_threshold5, classify6, slope_norm7, height_above_ground8)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
