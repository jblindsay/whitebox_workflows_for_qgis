from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
raster_6 = wbe.read_raster('base_raster6')
outputRaster = wbe.vector_points_to_raster(vector_1, 'field_name2', 'assign_op3', zero_background4, cell_size5, raster_6)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
