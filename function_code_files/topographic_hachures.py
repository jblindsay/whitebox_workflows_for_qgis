import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"dem1")
outputVector = wbe.topographic_hachures(raster_1, contour_interval2, base_contour3, deflection_tolerance4, filter_size5, separation6, distmin7, distmax8, discretization9, turnmax10, slopemin11, depth12)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
