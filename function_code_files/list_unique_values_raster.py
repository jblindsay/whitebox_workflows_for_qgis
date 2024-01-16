from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('inputRaster1')
data = wbe.list_unique_values_raster(raster_1)
wbe.write_text(data, 'fnOutput')
wbe.check_in_license('license_id')
