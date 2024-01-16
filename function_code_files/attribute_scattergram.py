from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
wbe.attribute_scattergram(vector_1, 'field_name_x2', 'field_name_y3', 'output_html_file4', add_trendline5)
wbe.check_in_license('license_id')
