from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('base1')
outputVector = wbe.hexagonal_grid_from_vector_base(vector_1, width2, 'orientation3')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
