from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('inputRaster1')
(outputRaster0, outputString1) = wbe.raster_area(raster_1, 'units2', zero_background3)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
with open('fnOutput1', 'w') as f:
    v = outputString1
    f.write(f"{v}")
wbe.check_in_license('license_id')
