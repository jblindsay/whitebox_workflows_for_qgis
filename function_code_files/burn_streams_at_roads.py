from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
vector_2 = wbe.read_vector('streams2')
vector_3 = wbe.read_vector('roads3')
outputRaster = wbe.burn_streams_at_roads(raster_1, variable_name, variable_name, road_width4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
