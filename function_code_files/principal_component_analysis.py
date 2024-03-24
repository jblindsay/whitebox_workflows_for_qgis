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
files = [rasters1]
file_nms = [fr"{x.strip()}" for x in files]
rasters_1 = wbe.read_rasters(*file_nms)
outputRasters = wbe.principal_component_analysis(rasters_1, 'output_html_file2', num_components3, standardized4)
for i in range(len(outputRasters)):
    fn = os.path.join(wbe.working_directory, f"{fnOutput}{str(i)}.tif")
    fn = fn.replace("'", "")
    wbe.write_raster(outputRasters[i], fn, compress_raster)
wbe.check_in_license('license_id')
