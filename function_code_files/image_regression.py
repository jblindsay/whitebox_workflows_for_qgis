import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('independent_variable1')
raster_2 = wbe.read_raster('dependent_variable2')
outputRaster = wbe.image_regression(raster_1, raster_2, 'output_html_file3', standardize_residuals4, output_scattergram5, num_samples6)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
