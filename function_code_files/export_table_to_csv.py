from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
wbe.export_table_to_csv(vector_1, 'output_csv_file2', headers3)
wbe.check_in_license('license_id')