from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input1')
outputLidar = wbe.lidar_elevation_slice(lidar_1, minz2, maxz3, classify4, in_class_value5, out_class_value6)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')