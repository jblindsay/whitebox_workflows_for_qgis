from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('specific_catchment_area1')
raster_2 = wbe.read_raster('slope2')
outputRaster = wbe.sediment_transport_index(raster_1, raster_2, sca_exponent3, slope_exponent4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
