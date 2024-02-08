import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('input1')
raster_2 = wbe.read_raster('reference2')
data = wbe.root_mean_square_error(raster_1, raster_2)
wbe.write_text(data, 'fnOutput')
wbe.check_in_license('license_id')
