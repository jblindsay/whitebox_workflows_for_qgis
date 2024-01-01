from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
raster_2 = wbe.read_raster('basins2')
outputVector = wbe.longest_flowpath(raster_1, raster_2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')