from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
(outputRaster0, outputRaster1) = wbe.multiscale_curvatures(raster_1, 'curv_type2', min_scale3, step_size4, num_steps5, step_nonlinearity6, log_transform7, standardize8)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.check_in_license('license_id')