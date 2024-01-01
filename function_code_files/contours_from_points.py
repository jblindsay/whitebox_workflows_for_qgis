from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
outputVector = wbe.contours_from_points(vector_1, 'field_name2', use_z_values3, max_triangle_edge_length4, contour_interval5, base_contour6, smoothing_filter_size7)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')