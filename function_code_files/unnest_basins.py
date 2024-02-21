import os
import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('d8_pointer1')
vector_2 = wbe.read_vector('pour_points2')
outputRasters = wbe.unnest_basins(raster_1, vector_2, esri_pntr3)
for i in range(len(outputRasters)):
    fn = os.path.join(wbe.working_directory, f"{fnOutput}{str(i)}.tif")
    fn = fn.replace("'", "")
    wbe.write_raster(outputRasters[i], fn, compress_raster)
wbe.check_in_license('license_id')
