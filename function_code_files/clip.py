import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector('input1')
vector_2 = wbe.read_vector('clip_layer2')
outputVector = wbe.clip(vector_1, vector_2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
