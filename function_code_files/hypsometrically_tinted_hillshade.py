from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
outputRaster = wbe.hypsometrically_tinted_hillshade(raster_1, solar_altitude2, hillshade_weight3, brightness4, atmospheric_effects5, palette6, reverse_palette7, full_360_mode8, z_factor9)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
