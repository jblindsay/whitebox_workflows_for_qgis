from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = 'wk_dir'
rasters_1 = wbe.read_rasters(rasters1)
vector_2 = wbe.read_vector('points2')
(outputVector0, outputString1) = wbe.extract_raster_values_at_points(rasters_1, variable_name)
wbe.write_vector(outputVector0, 'fnOutput0')
with open('fnOutput1', 'w') as f:
    v = outputString1
    f.write(f"{v}")
wbe.check_in_license('license_id')
