import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector('primary_vector1')
wbe.merge_table_with_csv(vector_1, 'primary_key_field2', 'foreign_csv_filename3', 'foreign_key_field4', 'import_field5')
wbe.check_in_license('license_id')
