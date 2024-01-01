from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input_lidar1')
outputLidar = wbe.classify_lidar(lidar_1, search_radius2, grd_threshold3, oto_threshold4, linearity_threshold5, planarity_threshold6, num_iter7, facade_threshold8)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
