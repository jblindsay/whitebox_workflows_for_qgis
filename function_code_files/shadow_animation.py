from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
wbe.shadow_animation(raster_1, palette2, max_dist3, 'date4', time_interval5, 'location6', image_height7, delay8, 'label9')
wbe.check_in_license('license_id')
