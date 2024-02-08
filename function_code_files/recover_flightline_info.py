import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input1')
outputLidar = wbe.recover_flightline_info(lidar_1, max_time_diff2, pt_src_id3, user_data4, rgb5)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
