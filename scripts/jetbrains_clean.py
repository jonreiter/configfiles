import argparse
import os
import shutil

def main():

    # Toolbox old app versions
    base_dir = os.environ["HOME"]
    apps_dir = base_dir + '/.local/share/JetBrains/Toolbox/apps'
    cache_dir = base_dir + '/.cache/JetBrains'

    parser = argparse.ArgumentParser()
    parser.add_argument('--appsdir', type=str, default=apps_dir)
    parser.add_argument('--cachedir', type=str, default=cache_dir)
    parser.add_argument('--cleanapps', type=bool, default=False)
    parser.add_argument('--cleancache', type=bool, default=False)
    args = parser.parse_args()

    if args.cleanapps:
        apps = os.listdir(args.appsdir)
        skip_list = ["Toolbox"]
        ndel = 0
        for app in apps:
            if app in skip_list:
                continue
            subdir = args.appsdir + '/' + app + '/ch-0/'
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
            print('Toolbox clean')

    # cache old versions
    if args.cleancache:
        cache_entires_raw = os.listdir(args.cachedir)
        cache_entries = {}
        for e in cache_entires_raw:
            f = e.split('.')
            f_year = f[0][-4:]
            f_stub = f[0][:-4]
            f_suffix = f_year + '.' + f[1]
            if f_stub not in cache_entries:
                cache_entries[f_stub] = [f_suffix]
            else:
                cache_entries[f_stub].append(f_suffix)
        ndel = 0
        for k in cache_entries:
            cache_entries[k].sort()
            to_delete = cache_entries[k][:-1]
            for subdir_suffix in to_delete:
                subdir_name = k + subdir_suffix
                dir_to_del = args.cachedir + '/' + subdir_name
                try:
                    ndel += 1
                    shutil.rmtree(dir_to_del, ignore_errors=True)
                    os.remove(dir_to_del)
                except OSError as e:
                    pass
        if ndel == 0:
            print('cache clean')

main()
