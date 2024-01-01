from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
raster_2 = wbe.read_raster('loading2')
raster_3 = wbe.read_raster('efficiency3')
raster_4 = wbe.read_raster('absorption4')
outputRaster = wbe.dinf_mass_flux(raster_1, raster_2, raster_3, raster_4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')