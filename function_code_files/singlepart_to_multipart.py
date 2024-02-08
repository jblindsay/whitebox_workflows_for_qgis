import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
outputVector = wbe.singlepart_to_multipart(vector_1, 'field_name2')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
