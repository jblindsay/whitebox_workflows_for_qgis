import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
vector_1 = wbe.read_vector('input_points1')
outputVector = wbe.construct_vector_tin(vector_1, 'field_name2', use_z3, max_triangle_edge_length4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
