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
outputVector = wbe.lidar_contour(lidar_1, contour_interval2, base_contour3, smooth4, 'interpolation_parameter5', 'returns_included6', excluded_classes7, min_elev8, max_elev9, tile_overlap10, max_triangle_edge_length11)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
