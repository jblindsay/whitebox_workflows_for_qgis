from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
outputVector = wbe.yield_filter(vector_1, 'yield_field_name2', 'pass_field_name3', swath_width4, z_score_threshold5, min_yield6, max_yield7)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
