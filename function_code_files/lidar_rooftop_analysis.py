import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
vector_2 = wbe.read_vector('building_footprints2')
outputVector = wbe.lidar_rooftop_analysis(, vector_2, search_radius3, num_iterations4, num_samples5, inlier_threshold6, acceptable_model_size7, max_planar_slope8, norm_diff_threshold9, azimuth10, altitude11)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
