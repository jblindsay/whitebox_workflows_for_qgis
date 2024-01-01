from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('input1')
freq = wbe.list_unique_values(vector_1, 'field_name2')
with open('fnOutput', 'w') as f:
    for line in freq:
        s = f"{line[0]},{line[1]}\n"
        f.write(f"{s}")
wbe.check_in_license('license_id')
