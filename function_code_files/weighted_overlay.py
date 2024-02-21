import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
rasters_1 = wbe.read_rasters(factors1)
rasters_3 = wbe.read_rasters(cost3)
rasters_4 = wbe.read_rasters(constraints4)
outputRaster = wbe.weighted_overlay(rasters_1, weights2, rasters_3, rasters_4, scale_max5)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
