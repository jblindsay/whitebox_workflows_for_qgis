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
(outputRaster0, outputRaster1) = wbe.local_hypsometric_analysis(raster_1, min_scale2, step_size3, num_steps4, step_nonlinearity5)
wbe.write_raster(outputRaster0, r"fnOutput0", compress_raster)
wbe.write_raster(outputRaster1, r"fnOutput1", compress_raster)
wbe.check_in_license('license_id')
