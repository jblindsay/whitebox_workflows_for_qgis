import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment
wbe = WbEnvironment('license_id')
wbe.verbose = True
wbe.max_procs = max_threads
wbe.working_directory = os.path.normpath(r"wk_dir")
raster_1 = wbe.read_raster('dem1')
raster_2 = wbe.read_raster('streams_raster2')
(outputFloat0, outputFloat1, outputFloat2, outputFloat3) = wbe.horton_ratios(raster_1, raster_2)
print(f"bifurcation_ratio: {outputFloat0}")
print(f"length_ratio: {outputFloat1}")
print(f"area_ratio: {outputFloat2}")
print(f"slope_ratio: {outputFloat3}")
wbe.check_in_license('license_id')
