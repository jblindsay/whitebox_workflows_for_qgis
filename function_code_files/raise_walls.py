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
vector_2 = wbe.read_vector(r"walls2")
vector_3 = wbe.read_vector(r"breach_lines3")
outputRaster = wbe.raise_walls(raster_1, vector_2, vector_3, wall_height4)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
