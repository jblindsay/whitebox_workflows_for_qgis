from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(dem_rasters1)
rasters_2 = wbe.read_rasters(watershed_rasters2)
wbe.slope_vs_elev_plot(rasters_1, rasters_2)
wbe.check_in_license('license_id')
