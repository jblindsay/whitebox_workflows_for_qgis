import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"dem1")
vector_2 = wbe.read_vector(r"points2")
outputVector = wbe.skyline_analysis(raster_1, vector_2, 'output_html_file3', max_dist4, observer_hgt_offset5, output_as_polygons6, az_fraction7)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
