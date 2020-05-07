"""
CoReCon
=======

CoReCon is an open collection of constraints on various physical quantities linked to the Epoch of Reionization (EoR).

It is built to be easily complemented by contribution from the scientific community, thanks to a simple data form that 
supports two different ways of input data.

CoReCon takes care of loading and interpreting the data, and presenting them in an organic and ready-to-use way. It also 
implement simple slicing capabilities, which allow to perform simple data filtering.

DISCLAIMER
^^^^^^^^^^
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Enrico Garaldi"

__license__ = "GPLv3"

__version__ = '0.2.2'



__fields__ = ["ionized_fraction", "Lya_flux_ps", "mfp", "tau_eff_HI", "tau_eff_HeII", "eta", "qlf", "glf", "T0", "tau_cmb"]

__descriptors__ = [r"$x_\mathrm{HII}$", r"$P\, [\mathrm{km/s}]$", r"$\lambda_\mathrm{mfp} \, [h^{-1} \, \mathrm{Mpc}]$", 
                   r"$\tau_\mathrm{eff, HI}$", r"$\tau_\mathrm{eff, HeII}$", r"$\eta$", 
                   r"$\log_{10} (phi_\mathrm{QSO}) \, [\mathrm{Mpc}^{-3} \, \mathrm{mag}^{-1}]$", 
                   r"$\log_{10} (phi_\mathrm{GAL}) \, [\mathrm{Mpc}^{-3} \, \mathrm{mag}^{-1}]$", "T0 [K]", 
                   r"$\tau_\mathrm{CMB}$"]

__dicts__ = {}
for f,d in zip(__fields__, __descriptors__):
    __dicts__[f] = {}
    __dicts__[f]["description"] = d


import numpy as np
import os.path
import os
import itertools
import copy

from .DataEntryClass import DataEntry


def _LoadDataIntoDictionary(filepath, dictionary):

    def _expand_field(field, shape):
        if field.size == 1:
            #if field==None or field==True or field==False:
            new_field = np.tile(field, shape)
            return new_field
        else:
            #return np.array(field).flatten()
            return field

    local_var_dict = {
        "dictionary_tag"        : None,
        "reference"             : None,
        "url"                   : None,
        "description"           : None,
        "data_structure"        : None,
        "extracted"             : None,
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


    with open(filepath, "r") as f:
        exec(f.read(), globals(), local_var_dict)

    #retrieve variables and transform into np.array when appropriate
    dictionary_tag         =          local_var_dict["dictionary_tag"        ]    
    reference              =          local_var_dict["reference"             ]    
    url                    =          local_var_dict["url"                   ]    
    description            =          local_var_dict["description"           ]    
    data_structure         =          local_var_dict["data_structure"        ]    
    extracted              =          local_var_dict["extracted"             ]    
    ndim                   =      int(local_var_dict["ndim"                  ] )  
    dimensions_descriptors = np.array(local_var_dict["dimensions_descriptors"] )  
    axes                   = np.array(local_var_dict["axes"                  ], dtype='O' )  
    values                 = np.array(local_var_dict["values"                ], dtype=float )  
    err_up                 = np.array(local_var_dict["err_up"                ], dtype=float ) 
    err_down               = np.array(local_var_dict["err_down"              ], dtype=float ) 
    err_up2                = np.array(local_var_dict["err_up2"               ], dtype=float ) 
    err_down2              = np.array(local_var_dict["err_down2"             ], dtype=float ) 
    upper_lim              = np.array(local_var_dict["upper_lim"             ], dtype=bool )
    lower_lim              = np.array(local_var_dict["lower_lim"             ], dtype=bool )


    #expand None's, True's, and False's (this will also convert them to array)
    err_up    = _expand_field(err_up   , values.shape)
    err_down  = _expand_field(err_down , values.shape)
    err_up2   = _expand_field(err_up2  , values.shape)
    err_down2 = _expand_field(err_down2, values.shape)
    upper_lim = _expand_field(upper_lim, values.shape)
    lower_lim = _expand_field(lower_lim, values.shape)
    

    #check dimension match
    assert( len(dimensions_descriptors) == ndim)
    if ndim == 0:
        assert( axes.shape[0] == 0 )
        #assert( values.shape[0] == 1 )
        for arr in [values, err_up, err_down, err_up2, err_down2, lower_lim, upper_lim]:
            assert( arr.shape[0] == 1 )
    elif ndim == 1:
        assert( axes.ndim == ndim)
        #assert( np.squeeze(values.shape) == len(axes) )
        for arr in [values, err_up, err_down, err_up2, err_down2, lower_lim, upper_lim]:
            assert( np.squeeze(arr.shape) == len(axes) )
    else:
        if data_structure == "grid":
            assert( np.squeeze(axes.shape) == ndim )
            #assert( np.shape(values) == tuple(len(a) for a in axes) )
            for arr in [values, err_up, err_down, err_up2, err_down2, lower_lim, upper_lim]:
                assert( np.shape(arr) == tuple(len(a) for a in axes) )
        elif data_structure == "points":
            assert( axes.shape[1] == ndim )
            Npts = axes.shape[0]
            #assert( len(values) == Npts )
            for arr in [values, err_up, err_down, err_up2, err_down2, lower_lim, upper_lim]:
                assert( len(arr) == Npts )

    #transform a grid into a list
    if (ndim > 1) and (data_structure == 'grid'):
        values    = values   .flatten() 
        err_up    = err_up   .flatten() 
        err_down  = err_down .flatten() 
        err_up2   = err_up2  .flatten() 
        err_down2 = err_down2.flatten() 
        lower_lim = lower_lim.flatten() 
        upper_lim = upper_lim.flatten() 
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

    #ensure values has ndim==2, shape=(Npts, Ndim)
    if ndim<2:
        axes = np.expand_dims(axes, axis=ndim)
    
    #filter out nan values
    w = np.isnan(values)
    axes      = axes     [~w]
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
                      url                    = url,        
                      ndim                   = ndim,
                      dimensions_descriptors = dimensions_descriptors,
                      extracted              = extracted,
                      axes                   = axes,
                      values                 = values,
                      err_up                 = err_up,
                      err_down               = err_down,
                      err_up2                = err_up2,
                      err_down2              = err_down2,
                      upper_lim              = upper_lim,
                      lower_lim              = lower_lim
                     )

def _LoadAllVariables(fields, dicts):
    for field in fields:
        datapath  = os.path.join(os.path.dirname(__file__), 'data')
        fieldpath = os.path.join(datapath, field)
        files = [i for i in os.listdir(fieldpath) if i.endswith("py")]
        for filename in files:
            if filename=='__init__.py':
                continue
            filepath = os.path.join(fieldpath, filename)
            _LoadDataIntoDictionary(filepath, dicts[field])


####################
# PUBLIC FUNCTIONS #
####################

def get_redshift_range(field, zmin, zmax):
    '''
    Returns all the datapoint for a given parameter that lie in a redshift range zmin <= z < zmax
    Parameters:
     field[string] : name of the physical parameter to retrieve
     zmin[float] : lower edge of the redshift range
     zmax[float] : upper edge of the redshift range
    '''

    dict_zslice = {}

    try:
        d = __dicts__[field]
    except KeyError:
        print("ERROR: field %s not found!"%field)
        return {}

    for k in d.keys():
        if k=="description":
            continue
        w = (d[k].dimensions_descriptors == 'redshift')
        if not any(w):
            print("WARNING: missing redshift dimension for entry %s. Skipping it."%(k))
            continue
        zdim = np.where(w)[0][0]
        
        if d[k].ndim == 1:
            redshift = d[k].axes
        else:
            redshift = d[k].axes[:,zdim]

        w = (zmin <= redshift) & (redshift < zmax)
        if any(w):
            dict_zslice[k] = DataEntry(
                      reference              = d[k].reference,
                      url                    = d[k].url,      
                      description            = d[k].description,
                      ndim                   = d[k].ndim,
                      dimensions_descriptors = d[k].dimensions_descriptors,
                      extracted              = d[k].extracted,
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

def get_lower_limits(field):
    '''
    Returns all the lower limits for a given parameter
    Parameters:
     field[string] : name of the physical parameter to retrieve
    '''

    dict_lls = {}

    try:
        d = __dicts__[field]
    except KeyError:
        print("ERROR: field %s not found!"%field)
        return {}

    for k in d.keys():
        if k=="description":
            continue
        
        if any(d[k].lower_lim):
            dict_lls[k] = DataEntry(
                      reference              = d[k].reference,
                      url                    = d[k].url,      
                      description            = d[k].description,
                      ndim                   = d[k].ndim,
                      dimensions_descriptors = d[k].dimensions_descriptors,
                      extracted              = d[k].extracted,
                      axes                   = d[k].axes     [d[k].lower_lim],
                      values                 = d[k].values   [d[k].lower_lim],
                      err_up                 = d[k].err_up   [d[k].lower_lim],
                      err_down               = d[k].err_down [d[k].lower_lim],
                      err_up2                = d[k].err_up2  [d[k].lower_lim],
                      err_down2              = d[k].err_down2[d[k].lower_lim],
                      upper_lim              = d[k].upper_lim[d[k].lower_lim],
                      lower_lim              = d[k].lower_lim[d[k].lower_lim]
                     )

    return dict_lls

def get_upper_limits(field):
    '''
    Returns all the lower limits for a given parameter
    Parameters:
     field[string] : name of the physical parameter to retrieve
    '''

    dict_uls = {}

    try:
        d = __dicts__[field]
    except KeyError:
        print("ERROR: field %s not found!"%field)
        return {}

    for k in d.keys():
        if k=="description":
            continue
        
        if any(d[k].upper_lim):
            dict_uls[k] = DataEntry(
                      reference              = d[k].reference,
                      url                    = d[k].url,      
                      description            = d[k].description,
                      ndim                   = d[k].ndim,
                      dimensions_descriptors = d[k].dimensions_descriptors,
                      extracted              = d[k].extracted,
                      axes                   = d[k].axes     [d[k].upper_lim],
                      values                 = d[k].values   [d[k].upper_lim],
                      err_up                 = d[k].err_up   [d[k].upper_lim],
                      err_down               = d[k].err_down [d[k].upper_lim],
                      err_up2                = d[k].err_up2  [d[k].upper_lim],
                      err_down2              = d[k].err_down2[d[k].upper_lim],
                      upper_lim              = d[k].upper_lim[d[k].upper_lim],
                      lower_lim              = d[k].lower_lim[d[k].upper_lim]
                     )

    return dict_uls


def fields():
    return copy.deepcopy(__fields__)

def get_all_dicts():
    return copy.deepcopy(__dicts__)

def get(field):
    if field in __fields__:
        return copy.deepcopy(__dicts__[field])
    else:
        return None

def print_all_entries():
    for field in __fields__:
        for k in __dicts__[field].keys():
            if k=="description":
                continue
            print(field, ' > ', k)

def get_data_entry_template():
    datapath = os.path.join(os.path.dirname(__file__), 'data')
    filepath = os.path.join(datapath, 'data_entry_template.py')
    with open(filepath, 'r') as tf:
        fstring = tf.read()
    return(fstring)

_LoadAllVariables(__fields__, __dicts__)
