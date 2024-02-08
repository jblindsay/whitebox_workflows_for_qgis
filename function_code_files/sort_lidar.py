import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_2 = wbe.read_lidar('input_lidar2')
outputLidar = wbe.sort_lidar('sort_criteria1', lidar_2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
