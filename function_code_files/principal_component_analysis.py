import os
from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(rasters1)
outputRasters = wbe.principal_component_analysis(rasters_1, num_components2, standardized3)
for i in range(len(outputRasters)):
    fn = os.path.join(wbe.working_directory, f"{fnOutput}{str(i)}.tif")
    fn = fn.replace("'", "")
    wbe.write_raster(outputRasters[i], fn, compress_raster)
wbe.check_in_license('license_id')
