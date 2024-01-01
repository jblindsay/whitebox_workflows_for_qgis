from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
outputVector = wbe.dissolve(vector_1, 'dissolve_field2', snap_tolerance3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
