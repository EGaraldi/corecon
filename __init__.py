"""
ReCon
=====

ReCon is an open collection of constraints on various physical quantities linked to the Epoch of Reionization (EoR).

It is built to be easily complemented by contribution from the scientific community, thanks to a simple data form that 
supports two different ways of input data.

ReCon takes care of loading and interpreting the data, and presenting them in an organic and ready-to-use way. It also 
implement simple slicing capabilities, which allow to perform simple data filtering.
"""


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

from ReCon.InternalFunctions import _insert_blank_spaces, _get_str_from_array1d, _get_str_from_multiarray, _get_str_from_array, _compare_arrays, _LoadDataIntoDictionary, _LoadAllVariables
from ReCon.DataEntryClass import DataEntry


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
