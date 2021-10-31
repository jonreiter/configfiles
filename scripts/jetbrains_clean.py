import argparse
import os
import shutil

def main():
    base_dir = os.environ["HOME"]
    apps_dir = base_dir + '/.local/share/JetBrains/Toolbox/apps'

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default=apps_dir)
    args = parser.parse_args()

    apps = os.listdir(args.dir)
    skip_list = ["Toolbox"]
    ndel = 0
    for app in apps:
        if app in skip_list:
            continue
        subdir = args.dir + '/' + app + '/ch-0/'
        sublist = os.listdir(subdir)
        vers = []
        for f in sublist:
            if f.find(".vmoptions") != -1:
                i = f.find(".vmoptions")
                ver = f[0:i]
                vers.append(ver)
        vers=list(set(vers))
        vers.sort()
        # only keep latest version
        for i in range(len(vers)-1):
            this_v = vers[i]
            suffixes = ['', '.vmoptions', '.plugins', '.vmoptions.port']
            ndel += 1
            for suffix in suffixes:
                dir_to_del = args.dir + '/' + app + '/ch-0/' + this_v + suffix
                print("deleting: " + dir_to_del)
                shutil.rmtree(dir_to_del, ignore_errors=True)
                try:
                    os.remove(dir_to_del)
                except OSError as e:
                    pass

    if ndel == 0:
        print('clean')

main()
