from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('image1')
outputRaster = wbe.direct_decorrelation_stretch(raster_1, achromatic_factor2, clip_percent3)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')