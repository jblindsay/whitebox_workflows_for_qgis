import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector(r"streams1")
raster_2 = wbe.read_raster(r"dem2")
(outputRaster0, outputRaster1, outputRaster2, outputRaster3) = wbe.topological_breach_burn(vector_1, raster_2, snap_distance3)
wbe.write_raster(outputRaster0, r"fnOutput0", compress_raster)
wbe.write_raster(outputRaster1, r"fnOutput1", compress_raster)
wbe.write_raster(outputRaster2, r"fnOutput2", compress_raster)
wbe.write_raster(outputRaster3, r"fnOutput3", compress_raster)
wbe.check_in_license('license_id')
