from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(input_rasters1)
outputRaster = wbe.modified_k_means_clustering(rasters_1, num_start_clusters2, merge_distance3, max_iterations4, percent_changed_threshold5)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
