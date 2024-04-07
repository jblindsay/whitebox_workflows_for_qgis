import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
vector_1 = wbe.read_vector(r"input1")
raster_5 = None
if r"base_raster5" != "None":
    raster_5 = wbe.read_raster(r"base_raster5")
outputRaster = wbe.vector_lines_to_raster(vector_1, 'field_name2', zero_background3, cell_size4, raster_5)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
