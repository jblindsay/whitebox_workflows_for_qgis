import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

import whitebox_workflows
from whitebox_workflows import WbEnvironment

wbe = WbEnvironment()
print(wbe.version())
print(whitebox_workflows.__file__)
