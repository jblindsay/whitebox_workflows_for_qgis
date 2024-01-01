from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
vector_2 = wbe.read_vector('walls2')
vector_3 = wbe.read_vector('breach_lines3')
outputRaster = wbe.raise_walls(raster_1, variable_name, variable_name, wall_height4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
