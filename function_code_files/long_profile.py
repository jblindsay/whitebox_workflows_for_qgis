from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('d8_pointer1')
raster_2 = wbe.read_raster('streams_raster2')
raster_3 = wbe.read_raster('dem3')
wbe.long_profile(raster_1, raster_2, raster_3, esri_pointer4)
wbe.check_in_license('license_id')