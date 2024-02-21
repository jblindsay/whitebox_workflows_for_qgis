import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
rasters_1 = wbe.read_rasters(input_rasters1)
raster_3 = wbe.read_raster('base_raster3')
outputRaster = wbe.resample(rasters_1, cell_size2, raster_3, 'method4')
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
