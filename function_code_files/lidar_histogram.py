from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input_lidar1')
wbe.lidar_histogram(lidar_1, 'parameter2', clip_percent3)
wbe.check_in_license('license_id')
