import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
files = [input_rasters1]
file_nms = [fr"{x.strip()}" for x in files]
rasters_1 = wbe.read_rasters(*file_nms)
vector_2 = wbe.read_vector(r"training_data2")
outputRaster = wbe.knn_classification(rasters_1, vector_2, 'class_field_name3', 'scaling_method4', k5, test_proportion6, use_clipping7, create_output8)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
