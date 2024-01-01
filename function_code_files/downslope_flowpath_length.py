from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('d8_pointer1')
raster_2 = wbe.read_raster('watersheds2')
raster_3 = wbe.read_raster('weights3')
outputRaster = wbe.downslope_flowpath_length(raster_1, raster_2, raster_3, esri_pntr4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
