from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
wbe.print_geotiff_tags('file_name1')
wbe.check_in_license('license_id')