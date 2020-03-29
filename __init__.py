__all__ = ["quasar_luminosity_function", "UVBG", "tau_CMB", "tau_effHI", "tau_effHeII", "ion_frac", "Lya_flux_PS", "T0", "eta", "ionizing_emissivity"]

import numpy as np
import os.path
import os

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
    
    def get_ref(self):
        return self.reference

    def __repr__(self):
        """string describing the class"""
        return "ReCon DataEntry class"

    def __str__(self):
        """output of print"""
        def insert_blank_spaces(string, nblanks):
            ns = string
            l = 0
            for c in string:
                if c=='\n':
                    ns = ns[:l+1] + (' '*nblanks) + ns[l+1:] 
                    l += nblanks
                l += 1
            return ns

        def get_str_from_array1d(prefix, arr):
            s = "%s[ "%prefix
            for i in range(min(len(arr), 3)):
                if i < len(arr)-1:
                    s += "%s, "%arr[i]
                else:
                    s += "%s "%arr[i]
            if len(arr) > 3:
                s += "... "
            s += "]\n"
            return s
        
        def get_str_from_multiarray(prefix, marr):
            s = "%s[ "%prefix
            for d in range(self.ndim):
                if d>0: s += " "*(len(prefix)+2)
                s += get_str_from_array1d("", marr[d])+"\n"
            s += " "*len(prefix) + "]\n"
            return s

        def get_str_from_array(prefix, arr):
            if arr is None:
                return prefix+"None\n"
            elif self.ndim==1:
                return get_str_from_array1d(prefix, arr)
            else:
                return get_str_from_multiarray(prefix, arr)

        ostr=""
        ostr += "ndim                   = %i\n"%self.ndim                  
        ostr += "description            = %s\n"%insert_blank_spaces(self.description, 25)
        ostr += "reference              = %s\n"%self.reference             
        ostr += get_str_from_array1d("dimensions_descriptors = ", self.dimensions_descriptors)
        ostr += get_str_from_array("axes                   = ", self.axes                  )
        ostr += get_str_from_array("values                 = ", self.values                )
        ostr += get_str_from_array("err_up                 = ", self.err_up                )
        ostr += get_str_from_array("err_down               = ", self.err_down              )
        ostr += get_str_from_array("err_up2                = ", self.err_up2               )
        ostr += get_str_from_array("err_down2              = ", self.err_down2             )
        ostr += get_str_from_array("upper_lim              = ", self.upper_lim             )
        ostr += get_str_from_array("lower_lim              = ", self.lower_lim             )
        return ostr

    def __eq__(self,other):
        """custom equality"""
        def compare_arrays(a,b):
            if a is None:
                if b is None:
                    return True
                else:
                    return False
            elif b is None:
                return False
            elif len(a)!=len(b):
                return False
            else:
                for i in range(len(a)):
                    if a[i] != b[i]:
                        return False
                return True

        return(
                              (self.ndim                 == other.ndim                   ) & \
                              (self.description          == other.description            ) & \
                              (self.reference            == other.reference              ) & \
                compare_arrays(self.dimensions_descriptors, other.dimensions_descriptors ) & \
                compare_arrays(self.axes                  , other.axes                   ) & \
                compare_arrays(self.values                , other.values                 ) & \
                compare_arrays(self.err_up                , other.err_up                 ) & \
                compare_arrays(self.err_down              , other.err_down               ) & \
                compare_arrays(self.err_up2               , other.err_up2                ) & \
                compare_arrays(self.err_down2             , other.err_down2              ) & \
                compare_arrays(self.upper_lim             , other.upper_lim              ) & \
                compare_arrays(self.lower_lim             , other.lower_lim              ) )

def LoadDataIntoDictionary(filename, dictionary, parameter):

    local_var_dict = {}

    file_full_path = os.path.join(os.path.dirname(__file__), parameter)
    file_full_path = os.path.join(file_full_path, filename)
    with open(file_full_path, "r") as f:
        exec(f.read(), globals(), local_var_dict)
    #print(local_var_dict)
    dictionary[local_var_dict["dictionary_tag"]] = \
            DataEntry(reference              =          local_var_dict["reference"             ]    ,
                      description            =          local_var_dict["description"           ]    ,
                      ndim                   =      int(local_var_dict["ndim"                  ] )  ,
                      dimensions_descriptors = np.array(local_var_dict["dimensions_descriptors"] )  ,
                      axes                   = np.array(local_var_dict["axes"                  ] )  ,
                      values                 = np.array(local_var_dict["values"                ] )  ,
                      err_up                 = np.array(local_var_dict["err_up"                ] ) if local_var_dict["err_up"   ] is not None else None ,
                      err_down               = np.array(local_var_dict["err_down"              ] ) if local_var_dict["err_down" ] is not None else None ,
                      err_up2                = np.array(local_var_dict["err_up2"               ] ) if local_var_dict["err_up2"  ] is not None else None ,
                      err_down2              = np.array(local_var_dict["err_down2"             ] ) if local_var_dict["err_down2"] is not None else None ,
                      upper_lim              = np.array(local_var_dict["upper_lim"             ] )  ,
                      lower_lim              = np.array(local_var_dict["lower_lim"             ] )  )   

def LoadAllVariables(parameters, variables):
    for parameter, var in zip(parameters, variables):
        files = [i for i in os.listdir(os.path.join(os.path.dirname(__file__), parameter)) if i.endswith("py")]
        for file in files:
            LoadDataIntoDictionary(file, var, parameter)

def Filter(diction, redshift):
    
    for key in diction:
        n = diction[key].ndim
        if(n==1):
            if(redshift in diction[key].axes):
                print("-- "+str(diction[key].reference)+" "+str(diction[key].axes[diction[key].axes.tolist().index(redshift)]))  

ion_frac = {}
flux_ps = {}
mfp = {}
taueffHI = {}
taueffHeII = {}

dictionaries = [ion_frac, flux_ps, mfp, taueffHI, taueffHeII]

# __all__ will replace parameters when all the data has been collected
parameters = ["ion_frac", "flux_ps", "mfp", "taueffHI", "taueffHeII"]


LoadAllVariables(parameters, dictionaries)
#print(flux_ps["McDonald et al. 2006"].err_down)
#Filter(ion_frac, 7.0)

#in flux PS, k is in h/Mpc  <-- need a way to write this
