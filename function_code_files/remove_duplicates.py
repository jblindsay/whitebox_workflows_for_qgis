from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input1')
outputLidar = wbe.remove_duplicates(lidar_1, include_z2)
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')