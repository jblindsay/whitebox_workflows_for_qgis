from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input_lidar1')
wbe.lidar_eigenvalue_features(lidar_1, num_neighbours2, search_radius3)
wbe.check_in_license('license_id')
