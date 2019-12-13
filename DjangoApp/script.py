#import numpy as np
import os.path
import os
import sqlite3
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('/ion_frac')

conn = sqlite3.connect('dbExperiment.sqlite3')
c = conn.cursor()

parameters = ["ion_frac"]


for parameter in parameters:
    files = [i for i in os.listdir(parameter) if i.endswith("py")]
    print(files)
    for file in files:
        file = file[:-3]
        temp = str('ion_frac/'+file)
        x = __import__(temp)
        print(x.reference)




#c.execute()
