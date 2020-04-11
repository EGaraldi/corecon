__fields__ = ["ionized_fraction", "Lya_flux_ps", "mfp", "tau_eff_HI", "tau_eff_HeII", "eta", "qlf", "T0"] #, "tau_CMB", "ionizing_emissivity"
ionized_fraction = {}
Lya_flux_ps = {}
mfp = {}
tau_eff_HI = {}
tau_eff_HeII = {}
eta = {}
qlf = {}
T0 = {}
#tau_CMB = {}
#ionizing_emissivity = {}

__dicts__  = [ionized_fraction, Lya_flux_ps, mfp, tau_eff_HI, tau_eff_HeII, eta, qlf, T0] #, tau_CMB, ionizing_emissivity

import numpy as np
import os.path
import os
import itertools
import copy

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

    def expand_field(field, shape):
        if field==None or field==True or field==False:
            new_field = np.tile(field, shape)
            return new_field
        else:
            return np.array(field).flatten()
        

    local_var_dict = {}

    file_full_path = os.path.join(os.path.dirname(__file__), 'data')
    file_full_path = os.path.join(file_full_path, parameter)
    file_full_path = os.path.join(file_full_path, filename)
    with open(file_full_path, "r") as f:
        exec(f.read(), globals(), local_var_dict)

    #retrieve variables and transform into np.array when appropriate
    dictionary_tag         =          local_var_dict["dictionary_tag"        ]    
    reference              =          local_var_dict["reference"             ]    
    description            =          local_var_dict["description"           ]    
    data_structure         =          local_var_dict["data_structure"        ]    
    ndim                   =      int(local_var_dict["ndim"                  ] )  
    dimensions_descriptors = np.array(local_var_dict["dimensions_descriptors"] )  
    axes                   = np.array(local_var_dict["axes"                  ], dtype='O' )  
    values                 = np.array(local_var_dict["values"                ], dtype='float' )  
    err_up                 =          local_var_dict["err_up"                ] # this will be treated later 
    err_down               =          local_var_dict["err_down"              ] # this will be treated later 
    err_up2                =          local_var_dict["err_up2"               ] # this will be treated later 
    err_down2              =          local_var_dict["err_down2"             ] # this will be treated later 
    upper_lim              =          local_var_dict["upper_lim"             ] # this will be treated later
    lower_lim              =          local_var_dict["lower_lim"             ] # this will be treated later
    

    #check dimension match
    assert( len(dimensions_descriptors) == ndim)
    if ndim == 1:
        assert( axes.ndim == ndim)
        assert( np.squeeze(values.shape) == len(axes) )
    else:
        if data_structure == "grid":
            assert( np.squeeze(axes.shape) == ndim )
            assert( np.shape(values) == tuple(len(a) for a in axes) )
        elif data_structure == "points":
            assert( axes.shape[1] == ndim )
            Npts = axes.shape[0]
            assert( len(values) == Npts )


    #transform a grid into a list
    if (ndim > 1) and (data_structure == 'grid'):
        values = values.flatten()
        new_axes = np.empty((len(values), ndim), dtype='O')
        
        ranges = [range(len(ax)) for ax in axes]
        sizes  = [len(ax) for ax in axes]
        for r in itertools.product(*ranges):
            idx = 0
            for q in range(ndim):
                idx += int(r[q] * np.product( sizes[q+1:] ))
            for q in range(ndim):
                new_axes[idx, q] = axes[q][r[q]]
        axes = new_axes
    

    #expand None's, True's, and False's (this will also convert them to array)
    err_up    = expand_field(err_up   , values.shape)
    err_down  = expand_field(err_down , values.shape)
    err_up2   = expand_field(err_up2  , values.shape)
    err_down2 = expand_field(err_down2, values.shape)
    upper_lim = expand_field(upper_lim, values.shape)
    lower_lim = expand_field(lower_lim, values.shape)
    
    #filter out None values
    w = (values == None)
    values    = values   [~w]
    err_up    = err_up   [~w]
    err_down  = err_down [~w]
    err_up2   = err_up2  [~w]
    err_down2 = err_down2[~w]
    upper_lim = upper_lim[~w]
    lower_lim = lower_lim[~w]


    dictionary[dictionary_tag] = \
            DataEntry(
                      reference              = reference,
                      description            = description,
                      ndim                   = ndim,
                      dimensions_descriptors = dimensions_descriptors,
                      axes                   = axes,
                      values                 = values,
                      err_up                 = err_up,
                      err_down               = err_down,
                      err_up2                = err_up2,
                      err_down2              = err_down2,
                      upper_lim              = upper_lim,
                      lower_lim              = lower_lim
                     )

def LoadAllVariables(parameters, variables):
    for parameter, var in zip(parameters, variables):
        #print(parameter)
        datapath = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), parameter)
        files = [i for i in os.listdir(datapath) if i.endswith("py")]
        for file in files:
            LoadDataIntoDictionary(file, var, parameter)

def Filter(diction, redshift):
    
    for key in diction:
        n = diction[key].ndim
        if(n==1):
            if(redshift in diction[key].axes):
                print("-- "+str(diction[key].reference)+" "+str(diction[key].axes[diction[key].axes.tolist().index(redshift)]))  


def get_redhift_range(parameter, zmin, zmax):
    '''
    Returns all the datapoint for a given parameter between that lie in a redshift range zmin <= z < zmax
    Parameters:
     parameter[string] : name of the physical parameter to retrieve
     zmin[float] : lower edge of the redshift range
     zmax[float] : upper edge of the redshift range
    '''

    dict_zslice = {}

    w = (np.array(__fields__) == parameter)
    if any(w):
        idx = np.where(w)[0][0]
        d = __dicts__[idx]
    else:
        print("ERROR: parameter %s not found!"%parameter)
        return {}

    for k in d.keys():
        w = (d[k].dimensions_descriptors == 'redshift')
        if not any(w):
            print("ERROR: missing redshift dimension for entry %s"%(k))
        zdim = np.where(w)[0][0]
        
        if d[k].ndim == 1:
            redshift = d[k].axes
        else:
            redshift = d[k].axes[:,zdim]

        w = (zmin <= redshift) & (redshift < zmax)
        if any(w):
            dict_zslice[k] = DataEntry(
                      reference              = d[k].reference,
                      description            = d[k].description,
                      ndim                   = d[k].ndim,
                      dimensions_descriptors = d[k].dimensions_descriptors,
                      axes                   = d[k].axes[w],
                      values                 = d[k].values[w],
                      err_up                 = d[k].err_up[w],
                      err_down               = d[k].err_down[w],
                      err_up2                = d[k].err_up2[w],
                      err_down2              = d[k].err_down2[w],
                      upper_lim              = d[k].upper_lim[w],
                      lower_lim              = d[k].lower_lim[w]
                     )

    return dict_zslice

LoadAllVariables(__fields__, __dicts__)
