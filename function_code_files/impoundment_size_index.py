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
(outputRaster0, outputRaster1, outputRaster2, outputRaster3, outputRaster4) = wbe.impoundment_size_index(raster_1, max_dam_length2, output_mean3, output_max4, output_volume5, output_area6, output_height7)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.write_raster(outputRaster2, 'fnOutput2', compress_raster)
wbe.write_raster(outputRaster3, 'fnOutput3', compress_raster)
wbe.write_raster(outputRaster4, 'fnOutput4', compress_raster)
wbe.check_in_license('license_id')
