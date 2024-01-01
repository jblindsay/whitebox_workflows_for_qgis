from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('points1')
raster_5 = wbe.read_raster('base_raster5')
outputRaster = wbe.heat_map(vector_1, 'field_name2', bandwidth3, cell_size4, raster_5, 'kernel_function6')
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')