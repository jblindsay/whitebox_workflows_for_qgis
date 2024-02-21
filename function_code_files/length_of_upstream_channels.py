import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('d8_pointer1')
raster_2 = wbe.read_raster('streams_raster2')
outputRaster = wbe.length_of_upstream_channels(raster_1, raster_2, esri_pointer3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
