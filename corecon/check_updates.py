import urllib
import zipfile
import os
import sys
import datetime


def check_data_updates(force=False):
    #check the time of the last update
    try:
        with open('time_of_last_update.dat', 'r') as tf:
            time_of_last_update = datetime.datetime.strptime(tf.readlines()[0], "%Y-%m-%d-%H-%M-%S")
    except FileNotFoundError:
        time_of_last_update = datetime.datetime.strptime("1970-1-1-00-00-00", "%Y-%m-%d-%H-%M-%S")

    difference = datetime.datetime.now() - time_of_last_update

    if force or difference.days >= 1: #UPDATE

        #retrieve updated data list
        try:
            print("Updating available data...")
            #url = "https://raw.githubusercontent.com/EGaraldi/corecon/master/corecon/data/data.zip"
            url = "https://raw.githubusercontent.com/EGaraldi/corecon/auto-update/corecon/data/data.zip"
            output = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'data.zip')
            urllib.request.urlretrieve(url, output)

            with zipfile.ZipFile(output, 'r') as zf:
                zf.extractall(path=os.path.join(os.path.dirname(__file__), 'data'))

            #log time of last update
            with open('time_of_last_update.dat', 'w') as tf:
                tf.write(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

        except Exception as e:
            raise SystemError("ERROR: Could not retrieve data.zip! "+str(e))
    return
