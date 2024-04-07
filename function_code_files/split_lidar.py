import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_2 = None
if r"input_lidar2" != "None":
    lidar_2 = wbe.read_lidar(r"input_lidar2")
wbe.split_lidar('split_criterion1', lidar_2, interval3, min_pts4)
wbe.check_in_license('license_id')
