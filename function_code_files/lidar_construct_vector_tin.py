import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = wbe.read_lidar(r"input_lidar1")
outputVector = wbe.lidar_construct_vector_tin(lidar_1, 'returns_included2', excluded_classes3, min_elev4, max_elev5, max_triangle_edge_length6)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
