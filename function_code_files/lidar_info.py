import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
lidar_1 = wbe.read_lidar(r"input_lidar1")
data = wbe.lidar_info(lidar_1, 'output_html_file2', show_point_density3, show_vlrs4, show_geokeys5)
wbe.write_text(data, 'fnOutput')
wbe.check_in_license('license_id')
