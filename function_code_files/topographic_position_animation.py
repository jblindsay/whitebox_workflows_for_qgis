import sys
path = 'plugin_path'
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('dem1')
wbe.topographic_position_animation(raster_1, 'output_html_file2', palette3, min_scale4, num_steps5, step_nonlinearity6, image_height7, delay8, 'label9', use_dev_max10)
wbe.check_in_license('license_id')
