import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"dem1")
wbe.shadow_animation(raster_1, 'output_html_file2', palette3, max_dist4, 'date5', time_interval6, 'location7', image_height8, delay9, 'label10')
wbe.check_in_license('license_id')
