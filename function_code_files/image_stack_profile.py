from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(images1)
vector_2 = wbe.read_vector('points2')
wbe.image_stack_profile(rasters_1, variable_name)
wbe.check_in_license('license_id')
