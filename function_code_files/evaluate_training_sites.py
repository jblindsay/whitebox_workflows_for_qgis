from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(input_rasters1)
vector_2 = wbe.read_vector('training_polygons2')
wbe.evaluate_training_sites(rasters_1, variable_name, 'class_field_name3')
wbe.check_in_license('license_id')
