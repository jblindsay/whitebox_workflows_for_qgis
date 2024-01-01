from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
outputVector = wbe.yield_normalization(vector_1, 'yield_field_name2', radius3, standardize4, min_yield5, max_yield6)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')