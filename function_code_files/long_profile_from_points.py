import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"d8_pointer1")
vector_2 = wbe.read_vector(r"points2")
raster_3 = wbe.read_raster(r"dem3")
wbe.long_profile_from_points(raster_1, vector_2, raster_3, 'output_html_file4', esri_pointer5)
wbe.check_in_license('license_id')
