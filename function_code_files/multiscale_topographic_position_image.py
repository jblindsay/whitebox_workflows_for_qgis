import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"local1")
raster_2 = wbe.read_raster(r"meso2")
raster_3 = wbe.read_raster(r"broad3")
raster_4 = wbe.read_raster(r"hillshade4")
outputRaster = wbe.multiscale_topographic_position_image(raster_1, raster_2, raster_3, raster_4, lightness5)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
