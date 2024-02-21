import os
import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
rasters_1 = wbe.read_rasters(rasters1)
outputRasters = wbe.inverse_pca(rasters_1, 'pca_report_file2')
for i in range(len(outputRasters)):
    fn = os.path.join(wbe.working_directory, f"{fnOutput}{str(i)}.tif")
    fn = fn.replace("'", "")
    wbe.write_raster(outputRasters[i], fn, compress_raster)
wbe.check_in_license('license_id')
