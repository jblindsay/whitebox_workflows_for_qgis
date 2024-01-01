from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
vector_1 = wbe.read_vector('pour_pts1')
raster_2 = wbe.read_raster('flow_accum2')
outputVector = wbe.snap_pour_points(vector_1, raster_2, snap_dist3)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
