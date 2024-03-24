import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"streams1")
raster_2 = wbe.read_raster(r"d8_pointer2")
outputVector = wbe.raster_streams_to_vector(raster_1, raster_2, esri_pointer3, all_vertices4)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
