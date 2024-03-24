import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"raster11")
raster_2 = wbe.read_raster(r"raster22")
wbe.wilcoxon_signed_rank_test(raster_1, raster_2, 'output_html_file3', num_samples4)
wbe.check_in_license('license_id')
