import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
files = [date1_rasters1]
file_nms = [fr"{x.strip()}" for x in files]
rasters_1 = wbe.read_rasters(*file_nms)
files = [date2_rasters2]
file_nms = [fr"{x.strip()}" for x in files]
rasters_2 = wbe.read_rasters(*file_nms)
(outputRaster0, outputRaster1, outputString2) = wbe.change_vector_analysis(rasters_1, rasters_2)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.write_text(outputString2, 'fnOutput2')
wbe.check_in_license('license_id')
