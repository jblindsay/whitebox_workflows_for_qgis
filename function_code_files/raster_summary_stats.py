from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
raster_1 = wbe.read_raster('input1')
data = wbe.raster_summary_stats(raster_1)
with open('fnOutput', 'w') as f:
    f.write(f"{data}")
wbe.check_in_license('license_id')