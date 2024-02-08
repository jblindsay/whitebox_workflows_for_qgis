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
outputVector = wbe.lidar_hex_bin(lidar_1, width2, 'orientation3')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
