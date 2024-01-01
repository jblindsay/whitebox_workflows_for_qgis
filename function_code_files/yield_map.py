from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
outputVector = wbe.yield_map(vector_1, 'pass_field_name2', swath_width3, max_change_in_heading4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
