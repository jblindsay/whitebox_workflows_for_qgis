import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"inputRaster1")
(outputRaster0, outputString1) = wbe.raster_perimeter(raster_1, 'units2', zero_background3)
wbe.write_raster(outputRaster0, r"fnOutput0", compress_raster)
wbe.write_text(outputString1, r"fnOutput1")
wbe.check_in_license('license_id')
