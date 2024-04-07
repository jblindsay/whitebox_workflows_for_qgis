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
(outputVector0, outputVector1) = wbe.ridge_and_valley_vectors(raster_1, filter_size2, ep_threshold3, slope_threshold4, min_length5)
wbe.write_vector(outputVector0, r"fnOutput0")
wbe.write_vector(outputVector1, r"fnOutput1")
wbe.check_in_license('license_id')
