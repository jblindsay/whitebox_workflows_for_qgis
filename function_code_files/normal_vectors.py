from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input1')
outputLidar = wbe.normal_vectors(lidar_1, search_radius2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')