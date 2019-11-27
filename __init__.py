__all__ = ["quasar_luminosity_function", "UVBG", "tau_CMB", "tau_effHI", "tau_effHeII", "ion_frac", "Lya_flux_PS", "T0", "eta"]

import numpy as np
import os.path

class DataEntry:

    def __init__(self, 
                 ndim                   = None,  
                 description            = None,  
                 reference              = None,    
                 dimensions_descriptors = None,  
                 axes                   = None,  
                 values                 = None,  
                 err_up                 = None,  
                 err_down               = None,  
                 err_up2                = None,  
                 err_down2              = None,  
                 upper_lim              = None,  
                 lower_lim              = None):

        self.ndim                   = ndim                  
        self.description            = description           
        self.reference              = reference             
        self.dimensions_descriptors = dimensions_descriptors
        self.axes                   = axes                  
        self.values                 = values                
        self.err_up                 = err_up                
        self.err_down               = err_down              
        self.err_up2                = err_up2               
        self.err_down2              = err_down2             
        self.upper_lim              = upper_lim             
        self.lower_lim              = lower_lim             


def LoadDataIntoDictionary(filename, dictionary):

    local_var_dict = {}

    file_full_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_full_path, "r") as f:
        exec(f.read(), globals(), local_var_dict)

    dictionary[local_var_dict["dictionary_tag"]] = \
            DataEntry(reference   =          local_var_dict["reference"  ]    ,
                      description =          local_var_dict["description"]    ,
                      values      = np.array(local_var_dict["values"     ] )  ,
                      err_up      = np.array(local_var_dict["err_up"     ] )  ,
                      err_down    = np.array(local_var_dict["err_down"   ] )  ,
                      err_up2     = np.array(local_var_dict["err_up2"    ] )  ,
                      err_down2   = np.array(local_var_dict["err_down2"  ] )  ,
                      upp_lim     = np.array(local_var_dict["upper_lim"  ] )  ,
                      low_lim     = np.array(local_var_dict["lower_lim"  ] )  )   





ion_frac = {}

LoadDataIntoDictionary('ion_frac/Fan_et_al_2006.py', ion_frac)


#in flux PS, k is in h/Mpc  <-- need a way to wirte this
