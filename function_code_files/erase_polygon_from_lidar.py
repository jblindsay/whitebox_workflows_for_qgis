from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input1')
vector_2 = wbe.read_vector('polygons2')
outputLidar = wbe.erase_polygon_from_lidar(lidar_1, variable_name)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
