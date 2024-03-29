import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"pan1")
raster_2 = wbe.read_raster(r"colour_composite2")
raster_3 = wbe.read_raster(r"red3")
raster_4 = wbe.read_raster(r"green4")
raster_5 = wbe.read_raster(r"blue5")
outputRaster = wbe.panchromatic_sharpening(raster_1, raster_2, raster_3, raster_4, raster_5, 'fusion_method6')
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
