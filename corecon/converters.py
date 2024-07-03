import numpy as np
import os
import copy
import os.path
import itertools

###################
# OldDataEntry CLASS #
###################


class OldDataEntry:
    """Class representing a single constraint.
    """

    def __init__(self, 
                 dictionary_tag         = None,
                 ndim                   = None,  
                 description            = None,  
                 reference              = None,
                 parent_field           = None,
                 url                    = None,
                 dimensions_descriptors = None,  
                 extracted              = None,
                 axes                   = None,  
                 values                 = None,  
                 err_up                 = None,  
                 err_down               = None,  
                 upper_lim              = None,  
                 lower_lim              = None,
                 extra_data             = None ):
        """construct method
        """
        self.dictionary_tag         = dictionary_tag
        self.ndim                   = ndim                  
        self.description            = description           
        self.reference              = reference              
        self.parent_field           = parent_field             
        self.url                    = url                   
        self.dimensions_descriptors = dimensions_descriptors
        self.extracted              = extracted
        self.axes                   = axes                  
        self.values                 = values                
        self.err_up                 = err_up                
        self.err_down               = err_down              
        self.upper_lim              = upper_lim             
        self.lower_lim              = lower_lim             
        self.extra_data = []
        if extra_data is not None:
            for k in extra_data.keys():
                setattr(self, k, extra_data[k])
                self.extra_data.append(k)
        self.extra_data = np.array(self.extra_data)

        #create named entries
        setattr(self, parent_field, values[:])
        for k, descr in enumerate(dimensions_descriptors):
            descr = _sanitize_variable_name(descr)
            dimensions_descriptors[k] = descr
            if ndim==1:
                setattr(self, descr, axes)
                if 'err_left' in self.extra_data:
                    setattr(self, descr+"_err_down", self.err_left)
                if 'err_right' in self.extra_data:
                    setattr(self, descr+"_err_up", self.err_right)
                if 'axes_upper_lim' in self.extra_data:
                    setattr(self, descr+"_upper_lim", self.axes_upper_lim)
                if 'axes_lower_lim' in self.extra_data:
                    setattr(self, descr+"_lower_lim", self.axes_lower_lim)
            else:
                setattr(self, descr, axes[:,k])
                if 'err_left' in self.extra_data:
                    setattr(self, descr+"_err_down", self.err_left[:,k])
                if 'err_right' in self.extra_data:
                    setattr(self, descr+"_err_up", self.err_right[:,k])
                if 'axes_upper_lim' in self.extra_data:
                    setattr(self, descr+"_upper_lim", self.axes_upper_lim[:,k])
                if 'axes_lower_lim' in self.extra_data:
                    setattr(self, descr+"_lower_lim", self.axes_lower_lim[:,k])


    def __repr__(self):
        """string describing the class
        """
        return "corecon OldDataEntry class"

    def __str__(self):
        """output of print
        """

        ostr=""
        ostr +=                       "ndim                   = %i\n"%self.ndim                  
        ostr +=                       "description            = %s\n"%_insert_blank_spaces(self.description, 25)
        ostr +=                       "reference              = %s\n"%self.reference             
        ostr +=                       "parent_field           = %s\n"%self.parent_field             
        ostr +=                       "url                    = %s\n"%self.url                   
        ostr +=                       "extracted              = %s\n"%self.extracted             
        ostr += _get_str_from_array1d("dimensions_descriptors = ", self.dimensions_descriptors)
        ostr += _get_str_from_array  ("axes                   = ", self.axes     )
        ostr += _get_str_from_array1d("values                 = ", self.values   )
        ostr += _get_str_from_array1d("err_up                 = ", self.err_up   )
        ostr += _get_str_from_array1d("err_down               = ", self.err_down )
        ostr += _get_str_from_array1d("upper_lim              = ", self.upper_lim)
        ostr += _get_str_from_array1d("lower_lim              = ", self.lower_lim)
        for ed in self.extra_data:
            ostr += _get_str_from_array1d(ed+" "*max(0,23-len(ed))+"= ", getattr(self, ed) )
        return ostr

    def __eq__(self,other):
        """custom equality definition
        """

        #need to check extra_fields here
        if len(self.extra_data) != len(other.extra_data):
            return False
        else:
            for s,o in zip(self.extra_data, other.extra_data):
                if (s != o) or ( np.any(getattr(self,s) != getattr(other,o)) ):
                    return False
            #all ok for extra_data, now check the rest
            return(
                               (self.ndim                   == other.ndim                                     ) & \
                               (self.description            == other.description                              ) & \
                               (self.reference              == other.reference                                ) & \
                               (self.parent_field           == other.parent_field                             ) & \
                               (self.url                    == other.url                                      ) & \
                               (self.extracted              == other.extracted                                ) & \
                    np.all     (self.dimensions_descriptors == other.dimensions_descriptors                   ) & \
                    np.all     (self.axes                   == other.axes                                     ) & \
                    np.allclose(self.values                 ,  other.values                 , equal_nan=True  ) & \
                    np.allclose(self.err_up                 ,  other.err_up                 , equal_nan=True  ) & \
                    np.allclose(self.err_down               ,  other.err_down               , equal_nan=True  ) & \
                    np.all     (self.upper_lim              == other.upper_lim                                ) & \
                    np.all     (self.lower_lim              == other.lower_lim                                ) )

    def swap_limits(self):
        """Swap upper and lower limits. Useful when computing a derived quantity.
        """
        ul_copy = copy.deepcopy(self.upper_lim)
        self.upper_lim = copy.deepcopy(self.lower_lim)
        self.lower_lim = copy.deepcopy(ul_copy)

    def swap_errors(self):
        """Swap upper and lower errors. Useful when computing a derived quantity.
        """
        eu_copy = copy.deepcopy(self.err_up)
        self.err_up   = copy.deepcopy(self.err_down)
        self.err_down = copy.deepcopy(eu_copy)

    #def none_to_value(self, value):
    #    for f in [self.values, self.err_up, self.err_down]:
    #        w = (f == None)
    #        f[w] = value

    #def none_to_nan(self):
    #    self.none_to_value(np.nan)
    
    def nan_to_values(self, array, new_vals):
        """Replaces all NaN with values.

        :param array: (list of) variable name(s) to work on. Use 'all' to replace NaNs in all array variables.
        :type array: (list of) str
        :param new_vals: value(s) to replace the NaNs with. If a np.array, it should have the correct dimension, i.e. the same as the number of NaNs.
        :type new_vals: float or np.array
        """
        #if array=='values' or array=='all':
        #    w = np.isnan(self.values)
        #    self.values[w] = new_vals
        #if array=='err_up' or array=='all':
        #    w = np.isnan(self.err_up)
        #    self.err_up[w] = new_vals
        #if array=='err_down' or array=='all':
        #    w = np.isnan(self.err_down)
        #    self.err_down[w] = new_vals
        if isinstance(array, str):
            if array=='all':
                names = []
                names.append('values')
                names.append('err_up')
                names.append('err_down')
                for k in self.extra_data:
                    if isinstance(getattr(self,k), np.ndarray):
                        names.append(k)
            else:
                names = [array]
        elif (isinstance(array, list) or isinstance(array, tuple)):
            names = array
        else:
            print("ERROR: the argument 'array' should be a string or a list/tuple of strings!")
            return

        for name in names:
            v = getattr(self, name)
            v[np.isnan(v)] = new_vals
            setattr(self, name, v)

    def set_lim_errors(self, newval, frac_of_values=False):
        """Set the value of error arrays for upper and lower limits.

        :param newval: value to assign to the error arrays.
        :type newval: float
        :param frac_of_values: if True, newval \*= values.
        :type frac_of_values: bool, optional
        """
        w = (self.upper_lim|self.lower_lim)
        if frac_of_values:
            newval *= self.values[w]
        self.err_up   [w] = newval
        self.err_down [w] = newval

    def list_attributes(self):
        """List the attributes for the current entry.
        """
        return list(self.__dict__.keys())
    


def _OldLoadDataIntoDictionary(filepath, parent_field):
                
    if filepath.endswith(".py"):
        return _OldLoadDataIntoDictionaryPy(filepath, parent_field)
    elif filepath.endswith(".ecsv"):
        return _OldLoadDataIntoDictionaryECSV(filepath, parent_field)



def _OldLoadDataIntoDictionaryPy(filepath, parent_field):

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
                if k=='err_left' or k=='err_right':
                    continue
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
        if 'err_left' in extra_data.keys():
            new_err_left = np.empty((len(values), ndim), dtype='O')
        if 'err_right' in extra_data.keys():
            new_err_right = np.empty((len(values), ndim), dtype='O')
        #_transform_extra_data = {}
        #_new_extra_data = {}
        for k in extra_data.keys():
            if k=='err_left' or k=='err_right':
                continue
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
                if 'err_left' in extra_data.keys():
                    new_err_left[idx, q] = extra_data['err_left'][q][r[q]]
                if 'err_right' in extra_data.keys():
                    new_err_right[idx, q] = extra_data['err_right'][q][r[q]]
                #for k in extra_data.keys():
                #    if _transform_extra_data[k]:
                #        _new_extra_data[k][idx, q] = extra_data[k][q][r[q]]
        axes = new_axes
        if 'err_left' in extra_data.keys():
            extra_data['err_left'] = new_err_left
        if 'err_right' in extra_data.keys():
            extra_data['err_right'] = new_err_right
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


    return OldDataEntry(
                      dictionary_tag         = dictionary_tag,
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


def _OldLoadDataIntoDictionaryECSV(filepath, dictionary, parent_field):
    raise NotImplementedError      


def _OldLoadAllVariables(fields, dicts):
    for field in fields:
        datapath  = os.path.join(os.path.dirname(__file__), 'data')
        fieldpath = os.path.join(datapath, field)
        files = [i for i in os.listdir(fieldpath) if i.endswith(".py")]
        for filename in files:
            if filename=='__init__.py':
                continue
            filepath = os.path.join(fieldpath, filename)
            try:
                _OldLoadDataIntoDictionary(filepath, dicts[field], field)
            except:
                print(f"WARNING: Cannot load {filename}. Skipping it.")


def _sanitize_variable_name(vname):
    vname = vname.replace(" ", "_")
    vname = ''.join(ch if ch.isalnum() or ch=="_" else '' for ch in vname)
    return vname
    

def _insert_blank_spaces(string, nblanks):
    ns = string
    l = 0
    for c in string:
        if c=='\n':
            ns = ns[:l+1] + (' '*nblanks) + ns[l+1:] 
            l += nblanks
        l += 1
    return ns


def _get_str_from_array1d(prefix, arr, truncate=-1):
    s = "%s[ "%prefix
    if truncate > 0:
        irange = range(min(len(arr), truncate))
    else:
        irange = range(len(arr))
    for i in irange:
        if arr[i]==np.inf:
            s += "np.inf, "
        elif isinstance(arr[i], str):
            s += "'%s', "%arr[i]
        else:
            s += "%s, "%arr[i]
    #remove last comma
    s = s[:-2]+" "
    if truncate > 0:
        s += "... "
    s += "]\n"
    return s


def _get_str_from_multiarray(prefix, marr, truncate=-1):
    s = "%s[ "%prefix
    if truncate > 0:
        rowrange = range(min(marr.shape[0], truncate))
    else:
        rowrange = range(marr.shape[0])
    for row in rowrange:
        local_prefix = " "*(len(prefix)+2) if row > 0 else ""
        s += _get_str_from_array(local_prefix, marr[row, ...], truncate=truncate)
    if truncate > 0:
        s += " "*(len(prefix)+2)+"...\n"
    s += " "*len(prefix) + "]\n"
    return s


def _get_str_from_array(prefix, arr, truncate=-1):
    if arr is np.nan:
        return prefix+"NaN\n"
    elif arr.ndim==1:
        return _get_str_from_array1d(prefix, arr, truncate=truncate)
    else:
        return _get_str_from_multiarray(prefix, arr, truncate=truncate)



def _SaveDataIntoFilePy(data, newfile_name):

    with open(newfile_name, 'w') as newf:
        
        for key in ['dictionary_tag', 'reference', 'url', 'extracted']:
            newf.write(f"{key.ljust(30)}= '{getattr(data, key)}'\n\n")

        newf.write(f"{'description'.ljust(30)}= \\\n'''{getattr(data, 'description')}'''\n\n")
        
        for key in data.dimensions_descriptors:
            newf.write(_get_str_from_array1d(f"{key.ljust(30)}= ", getattr(data, key)))
            for e in ["_err_up", "_err_down"]:
                ekey = key+e
                #here using default value for getattr to deal with cases where there's no ekey
                newf.write(_get_str_from_array1d(f"{ekey.ljust(30)}= ", getattr(data, ekey, np.zeros_like(getattr(data, key)))))
            for e in ["_upper_lim", "_lower_lim"]:
                ekey = key+e
                #always False for these fields
                newf.write(f"{ekey.ljust(30)}= False\n")
            newf.write("\n")

        
        key = data.parent_field
        newf.write(_get_str_from_array1d(f"{key.ljust(30)}= ", getattr(data, 'values')))
        for e in ["err_up", "err_down"]:
            ekey = key+"_"+e
            #here using default testdir/test_H18.pyvalue for getattr to deal with cases where there's no ekey
            newf.write(_get_str_from_array1d(f"{ekey.ljust(30)}= ", getattr(data, e)))
        for e in ["upper_lim", "lower_lim"]:
            ekey = key+"_"+e
            #always False for these fields
            newf.write(_get_str_from_array1d(f"{ekey.ljust(30)}= ", getattr(data, e)))
        newf.write("\n")
        
        for key in data.extra_data:
            if key.startswith("err_up_") or key.startswith("err_down_") or \
               key.startswith("upper_lim_") or key.startswith("lower_lim_") or \
               key=='err_left' or key=='err_right' or \
               key=='err_up2' or key=='err_down2' or \
               key=='axes_lower_lim' or key=='axes_upper_lim':
                continue
            else:
                newf.write(_get_str_from_array1d(f"{key.ljust(30)}= ", getattr(data, key)))
                for e in ["err_up", "err_down"]:
                    ekey = key+"_"+e
                    #here using default value for getattr to deal with cases where there's no ekey
                    newf.write(_get_str_from_array1d(f"{ekey.ljust(30)}= ", getattr(data, e+"_"+key, np.zeros_like(getattr(data, key)))))
                for e in ["upper_lim", "lower_lim"]:
                    ekey = key+"_"+e
                    #always False for these fields
                    newf.write(_get_str_from_array1d(f"{ekey.ljust(30)}= ", getattr(data, e+"_"+key, np.zeros_like(getattr(data, key)).astype(bool))))
                newf.write("\n")


def ConvertOldFileToNewFile(oldfile_path, oldfile_field, newfile_name):
    try:
        data = _OldLoadDataIntoDictionary(oldfile_path, oldfile_field)
        _SaveDataIntoFilePy(data, newfile_name)
    except:
        raise Exception(f"WARNING: Cannot load {oldfile_path}!")

    
def ConvertAllOldFilesToNewFiles(oldfile_basepath, newfile_path):
    fields = [i for i in os.listdir(oldfile_basepath)]
    newfiles_created = []
    for field in fields:
        if field.startswith("__") or field == 'data.zip' or field == 'make_data_archive.py' or field=='data_entry_template.py':
            continue

        print(f"Converting field: {field}".ljust(80))
        fieldpath = os.path.join(oldfile_basepath, field)
        files = [i for i in os.listdir(fieldpath) if i.endswith(".py")]
        for filename in files:
            
            if filename=='__init__.py':
                continue

            print(f"  converting {filename}")#, end='\r')

            filepath = os.path.join(fieldpath, filename)
            newfile_name = os.path.join(newfile_path, filename)

            #avoid over-writing duplicates
            exist = newfile_name in newfiles_created
            app = 0
            while(exist):
                if app==0:
                    print(f"-- INFO: {filename} exists already. Appending {app}")
                    newfile_name = newfile_name[:-3]+'-'+str(app)+newfile_name[-3:]
                else:
                    print(f"-- INFO: {filename} exists already. Appending {app}")
                    newfile_name = newfile_name[:-4-len(str(app))]+'-'+str(app)+newfile_name[-3:]
                exist = newfile_name in newfiles_created
                app += 1

            newfiles_created.append(newfile_name)

            try:
                ConvertOldFileToNewFile(filepath, field, newfile_name)
            except:
                print(f"===== WARNING: Cannot load {filename}!")
    