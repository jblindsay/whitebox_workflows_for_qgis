import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster('red1')
raster_2 = wbe.read_raster('green2')
raster_3 = wbe.read_raster('blue3')
raster_4 = wbe.read_raster('composite4')
(outputRaster0, outputRaster1, outputRaster2) = wbe.rgb_to_ihs(raster_1, raster_2, raster_3, raster_4)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.write_raster(outputRaster2, 'fnOutput2', compress_raster)
wbe.check_in_license('license_id')
