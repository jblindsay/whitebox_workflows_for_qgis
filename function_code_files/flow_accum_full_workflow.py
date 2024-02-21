import os, sys
path = os.path.normpath("plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath("wk_dir")
raster_1 = wbe.read_raster('dem1')
(outputRaster0, outputRaster1, outputRaster2) = wbe.flow_accum_full_workflow(raster_1, 'out_type2', log_transform3, clip4, esri_pntr5)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.write_raster(outputRaster2, 'fnOutput2', compress_raster)
wbe.check_in_license('license_id')
