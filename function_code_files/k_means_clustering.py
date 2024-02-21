import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
rasters_1 = wbe.read_rasters(input_rasters1)
outputRaster = wbe.k_means_clustering(rasters_1, 'output_html_file2', num_clusters3, max_iterations4, percent_changed_threshold5, 'initialization_mode6', min_class_size7)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
