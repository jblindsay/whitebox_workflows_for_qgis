from whitebox_workflows import WbEnvironment
# from processing.core.ProcessingConfig import ProcessingConfig, Setting
import inspect, markdown, os

def helpPath():
    return os.path.normpath(os.path.join(os.path.dirname(__file__), 'help'))

licenseId = 'geog3430-f23'
# licenseId = ProcessingConfig.getSetting('FLOATING_LICENSE_ID')
# if len(licenseId) == 0:
#     licenseId = None
wbe = WbEnvironment(licenseId)

# Get the list of functions
method_list = inspect.getmembers(WbEnvironment)

for i in range(len(method_list)):
    method_nm = method_list[i][0]
    if not method_nm.startswith("__"):
        method = method_list[i][1]
        if method.__doc__ != None and len(method.__doc__) > 10:
            print(f"{method_nm} ({inspect.getfile(method)})")
            # print(inspect.getdoc(method))
            # s = inspect.signature(method)
            # print(s.parameters)
            # print(inspect.getargspec(method))

            docs = method.__doc__

            if len(docs.strip()) > 0:
                help = markdown.markdown(docs).replace("\n", "").replace("tool_help.md", "https://www.whiteboxgeo.com/manual/wbw-user-manual/book/tool_help.html")

                help += '''
<div align="center">
    <ul>
        <li><a href="https://www.whiteboxgeo.com/whitebox-workflows-for-python/">WbW Homepage</a></li>
        <li><a href="https://www.whiteboxgeo.com/manual/wbw-user-manual/book/preface.html">User Manual</a></li>
        <li><a href="https://www.whiteboxgeo.com/wbw-purchase/">Support WbW</a></li>
    </ul>
</div>        
'''

                helpFile = os.path.join(helpPath(), f"{method_nm}.html")

                with open(helpFile, "w") as f:
                    f.write(help)

print('Done!')