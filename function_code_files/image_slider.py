from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('left_raster1')
raster_2 = wbe.read_raster('right_raster2')
wbe.image_slider(raster_1, raster_2, left_palette3, left_reverse_palette4, 'left_label5', right_palette6, right_reverse_palette7, 'right_label8', image_height9)
wbe.check_in_license('license_id')
