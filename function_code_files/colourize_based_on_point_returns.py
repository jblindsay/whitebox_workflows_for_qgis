import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input_lidar1')
outputLidar = wbe.colourize_based_on_point_returns(lidar_1, intensity_blending_amount2, 'only_ret_colour3', 'first_ret_colour4', 'intermediate_ret_colour5', 'last_ret_colour6')
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
