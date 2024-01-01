from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('nir_image1')
raster_2 = wbe.read_raster('red_image2')
outputRaster = wbe.normalized_difference_index(raster_1, raster_2, clip_percent3, correction_value4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
