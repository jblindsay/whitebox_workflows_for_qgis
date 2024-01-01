from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
wbe.topographic_position_animation(raster_1, palette2, min_scale3, num_steps4, step_nonlinearity5, image_height6, delay7, 'label8', use_dev_max9)
wbe.check_in_license('license_id')
