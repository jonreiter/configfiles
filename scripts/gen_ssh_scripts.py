import json
import os
import stat

configfile="config.json"
scriptdir=os.environ['HOME'] + '/bin/'

with open(configfile) as f:
    d = json.load(f)
for e in d:
    this_name = e['name']
    this_host = e['host']
    this_user = e['user']
    this_port = e['port']
    this_file = scriptdir + this_name
    with open(this_file, 'w') as g:
        g.write(f"""#!/bin/bash

HOST={this_host}
USER={this_user}
PORT={this_port}

ssh -C -X -p ${{PORT}} ${{USER}}@${{HOST}}
""")
    st = os.stat(this_file)
    os.chmod(this_file, st.st_mode | stat.S_IEXEC)


