from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input1')
(outputLidar0, outputLidar1) = wbe.lidar_thin(lidar_1, resolution2, 'selection_method3', save_filtered4)
wbe.write_lidar(outputLidar0, 'fnOutput0')
wbe.write_lidar(outputLidar1, 'fnOutput1')
wbe.check_in_license('license_id')
