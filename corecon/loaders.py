import numpy as np
import os.path
import os
import itertools

from .DataEntryClass import DataEntry

def _LoadDataIntoDictionary(filepath, dictionary, parent_field):
                
    if filepath.endswith(".py"):
        _LoadDataIntoDictionaryPy(filepath, dictionary, parent_field)
    elif filepath.endswith(".ecsv"):
        _LoadDataIntoDictionaryECSV(filepath, dictionary,parent_field)



def _LoadDataIntoDictionaryPy(filepath, dictionary, parent_field):

    def _expand_field(field, shape):
        if field.size == 1:
            #if field==None or field==True or field==False:
            new_field = np.tile(field, shape)
            return new_field
        else:
            #return np.array(field).flatten()
            return field

    local_var_dict = {}


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

    #special treatment for 1-dim data
    #if ndim == 1:
    #    axes = axes.reshape((*axes.shape,1))


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
                idx += int(r[q] * np.prod( sizes[q+1:] ))
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
                      parent_field           = parent_field,
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


def _LoadDataIntoDictionaryECSV(filepath, dictionary, parent_field):
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
                _LoadDataIntoDictionary(filepath, dicts[field], field)
            except:
                print(f"WARNING: Cannot load {filename}. Skipping it.")
