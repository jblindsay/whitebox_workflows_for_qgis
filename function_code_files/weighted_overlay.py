import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
files = [factors1]
file_nms = [fr"{x.strip()}" for x in files]
rasters_1 = wbe.read_rasters(*file_nms)
files = [cost3]
file_nms = [fr"{x.strip()}" for x in files]
rasters_3 = wbe.read_rasters(*file_nms)
files = [constraints4]
file_nms = [fr"{x.strip()}" for x in files]
rasters_4 = wbe.read_rasters(*file_nms)
outputRaster = wbe.weighted_overlay(rasters_1, weights2, rasters_3, rasters_4, scale_max5)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
