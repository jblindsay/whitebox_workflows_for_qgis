from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(input_rasters1)
outputRaster = wbe.k_means_clustering(rasters_1, num_clusters2, max_iterations3, percent_changed_threshold4, 'initialization_mode5', min_class_size6)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
