import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('inputRaster1')
outputVector = wbe.find_lowest_or_highest_points(raster_1, 'output_type2')
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
