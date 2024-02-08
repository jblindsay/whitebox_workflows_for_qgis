import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('raster11')
raster_2 = wbe.read_raster('raster22')
wbe.two_sample_ks_test(raster_1, raster_2, 'output_html_file3', num_samples4)
wbe.check_in_license('license_id')
