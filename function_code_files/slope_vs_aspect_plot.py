import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
wbe.slope_vs_aspect_plot(raster_1, 'output_html_file2', aspect_bin_size3, min_slope4, z_factor5)
wbe.check_in_license('license_id')
