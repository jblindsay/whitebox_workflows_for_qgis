from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('inputRaster1')
wbe.crispness_index(raster_1, 'output_html_file2')
wbe.check_in_license('license_id')
