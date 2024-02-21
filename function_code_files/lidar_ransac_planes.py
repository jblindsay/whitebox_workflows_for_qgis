import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = wbe.read_lidar('in_lidar1')
outputLidar = wbe.lidar_ransac_planes(lidar_1, search_radius2, num_iterations3, num_samples4, inlier_threshold5, acceptable_model_size6, max_planar_slope7, classify8, only_last_returns9)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
