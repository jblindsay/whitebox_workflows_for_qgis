import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = None
if r"red1" != "None":
    raster_1 = wbe.read_raster(r"red1")
raster_2 = None
if r"green2" != "None":
    raster_2 = wbe.read_raster(r"green2")
raster_3 = None
if r"blue3" != "None":
    raster_3 = wbe.read_raster(r"blue3")
raster_4 = None
if r"composite4" != "None":
    raster_4 = wbe.read_raster(r"composite4")
(outputRaster0, outputRaster1, outputRaster2) = wbe.rgb_to_ihs(raster_1, raster_2, raster_3, raster_4)
wbe.write_raster(outputRaster0, r"fnOutput0", compress_raster)
wbe.write_raster(outputRaster1, r"fnOutput1", compress_raster)
wbe.write_raster(outputRaster2, r"fnOutput2", compress_raster)
wbe.check_in_license('license_id')
