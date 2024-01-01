from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
outputRaster = wbe.time_in_daylight(raster_1, az_fraction2, max_dist3, latitude4, longitude5, 'utc_offset_str6', start_day7, end_day8, 'start_time9', 'end_time10')
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
