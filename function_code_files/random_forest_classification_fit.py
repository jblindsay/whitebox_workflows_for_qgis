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
vector_2 = wbe.read_vector('training_data2')
model_bytes = wbe.random_forest_classification_fit(rasters_1, vector_2, 'class_field_name3', 'split_criterion4', n_trees5, min_samples_leaf6, min_samples_split7, test_proportion8)
with open('fnOutput', "wb") as file:
    file.write(bytearray(model_bytes))
wbe.check_in_license('license_id')
