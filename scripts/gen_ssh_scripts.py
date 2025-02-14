import argparse
import json
import os
import stat

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--configfile", type=str, default="config.json")
    parser.add_argument("--scriptdir", type=str, default=os.environ["HOME"]+ "/bin/")
    args = parser.parse_args()

    with open(args.configfile) as f:
        d = json.load(f)
    for e in d:
        this_name = e['name']
        this_host = e['host']
        this_user = e['user']
        this_port = e['port']
        this_file = args.scriptdir + "ssh-" + this_name
        with open(this_file, 'w') as g:
            g.write(f"""#!/bin/bash
    
    HOST={this_host}
    USER={this_user}
    PORT={this_port}
    
    ssh -C -X -p ${{PORT}} ${{USER}}@${{HOST}}
    """)
        st = os.stat(this_file)
        os.chmod(this_file, st.st_mode | stat.S_IEXEC)

main()
