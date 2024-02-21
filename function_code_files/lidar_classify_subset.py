import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = wbe.read_lidar('base_lidar1')
lidar_2 = wbe.read_lidar('subset_lidar2')
outputLidar = wbe.lidar_classify_subset(lidar_1, lidar_2, subset_class_value3, nonsubset_class_value4)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
