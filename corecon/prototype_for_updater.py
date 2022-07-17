import urllib
import yaml
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
        baseurl = "https://raw.githubusercontent.com/EGaraldi/corecon/master/corecon/data/"
        baseoutput = "./data/"

        print("Updating available data...")
        url = os.path.join(baseurl,"/data.yaml")
        output = os.path.join(baseoutput,"/data.yaml")
        urllib.request.urlretrieve(url, output)

        #retrieve content
        with open("data/data.yaml", 'r') as f:
            data = yaml.safe_load(f)

        for d in data.keys(): 
            try: 
                newdir = os.path.join(baseoutput, d)
                os.mkdir(newdir) 
            except FileExistsError: 
                pass 
            except Exception as e: 
                raise SystemError("ERROR: could not create a directory within data/! "+str(e))

            for f in data[d]:
                try:
                    relative_path = os.path.join(d, f)
                    url = os.path.join(baseurl, relative_path)
                    output = os.path.join(baseoutput,relative_path)
                    urllib.request.urlretrieve(url, output)
                except Exception as e:
                    raise SystemError(f"ERROR: Could not retrieve {relative_path}! "+str(e))
        
        #log time of last update
        with open('time_of_last_update.dat', 'w') as tf:
            tf.write(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    except Exception as e:
        raise SystemError("ERROR: Could not retrieve data.yaml! "+str(e))
