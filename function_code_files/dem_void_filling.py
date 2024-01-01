from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
raster_2 = wbe.read_raster('fill2')
outputRaster = wbe.dem_void_filling(raster_1, raster_2, mean_plane_dist3, 'edge_treatment4', weight_value5)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
