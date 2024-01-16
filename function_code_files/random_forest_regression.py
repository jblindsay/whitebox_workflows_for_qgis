from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(input_rasters1)
vector_2 = wbe.read_vector('training_data2')
outputRaster = wbe.random_forest_regression(rasters_1, vector_2, 'field_name3', n_trees4, min_samples_leaf5, min_samples_split6, test_proportion7, create_output8)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
