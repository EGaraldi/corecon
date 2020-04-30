import sys
sys.path.insert(1, '../../')
import corecon as crc
import numpy as np


header = {"ionized_fraction" : "Ionized fraction", 
          "Lya_flux_ps"      : "Ly-alpha flux power spectrum", 
          "mfp"              : "Mean free path of ionising photons", 
          "tau_eff_HI"       : "HI Ly-alpha effective optical depth", 
          "tau_eff_HeII"     : "HeII Ly-alpha effective optical depth", 
          "eta"              : "Column density ratio", 
          "qlf"              : "Quasar luminosity function", 
          "glf"              : "Galaxy luminosity function", 
          "T0"               : "IGM temperature at mean density", 
          "tau_CMB"          : "CMB optical depth", 
         }

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

'''%(name, header[name], "="*len(header[name]),  name)

    for ik, k in enumerate(fdict.keys()):
        if k=="description":
            continue
        #s += '`%s <%s>`_\n\n'%(k, fdict[k].url)
        s += '|%s|\n\n.. |%s| raw:: html\n\n   <a href="%s" target="_blank">%s</a>\n\n'%(k, k, fdict[k].url, k)
        
    with open(name+'.rst', 'w') as tf:
        tf.write(s)
