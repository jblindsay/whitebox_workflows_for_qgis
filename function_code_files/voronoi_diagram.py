from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input_points1')
outputVector = wbe.voronoi_diagram(vector_1)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
