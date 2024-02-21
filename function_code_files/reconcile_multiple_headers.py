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
outputVector = wbe.reconcile_multiple_headers(vector_1, 'region_field_name2', 'yield_field_name3', radius4, min_yield5, max_yield6, mean_tonnage7)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
