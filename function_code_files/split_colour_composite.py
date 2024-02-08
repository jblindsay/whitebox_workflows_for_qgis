import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('composite_image1')
(outputRaster0, outputRaster1, outputRaster2) = wbe.split_colour_composite(raster_1)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.write_raster(outputRaster2, 'fnOutput2', compress_raster)
wbe.check_in_license('license_id')
