"""
.. moduleauthor:: Enrico Garaldi <egaraldi@mpa-garching.mpg.de>
"""

__author__ = "Enrico Garaldi"

__license__ = "GPLv3"

__description__ ="""
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


import numpy as np
import os.path
import os
import itertools
import copy
import urllib
import zipfile
import sys
import datetime

from .DataEntryClass import DataEntry
from .FieldClass import Field
from .check_updates import _check_data_updates

#check for updates in data
_check_data_updates(force=False, silent=True)

#get version number
with open(os.path.join(os.path.dirname(__file__), 'version.py')) as f:  exec(f.read())

#get fields info
with open(os.path.join(os.path.dirname(__file__), 'fields_info.py')) as f:  exec(f.read())

       

__fields__ = list( __fields_info__.keys() )

__dicts__ = {}
for f in __fields__:
    __dicts__[f] = Field()
    __dicts__[f].field_symbol      = __fields_info__[f]["symbol"]
    __dicts__[f].field_description = __fields_info__[f]["description"]
    __dicts__[f].field_units       = __fields_info__[f]["units"]
    __dicts__[f].field_remarks     = __fields_info__[f]["remarks"]


def _LoadDataIntoDictionary(filepath, dictionary):
                
    if filepath.endswith(".py"):
        _LoadDataIntoDictionaryPy(filepath, dictionary)
    elif filepath.endswith(".ecsv"):
        _LoadDataIntoDictionaryECSV(filepath, dictionary)



def _LoadDataIntoDictionaryPy(filepath, dictionary):

    def _expand_field(field, shape):
        if field.size == 1:
            #if field==None or field==True or field==False:
            new_field = np.tile(field, shape)
            return new_field
        else:
            #return np.array(field).flatten()
            return field

    local_var_dict = {
#        "dictionary_tag"        : None,
#        "reference"             : None,
#        "url"                   : None,
#        "description"           : None,
#        "data_structure"        : None,
#        "extracted"             : None,
#        "ndim"                  : None,
#        "dimensions_descriptors": None,
#        "axes"                  : None,
#        "values"                : None,
#        "err_up"                : None,
#        "err_down"              : None,
#        "upper_lim"             : None,
#        "lower_lim"             : None
    }


    with open(filepath, "r") as f:
        exec(f.read(), globals(), local_var_dict)

    #retrieve variables and transform into np.array when appropriate
    dictionary_tag         =          local_var_dict["dictionary_tag"        ]               ; del local_var_dict["dictionary_tag"        ]
    reference              =          local_var_dict["reference"             ]               ; del local_var_dict["reference"             ]
    url                    =          local_var_dict["url"                   ]               ; del local_var_dict["url"                   ]
    description            =          local_var_dict["description"           ]               ; del local_var_dict["description"           ]
    data_structure         =          local_var_dict["data_structure"        ]               ; del local_var_dict["data_structure"        ]
    extracted              =          local_var_dict["extracted"             ]               ; del local_var_dict["extracted"             ]
    ndim                   =      int(local_var_dict["ndim"                  ] )             ; del local_var_dict["ndim"                  ]
    dimensions_descriptors = np.array(local_var_dict["dimensions_descriptors"] )             ; del local_var_dict["dimensions_descriptors"]
    axes                   = np.array(local_var_dict["axes"                  ], dtype='O' )  ; del local_var_dict["axes"                  ]
    values                 = np.array(local_var_dict["values"                ], dtype=float ); del local_var_dict["values"                ] 
    err_up                 = np.array(local_var_dict["err_up"                ], dtype=float ); del local_var_dict["err_up"                ]
    err_down               = np.array(local_var_dict["err_down"              ], dtype=float ); del local_var_dict["err_down"              ]
    upper_lim              = np.array(local_var_dict["upper_lim"             ], dtype=bool ) ; del local_var_dict["upper_lim"             ]
    lower_lim              = np.array(local_var_dict["lower_lim"             ], dtype=bool ) ; del local_var_dict["lower_lim"             ]
    #now process keys left, assuming they are arrays (or can be expanded to arrays)
    extra_data = {}
    for k in local_var_dict.keys():
        extra_data[k] = np.array(local_var_dict[k], dtype=object)

    #expand None's, True's, and False's (this will also convert them to array)
    err_up    = _expand_field(err_up   , values.shape)
    err_down  = _expand_field(err_down , values.shape)
    upper_lim = _expand_field(upper_lim, values.shape)
    lower_lim = _expand_field(lower_lim, values.shape)
    for k in extra_data.keys():
        extra_data[k] = _expand_field(extra_data[k], values.shape)
    

    #check dimension match
    assert( len(dimensions_descriptors) == ndim)
    if ndim == 0:
        assert( axes.shape[0] == 0 )
        #assert( values.shape[0] == 1 )
        for arr in [values, err_up, err_down, lower_lim, upper_lim]:
            assert( arr.shape[0] == 1 )
        for k in extra_data.keys():
            assert( extra_data[k].shape[0] == 1 )
    elif ndim == 1:
        assert( axes.ndim == ndim)
        #assert( np.squeeze(values.shape) == len(axes) )
        for arr in [values, err_up, err_down, lower_lim, upper_lim]:
            assert( np.squeeze(arr.shape) == len(axes) )
        for k in extra_data.keys():
            assert( np.squeeze(extra_data[k].shape) == len(axes) )
    else:
        if data_structure == "grid":
            assert( np.squeeze(axes.shape) == ndim )
            #assert( np.shape(values) == tuple(len(a) for a in axes) )
            for arr in [values, err_up, err_down, lower_lim, upper_lim]:
                assert( np.shape(arr) == tuple(len(a) for a in axes) )
            for k in extra_data.keys():
         #       assert( (np.shape(extra_data[k]) == tuple(len(a) for a in axes)) or \
         #               (np.squeeze(np.shape(extra_data[k])) == ndim) )
                assert( np.shape(extra_data[k]) == tuple(len(a) for a in axes) )
        elif data_structure == "points":
            assert( axes.shape[1] == ndim )
            Npts = axes.shape[0]
            #assert( len(values) == Npts )
            for arr in [values, err_up, err_down, lower_lim, upper_lim]:
                assert( len(arr) == Npts )
            for k in extra_data.keys():
                assert( len(extra_data[k]) == Npts )

    #transform a grid into a list
    if (ndim > 1) and (data_structure == 'grid'):
        values    = values   .flatten() 
        err_up    = err_up   .flatten() 
        err_down  = err_down .flatten() 
        lower_lim = lower_lim.flatten() 
        upper_lim = upper_lim.flatten() 
        new_axes  = np.empty((len(values), ndim), dtype='O')
        #_transform_extra_data = {}
        #_new_extra_data = {}
        for k in extra_data.keys():
            #if np.squeeze(np.shape(extra_data[k])) == ndim:
            #    _transform_extra_data[k] = True
            #    _new_extra_data[k] = np.empty((len(values), ndim), dtype='O')
            #else:
            #    _transform_extra_data[k] = False
            #    extra_data[k] = extra_data[k].flatten()
            extra_data[k] = extra_data[k].flatten()

        ranges = [range(len(ax)) for ax in axes]
        sizes  = [len(ax) for ax in axes]
        for r in itertools.product(*ranges):
            idx = 0
            for q in range(ndim):
                idx += int(r[q] * np.product( sizes[q+1:] ))
            for q in range(ndim):
                new_axes[idx, q] = axes[q][r[q]]
                #for k in extra_data.keys():
                #    if _transform_extra_data[k]:
                #        _new_extra_data[k][idx, q] = extra_data[k][q][r[q]]
        axes = new_axes
        #for k in extra_data.keys():
        #    if _transform_extra_data[k]:
        #        extra_data[k] = _new_extra_data[k]

    #ensure values has ndim==2, shape=(Npts, Ndim)
    #if ndim<2:
    #    axes = np.expand_dims(axes, axis=ndim)
    
    #filter out nan values
    w = np.isnan(values)
    if ndim>0:
        axes  = axes     [~w]
    values    = values   [~w]
    err_up    = err_up   [~w]
    err_down  = err_down [~w]
    upper_lim = upper_lim[~w]
    lower_lim = lower_lim[~w]
    for k in extra_data.keys():
        extra_data[k] = extra_data[k][~w]


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
                      upper_lim              = upper_lim,
                      lower_lim              = lower_lim,
                      extra_data             = extra_data
                     )


def _LoadDataIntoDictionaryECSV(filepath, dictionary):
    raise NotImplementedError      


def _LoadAllVariables(fields, dicts):
    for field in fields:
        datapath  = os.path.join(os.path.dirname(__file__), 'data')
        fieldpath = os.path.join(datapath, field)
        files = [i for i in os.listdir(fieldpath) if i.endswith(".py")]
        for filename in files:
            if filename=='__init__.py':
                continue
            filepath = os.path.join(fieldpath, filename)
            try:
                _LoadDataIntoDictionary(filepath, dicts[field])
            except:
                print(f"WARNING: Cannot load {filename}. Skipping it.")

####################
# PUBLIC FUNCTIONS #
####################


def fields():
    """List all available fields, i.e. physical quantities with available constraints.
    
    :return: A list of physical quantities with available constraints.
    :rtype: list of strings.
    """
    return copy.deepcopy(__fields__)

def get_all_dicts():
    """Returns all constraints dictionaries.
    
    :return: A list of all availabl dictionaries with constraints.
    :rtype: list of dict.
    """
    return copy.deepcopy(__dicts__)

def get(field):
    """Retrieve constraints for a single physical quantity.
    
    :param field: name of the physical parameter to retrieve limits from.
    :type field: str.
    :return: A dictionary of constraints.
    :rtype: dict (None if field is not available).
    """
    assert field in __fields__, 'ERROR: {0:} is not a valid field.'.format(field)
    return copy.deepcopy(__dicts__[field])

def print_all_entries():
    """Prints all entries available in corecon.
    """
    for field in __fields__:
        for k in __dicts__[field].keys():
            #if k=="description": continue
            print(field, ' > ', k)

def get_data_entry_template():
    """Returns a string containing the data entry template for adding new constraints.

    :return: a string containing the data entry template.
    :rtype: str.
    """
    datapath = os.path.join(os.path.dirname(__file__), 'data')
    filepath = os.path.join(datapath, 'data_entry_template.py')
    with open(filepath, 'r') as tf:
        fstring = tf.read()
    return(fstring)

def update_data():
    """Checks for updates in the available constraints (not of the package itself!) and 
    downloads them if available. Requires internet connection to the CoReCon's repository.
    """
    _check_data_updates(force=True)


_LoadAllVariables(__fields__, __dicts__)
