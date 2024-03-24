import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"input1")
(outputRaster0, outputString1) = wbe.centroid_raster(raster_1)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_text(outputString1, 'fnOutput1')
wbe.check_in_license('license_id')
