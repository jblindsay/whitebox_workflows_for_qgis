from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('data_raster1')
raster_2 = wbe.read_raster('feature_definitions_raster2')
(outputRaster0, outputString1) = wbe.zonal_statistics(raster_1, raster_2, 'stat_type3', zero_is_background4)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
with open('fnOutput1', 'w') as f:
    v = outputString1
    f.write(f"{v}")
wbe.check_in_license('license_id')
