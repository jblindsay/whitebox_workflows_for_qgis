import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
outputVector = wbe.csv_points_to_vector('input_file1', x_field_num2, y_field_num3, epsg4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
