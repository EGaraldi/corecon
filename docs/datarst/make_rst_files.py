import sys
sys.path.insert(1, '../../../')
import ReCon
import numpy as np


header = {"ionized_fraction" : "Ionised fraction", 
          "Lya_flux_ps"      : "Ly-alpha flux power spectrum", 
          "mfp"              : "Mean free path of ionising photons", 
          "tau_eff_HI"       : "HI Ly-alpha effective optical depth", 
          "tau_eff_HeII"     : "HeII Ly-alpha effective optical depth", 
          "eta"              : "Column density ratio", 
          "qlf"              : "Quasar luminosity function", 
          "T0"               : "IGM temperature at mean density", 
          "tau_CMB"          : "CMB optical depth", 
         }


for name, fdict in zip(ReCon.__fields__, ReCon.__dicts__):
    
    s = '''
%s
%s
.. image:: ../plots/%s.png
   :height: 200pt

Data sources
^^^^^^^^^^^^

'''%(header[name], "="*len(header[name]),  name)

    for ik, k in enumerate(fdict.keys()):
        s += '`%s <%s>`_\n\n'%(k, "http://www.arxiv.org")#fdict[k].link)
        
    with open(name+'.rst', 'w') as tf:
        tf.write(s)
