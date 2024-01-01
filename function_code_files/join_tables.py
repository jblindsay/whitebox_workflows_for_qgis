from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('primary_vector1')
vector_3 = wbe.read_vector('foreign_vector3')
wbe.join_tables(vector_1, 'primary_key_field2', variable_name, 'foreign_key_field4', 'import_field5')
wbe.check_in_license('license_id')
