import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
lidar_1 = wbe.read_lidar('input_lidar1')
outputVector = wbe.individual_tree_detection(lidar_1, min_search_radius2, min_height3, max_search_radius4, max_height5, only_use_veg6)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
