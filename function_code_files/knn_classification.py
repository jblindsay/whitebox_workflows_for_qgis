from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(input_rasters1)
vector_2 = wbe.read_vector('training_data2')
outputRaster = wbe.knn_classification(rasters_1, vector_2, 'class_field_name3', 'scaling_method4', k5, test_proportion6, use_clipping7, create_output8)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
