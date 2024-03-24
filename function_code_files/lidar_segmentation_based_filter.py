import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = wbe.read_lidar(r"in_lidar1")
outputLidar = wbe.lidar_segmentation_based_filter(lidar_1, search_radius2, norm_diff_threshold3, max_z_diff4, classify_points5)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
