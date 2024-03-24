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
model_bytes = wbe.random_forest_regression_fit(rasters_1, vector_2, 'field_name3', n_trees4, min_samples_leaf5, min_samples_split6, test_proportion7)
with open('fnOutput', "wb") as file:
    file.write(bytearray(model_bytes))
wbe.check_in_license('license_id')
