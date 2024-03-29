import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector(r"seed_points1")
raster_2 = wbe.read_raster(r"d8_pointer2")
outputRaster = wbe.trace_downslope_flowpaths(vector_1, raster_2, esri_pntr3, zero_background4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
