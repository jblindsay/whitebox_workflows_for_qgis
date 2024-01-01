from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
outputRaster = wbe.geomorphons(raster_1, search_distance2, flatness_threshold3, flatness_distance4, skip_distance5, output_forms6, analyze_residuals7)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
