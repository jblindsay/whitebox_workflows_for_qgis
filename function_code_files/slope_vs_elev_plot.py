import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
files = [dem_rasters1]
file_nms = [fr"{x.strip()}" for x in files]
rasters_1 = wbe.read_rasters(*file_nms)
files = [watershed_rasters3]
file_nms = [fr"{x.strip()}" for x in files]
rasters_3 = wbe.read_rasters(*file_nms)
wbe.slope_vs_elev_plot(rasters_1, 'output_html_file2', rasters_3)
wbe.check_in_license('license_id')
