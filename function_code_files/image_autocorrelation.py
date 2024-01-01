from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(rasters1)
wbe.image_autocorrelation(rasters_1, 'contiguity_type2')
wbe.check_in_license('license_id')
