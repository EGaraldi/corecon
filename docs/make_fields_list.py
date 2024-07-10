import numpy as np

#get fields info
with open('../corecon/fields_info.py') as f:  exec(f.read())

with open('fields_list.rst', 'w') as tf:
    for f in __fields_info__.keys():
        tf.write("- :ref:`%s`\n"%f)
#        tf.write('`'+__fields_info__[f]["description"]+'`_\n')
#        tf.write('-'*(len(__fields_info__[f]["description"])+3)+'\n')
#        tf.write('\n')
#        tf.write('.. _'+__fields_info__[f]["description"]+f': datarst/{f}.html\n')
#        tf.write('\n')
#        tf.write('\n')
