from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('in_lidar1')
outputLidar = wbe.find_flightline_edge_points(lidar_1)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
