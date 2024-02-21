import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import download_sample_data, WbEnvironment
wbe = WbEnvironment()
wbe.verbose = True
wbe.working_directory = download_sample_data('dataset_nm')
print(f'Data have been stored in: {wbe.working_directory}')