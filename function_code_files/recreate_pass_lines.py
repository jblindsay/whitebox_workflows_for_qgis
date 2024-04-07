import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector(r"input1")
(outputVector0, outputVector1) = wbe.recreate_pass_lines(vector_1, 'yield_field_name2', max_change_in_heading3, ignore_zeros4)
wbe.write_vector(outputVector0, r"fnOutput0")
wbe.write_vector(outputVector1, r"fnOutput1")
wbe.check_in_license('license_id')
