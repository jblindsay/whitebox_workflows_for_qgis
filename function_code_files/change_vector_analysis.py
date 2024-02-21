import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
rasters_1 = wbe.read_rasters(date1_rasters1)
rasters_2 = wbe.read_rasters(date2_rasters2)
(outputRaster0, outputRaster1, outputString2) = wbe.change_vector_analysis(rasters_1, rasters_2)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.write_text(outputString2, 'fnOutput2')
wbe.check_in_license('license_id')
