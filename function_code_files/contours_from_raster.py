import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster('raster_surface1')
outputVector = wbe.contours_from_raster(raster_1, contour_interval2, base_contour3, smoothing_filter_size4, deflection_tolerance5)
wbe.write_vector(outputVector, 'fnOutput')
wbe.check_in_license('license_id')
