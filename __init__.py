"""
CoReCon
=====

CoReCon is an open collection of constraints on various physical quantities linked to the Epoch of Reionization (EoR).

It is built to be easily complemented by contribution from the scientific community, thanks to a simple data form that 
supports two different ways of input data.

CoReCon takes care of loading and interpreting the data, and presenting them in an organic and ready-to-use way. It also 
implement simple slicing capabilities, which allow to perform simple data filtering.
"""


__fields__ = ["ionized_fraction", "Lya_flux_ps", "mfp", "tau_eff_HI", "tau_eff_HeII", "eta", "qlf", "glf", "T0"] #, "tau_CMB", "ionizing_emissivity"



ionized_fraction = {}
Lya_flux_ps = {}
mfp = {}
tau_eff_HI = {}
tau_eff_HeII = {}
eta = {}
qlf = {}
glf = {}
T0 = {}
#tau_CMB = {}
#ionizing_emissivity = {}

__dicts__  = [ionized_fraction, Lya_flux_ps, mfp, tau_eff_HI, tau_eff_HeII, eta, qlf, glf, T0] #, tau_CMB, ionizing_emissivity

import numpy as np
import os.path
import os
import itertools
import copy

from .DataEntryClass import DataEntry


def _LoadDataIntoDictionary(filename, dictionary, parameter):

    def _expand_field(field, shape):
        if field==None or field==True or field==False:
            new_field = np.tile(field, shape)
            return new_field
        else:
            return np.array(field).flatten()
        

    local_var_dict = {
        "dictionary_tag"        : None,
        "reference"             : None,
        "description"           : None,
        "data_structure"        : None,
        "ndim"                  : None,
        "dimensions_descriptors": None,
        "axes"                  : None,
        "values"                : None,
        "err_up"                : None,
        "err_down"              : None,
        "err_up2"               : None,
        "err_down2"             : None,
        "upper_lim"             : None,
        "lower_lim"             : None
    }


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
    err_up    = _expand_field(err_up   , values.shape)
    err_down  = _expand_field(err_down , values.shape)
    err_up2   = _expand_field(err_up2  , values.shape)
    err_down2 = _expand_field(err_down2, values.shape)
    upper_lim = _expand_field(upper_lim, values.shape)
    lower_lim = _expand_field(lower_lim, values.shape)
    
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

def _LoadAllVariables(parameters, variables):
    for parameter, var in zip(parameters, variables):
        #print(parameter)
        datapath = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), parameter)
        files = [i for i in os.listdir(datapath) if i.endswith("py")]
        for file in files:
            if file=='__init__.py':
                continue
            #else:
            #    print(file)
            _LoadDataIntoDictionary(file, var, parameter)


####################
# PUBLIC FUNCTIONS #
####################

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


def get_available_fields():
    return copy.copy(__fields__)

def get_dict_from_field_name(field):
    if field in __fields__:
        w = np.where(np.array(__fields__) == field)[0][0]
        return __dicts__[w]
    else:
        return None



_LoadAllVariables(__fields__, __dicts__)
