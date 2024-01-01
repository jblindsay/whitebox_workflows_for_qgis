from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input_lidar1')
wbe.lidar_point_stats(lidar_1, cell_size2, num_points3, num_pulses4, avg_points_per_pulse5, z_range6, intensity_range7, predominant_class8)
wbe.check_in_license('license_id')
