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
outputLidar = wbe.colourize_based_on_class(lidar_1, intensity_blending_amount2, 'clr_str3', use_unique_clrs_for_buildings4, search_radius5)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
