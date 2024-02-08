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
vector_2 = wbe.read_vector('points2')
wbe.multiscale_std_dev_normals_signature(raster_1, vector_2, 'output_html_file3', min_scale4, step_size5, num_steps6, step_nonlinearity7)
wbe.check_in_license('license_id')
