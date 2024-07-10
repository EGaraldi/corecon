import sys
sys.path.insert(1, '../../')
import corecon as crc
import numpy as np

#get fields info
with open('../../corecon/fields_info.py') as f:  exec(f.read())

alldicts = crc.get_all_dicts()
for name in crc.get_fields():
    print(name)
    fdict = alldicts[name]

    output_string = f'.. _{name}:\n\n'
    output_string += __fields_info__[name]["description"]+'\n'
    output_string += '='*len(__fields_info__[name]["description"])+'\n\n'

    output_string += '**Field names**: \n'
    output_string += f'"{name}", '

    synonyms = crc.get_field_synonyms(name)
    for synonym in synonyms:
        output_string += f'"{synonym}", '
    
    output_string = output_string[:-2] + "\n\n"#remove last ", "


    output_string += '**Units**: \n'
    output_string += __fields_info__[name]["units"]+'\n\n'

    output_string += '**Remarks**: \n'
    output_string += __fields_info__[name]["remarks"]+'\n\n'

    output_string += '**Required fields**: \n'
    for rf in __fields_info__[name]["required_fields"]:
        output_string += f'"{rf}", '
    if len(__fields_info__[name]["required_fields"]) > 0:
        output_string = output_string[:-2] + "\n\n" #remove last ", "

    output_string += f'''
    
Data
^^^^

.. raw:: html
    :file: ../plots/{name}.html

**Data sources**

'''

    sorted_keys = list(fdict.keys())
    sorted_keys.sort()

    for ik, k in enumerate(sorted_keys):
        #if k=="description": continue
        #s += '`%s <%s>`_\n\n'%(k, fdict[k].url)
        output_string += '|%s|\n\n.. |%s| raw:: html\n\n   <a href="%s" target="_blank">%s</a>\n\n'%(k, k, fdict[k].url, k)
        
    with open(name+'.rst', 'w') as tf:
        tf.write(output_string)
