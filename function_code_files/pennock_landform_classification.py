import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('dem1')
(outputRaster0, outputString1) = wbe.pennock_landform_classification(raster_1, slope_threshold2, prof_curv_threshold3, plan_curv_threshold4, z_factor5)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_text(outputString1, 'fnOutput1')
wbe.check_in_license('license_id')
