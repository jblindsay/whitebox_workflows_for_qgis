from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
lidar_1 = wbe.read_lidar('input_lidar1')
data = wbe.lidar_info(lidar_1, show_point_density2, show_vlrs3, show_geokeys4)
with open('fnOutput', 'w') as f:
    f.write(f"{data}")
wbe.check_in_license('license_id')
