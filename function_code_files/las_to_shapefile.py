from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input_lidar1')
outputVector = wbe.las_to_shapefile(lidar_1, output_multipoint2)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
