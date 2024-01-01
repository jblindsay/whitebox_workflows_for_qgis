from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
vector_2 = wbe.read_vector('points2')
wbe.max_elevation_dev_signature(raster_1, variable_name, min_scale3, max_scale4, step_size5)
wbe.check_in_license('license_id')
