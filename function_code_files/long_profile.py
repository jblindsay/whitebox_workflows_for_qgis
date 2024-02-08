import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('d8_pointer1')
raster_2 = wbe.read_raster('streams_raster2')
raster_3 = wbe.read_raster('dem3')
wbe.long_profile(raster_1, raster_2, raster_3, 'output_html_file4', esri_pointer5)
wbe.check_in_license('license_id')
