import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment, WbPalette
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster('left_raster1')
raster_2 = wbe.read_raster('right_raster2')
wbe.image_slider(raster_1, raster_2, 'output_html_file3', left_palette4, left_reverse_palette5, 'left_label6', right_palette7, right_reverse_palette8, 'right_label9', image_height10)
wbe.check_in_license('license_id')
