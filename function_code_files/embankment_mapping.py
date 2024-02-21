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
vector_2 = wbe.read_vector('roads_vector2')
(outputRaster0, outputRaster1) = wbe.embankment_mapping(raster_1, vector_2, search_dist3, min_road_width4, typical_embankment_width5, typical_embankment_max_height6, embankment_max_width7, max_upwards_increment8, spillout_slope9, remove_embankments10)
wbe.write_raster(outputRaster0, 'fnOutput0', compress_raster)
wbe.write_raster(outputRaster1, 'fnOutput1', compress_raster)
wbe.check_in_license('license_id')
