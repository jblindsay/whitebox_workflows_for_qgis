from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('image11')
raster_2 = wbe.read_raster('image22')
outputRaster = wbe.mosaic_with_feathering(raster_1, raster_2, 'resampling_method3', distance_weight4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')