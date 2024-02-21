import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('red1')
raster_2 = wbe.read_raster('green2')
raster_3 = wbe.read_raster('blue3')
raster_4 = wbe.read_raster('opacity4')
outputRaster = wbe.create_colour_composite(raster_1, raster_2, raster_3, raster_4, enhance5, treat_zeros_as_nodata6)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
