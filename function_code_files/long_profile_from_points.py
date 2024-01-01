from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('d8_pointer1')
vector_2 = wbe.read_vector('points2')
raster_3 = wbe.read_raster('dem3')
wbe.long_profile_from_points(raster_1, variable_name, raster_3, esri_pointer4)
wbe.check_in_license('license_id')
