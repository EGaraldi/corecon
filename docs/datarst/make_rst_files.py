import sys
sys.path.insert(1, '../../')
import corecon as crc
import numpy as np

#get fields info
with open('../../corecon/fields_info.py') as f:  exec(f.read())

alldicts = crc.get_all_dicts()
for name in crc.fields():
    fdict = alldicts[name]

    s = '''.. _%s:

%s
%s
.. image:: ../plots/%s.png
   :height: 200pt

Data sources
^^^^^^^^^^^^

'''%(name, __fields_info__[name]["header"], "="*len(__fields_info__[name]["header"]), name)

    sorted_keys = list(fdict.keys())
    sorted_keys.sort()

    for ik, k in enumerate(sorted_keys):
        if k=="description":
            continue
        #s += '`%s <%s>`_\n\n'%(k, fdict[k].url)
        s += '|%s|\n\n.. |%s| raw:: html\n\n   <a href="%s" target="_blank">%s</a>\n\n'%(k, k, fdict[k].url, k)
        
    with open(name+'.rst', 'w') as tf:
        tf.write(s)
