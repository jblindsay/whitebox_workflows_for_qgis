from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('d8_pointer1')
vector_2 = wbe.read_vector('pour_points2')
outputRaster = wbe.watershed(raster_1, variable_name, esri_pntr3)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
