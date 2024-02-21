import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

import whitebox_workflows
whitebox_workflows.activate_license(
key=key1,
firstname=firstName2,
lastname=lastName3,
email=email4,
agree_to_license_terms=agreeToTerms5
)
