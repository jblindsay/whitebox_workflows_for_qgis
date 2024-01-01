from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
outputVector = wbe.merge_line_segments(vector_1, snap_tolerance2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')