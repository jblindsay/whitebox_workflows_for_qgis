import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
vector_1 = wbe.read_vector('input1')
vector_2 = wbe.read_vector('erase_layer2')
outputVector = wbe.erase(vector_1, vector_2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
