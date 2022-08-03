import os
from urllib.request import urlretrieve
import zipfile
import sys
import datetime

def _check_data_updates(force=False, silent=False):

    if not silent: print("Checking for updates... ", end='')

    basepath = os.path.dirname(__file__)

    #check the time of the last update
    try:
        with open(os.path.join(basepath, 'time_of_last_update.dat'), 'r') as tf:
            time_of_last_update = datetime.datetime.strptime(tf.readlines()[0], "%Y-%m-%d-%H-%M-%S")
    except FileNotFoundError:
        time_of_last_update = datetime.datetime.strptime("1970-1-1-00-00-00", "%Y-%m-%d-%H-%M-%S")

    difference = datetime.datetime.now() - time_of_last_update

    if force or (difference.days >= 1): #UPDATE

        #retrieve updated data list
        try:
            if not silent: print("Updating available data... ")
            url = "https://raw.githubusercontent.com/EGaraldi/corecon/master/corecon/data/data.zip"
            datapath = os.path.join(basepath, 'data')
            output = os.path.join(datapath, 'data.zip')
            urlretrieve(url, output)

            #remove current data
            content = os.listdir(datapath)
            for c in content:
                cpath = os.path.join(datapath,c)
                if os.path.isdir(cpath):
                    ccontent = os.listdir(cpath)
                    for cc in ccontent:
                        if not cc.startswith("__"):
                            os.remove(os.path.join(cpath, cc))

            with zipfile.ZipFile(output, 'r') as zf:
                zf.extractall(path=datapath)

            #log time of last update
            with open(os.path.join(basepath, 'time_of_last_update.dat'), 'w') as tf:
                tf.write(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            
            if not silent: print("done!")

        except Exception as e:
            print("WARNING: Could not retrieve data.zip! "+str(e))
    else:
        if not silent: print("Nothing to be done! (the last update is more recent than 1 day, use the update_data function to force an update).")

    return
