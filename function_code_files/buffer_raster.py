from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('input1')
outputRaster = wbe.buffer_raster(raster_1, buffer_size2, grid_cells_units3)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
