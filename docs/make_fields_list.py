import numpy as np

#get fields info
with open('../corecon/fields_info.py') as f:  exec(f.read())

with open('fields_list.rst', 'w') as tf:
    for f in __fields_info__.keys():
        tf.write("- :ref:`%s`\n"%f)

