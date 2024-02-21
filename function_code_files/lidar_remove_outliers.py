import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = wbe.read_lidar('input1')
outputLidar = wbe.lidar_remove_outliers(lidar_1, search_radius2, elev_diff3, use_median4, classify5)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
