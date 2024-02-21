import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
vector_1 = wbe.read_vector('streams1')
raster_2 = wbe.read_raster('dem2')
(outputVector0, outputVector1, outputVector2, outputVector3) = wbe.vector_stream_network_analysis(vector_1, raster_2, max_ridge_cutting_height3, snap_distance4)
wbe.write_vector(outputVector0, 'fnOutput0')
wbe.write_vector(outputVector1, 'fnOutput1')
wbe.write_vector(outputVector2, 'fnOutput2')
wbe.write_vector(outputVector3, 'fnOutput3')
wbe.check_in_license('license_id')
