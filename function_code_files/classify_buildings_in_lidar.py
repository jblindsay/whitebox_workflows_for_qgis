import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
lidar_1 = wbe.read_lidar('in_lidar1')
vector_2 = wbe.read_vector('building_footprints2')
outputLidar = wbe.classify_buildings_in_lidar(lidar_1, vector_2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
