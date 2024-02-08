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
wbe.lidar_tile(lidar_1, tile_width2, tile_height3, origin_x4, origin_y5, min_points_in_tile6, output_laz_format7)
wbe.check_in_license('license_id')
