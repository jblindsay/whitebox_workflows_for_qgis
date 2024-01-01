from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
wbe.slope_vs_aspect_plot(raster_1, aspect_bin_size2, min_slope3, z_factor4)
wbe.check_in_license('license_id')
