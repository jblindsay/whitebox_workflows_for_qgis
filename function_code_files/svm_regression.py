from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(input_rasters1)
vector_2 = wbe.read_vector('training_data2')
outputRaster = wbe.svm_regression(rasters_1, vector_2, 'class_field_name3', 'scaling_method4', c_value5, epsilon_value6, kernel_gamma7, test_proportion8, create_output9)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
