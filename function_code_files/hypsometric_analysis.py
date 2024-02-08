import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(dem_rasters1)
rasters_3 = wbe.read_rasters(watershed_rasters3)
wbe.hypsometric_analysis(rasters_1, 'output_html_file2', rasters_3)
wbe.check_in_license('license_id')
