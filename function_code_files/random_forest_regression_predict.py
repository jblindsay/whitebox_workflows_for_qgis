import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
rasters_1 = wbe.read_rasters(input_rasters1)
model_bytes_2 = []
with open('model_bytes2', mode='rb') as file:
    model_bytes_2 = list(file.read())
outputRaster = wbe.random_forest_regression_predict(rasters_1, model_bytes_2)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
