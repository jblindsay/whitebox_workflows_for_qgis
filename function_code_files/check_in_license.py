import os, sys
path = os.path.normpath(r"plugin_path")
if path not in sys.path:
    sys.path.append(path)

from whitebox_workflows import WbEnvironment

wbe = WbEnvironment()
check_in_str = 'success' 
num_checked_in = 0
while 'Unsuccessful' not in check_in_str:
    if len('id1') == 0:
        check_in_str = wbe.check_in_license('license_id')
    else:
        check_in_str = wbe.check_in_license('id1')

    if 'Unsuccessful' not in check_in_str:
         num_checked_in += 1

print('Num. successful license check-ins: ', num_checked_in)
