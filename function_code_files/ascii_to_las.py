import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
wbe.ascii_to_las(input_ascii_files1, 'pattern2', epsg_code3)
wbe.check_in_license('license_id')
