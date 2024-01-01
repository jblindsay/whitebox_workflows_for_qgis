from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
vector_2 = wbe.read_vector('points2')
wbe.multiscale_std_dev_normals_signature(raster_1, variable_name, min_scale3, step_size4, num_steps5, step_nonlinearity6)
wbe.check_in_license('license_id')
