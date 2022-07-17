import urllib
#import yaml
import zipfile
import os
import sys
import datetime

#check the time of the last update
with open('time_of_last_update.dat', 'r') as tf:
    time_of_last_update = datetime.datetime.strptime(tf.readlines()[0], "%Y-%m-%d-%H-%M-%S")

difference = datetime.datetime.now() - time_of_last_update

if difference.days >= 1: #UPDATE

    #retrieve updated data list
    try:
        print("Updating available data...")
        url = "https://raw.githubusercontent.com/EGaraldi/corecon/master/corecon/data/data.zip"
        output = os.path.join(os.path.join('.', 'data'), 'data.zip')
        urllib.request.urlretrieve(url, output)

        with zipfile.ZipFile(output, 'r') as zf:
            zf.extractall(path=os.path.join('.', 'data'))

        #log time of last update
        with open('time_of_last_update.dat', 'w') as tf:
            tf.write(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    except Exception as e:
        raise SystemError("ERROR: Could not retrieve data.yaml! "+str(e))

