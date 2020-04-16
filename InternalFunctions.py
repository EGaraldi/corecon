import numpy as np
import os.path
import os
import itertools
import copy

from .DataEntryClass import DataEntry

######################
# INTERNAL FUNCTIONS #
######################
def _insert_blank_spaces(string, nblanks):
    ns = string
    l = 0
    for c in string:
        if c=='\n':
            ns = ns[:l+1] + (' '*nblanks) + ns[l+1:] 
            l += nblanks
        l += 1
    return ns


def _get_str_from_array1d(prefix, arr):
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


def _get_str_from_multiarray(prefix, marr):
    s = "%s[ "%prefix
    for d in range(self.ndim):
        if d>0: s += " "*(len(prefix)+2)
        s += _get_str_from_array1d("", marr[d])+"\n"
    s += " "*len(prefix) + "]\n"
    return s


def _get_str_from_array(prefix, arr):
    if arr is None:
        return prefix+"None\n"
    elif self.ndim==1:
        return _get_str_from_array1d(prefix, arr)
    else:
        return _get_str_from_multiarray(prefix, arr)


def _compare_arrays(a,b):
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


def _LoadDataIntoDictionary(filename, dictionary, parameter):

    def _expand_field(field, shape):
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
            _LoadDataIntoDictionary(file, var, parameter)


#def _Filter(diction, redshift):
#    
#    for key in diction:
#        n = diction[key].ndim
#        if(n==1):
#            if(redshift in diction[key].axes):
#                print("-- "+str(diction[key].reference)+" "+str(diction[key].axes[diction[key].axes.tolist().index(redshift)]))  
