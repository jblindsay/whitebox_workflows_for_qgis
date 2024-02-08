import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
outputVector = wbe.merge_vectors()
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
