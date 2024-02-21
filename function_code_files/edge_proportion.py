import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('inputRaster1')
(outputRaster0, outputString1) = wbe.edge_proportion(raster_1)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_text(outputString1, 'fnOutput1')
wbe.check_in_license('license_id')
