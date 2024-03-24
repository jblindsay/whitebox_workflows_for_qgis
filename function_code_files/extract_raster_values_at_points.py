import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
files = [rasters1]
file_nms = [fr"{x.strip()}" for x in files]
rasters_1 = wbe.read_rasters(*file_nms)
vector_2 = wbe.read_vector(r"points2")
(outputVector0, outputString1) = wbe.extract_raster_values_at_points(rasters_1, vector_2)
wbe.write_vector(outputVector0, 'fnOutput0')
wbe.write_text(outputString1, 'fnOutput1')
wbe.check_in_license('license_id')
