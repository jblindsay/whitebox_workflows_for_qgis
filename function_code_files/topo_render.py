import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster(r"dem1")
vector_6 = wbe.read_vector(r"clipping_polygon6")
outputRaster = wbe.topo_render(raster_1, palette2, reverse_palette3, azimuth4, altitude5, vector_6, background_hgt_offset7, background_clr8, attenuation_parameter9, ambient_light10, z_factor11)
wbe.write_raster(outputRaster, 'fnOutput', compress_raster)
wbe.check_in_license('license_id')
