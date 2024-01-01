from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
outputLidar = wbe.lidar_join()
wbe.write_lidar(outputLidar, 'fnOutput')
wbe.check_in_license('license_id')
