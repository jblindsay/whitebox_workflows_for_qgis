from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('inputRaster1')
outputVector = wbe.river_centerlines(raster_1, min_length2, search_radius3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
