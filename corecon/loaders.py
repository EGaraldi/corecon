import numpy as np
import os.path
import os
import itertools
import copy

from .DataEntryClass import DataEntry

#get build type
with open(os.path.join(os.path.dirname(__file__), 'build_type.py')) as f:  exec(f.read())

#get fields info
with open(os.path.join(os.path.dirname(__file__), 'fields_info.py')) as f:  exec(f.read())


def _LoadData(filepath):
                
    if filepath.endswith(".py"):
        data_entry = _LoadDataPy(filepath)
    elif filepath.endswith(".ecsv"):
        data_entry = _LoadDataECSV(filepath)
    elif filepath.endswith(".hdf5"):
        data_entry = _LoadDataHDF5(filepath)
    else:
        data_entry = None
    return data_entry


def _LoadDataPy(filepath):

    def _expand_field(field, shape):
        if field.size == 1:
            #if field==None or field==True or field==False:
            new_field = np.tile(field, shape)
            return new_field
        else:
            #return np.array(field).flatten()
            return field

    def _extract_item(dictionary, key):
        item = copy.copy(local_var_dict[key])
        if __build_type__ == 'DEBUG': print(f"  [debug] extracted {key} from local_var_dict as {item}")
        del local_var_dict[key]
        return item
    
    _mandatory_auxiliary_info = ["err_up", "err_down", "upper_lim", "lower_lim", "units"]
    def _is_mandatory_auxiliary_info(key):
        for mai in _mandatory_auxiliary_info:
            if key.endswith("_"+mai):
                return True
        #default option
        return False
    
    def _has_mandatory_auxiliary_info(key):
        for mai in _mandatory_auxiliary_info:
            if not key+"_"+mai in local_var_dict.keys():
                return False, mai
        #default option
        return True, None
    
    def _process_log_variable(var):
        var_nolog = var[4:]
        local_var_dict[var_nolog] = local_var_dict[var]
        del local_var_dict[var]
        for mai in _mandatory_auxiliary_info:
            local_var_dict[f"{var_nolog}_{mai}"] = local_var_dict[f"{var}_{mai}"]
            del local_var_dict[f"{var}_{mai}"]


    local_var_dict = {}
    with open(filepath, "r") as f:
        exec(f.read(), globals(), local_var_dict)

    dictionary_tag = _extract_item(local_var_dict, 'dictionary_tag')
    reference      = _extract_item(local_var_dict, 'reference'     )
    description    = _extract_item(local_var_dict, 'description'   )
    url            = _extract_item(local_var_dict, 'url'           )
    extracted      = _extract_item(local_var_dict, 'extracted'     )
    variable_list = []

    #build list of variable in the file
    for k in local_var_dict.keys():
        if not _is_mandatory_auxiliary_info(k):
            if __build_type__ == 'DEBUG': print(f"  [debug] Adding {k} to variable list")
            variable_list.append(k)

    #check that each variable has required fields
    #TODO: what about auxiliary fields that do not have errors, etc. -> maybe make exception for fields starting with "aux_"
    for variable in variable_list:
        has_mai, missing_mai = _has_mandatory_auxiliary_info(variable)
        if not has_mai:
            raise KeyError(f"{variable}_{missing_mai} not found! variables found {data_entry.variable_list}")

    #TODO: decide whether do this or keep "log_" in front of var name -- but what happens with required variables in fields?
    # #remove "log_" from front of variables and then store the info that they are log
    # for iv, variable in enumerate(variable_list):
    #     if variable.startswith("log_"):
    #         if __build_type__ == 'DEBUG': print(f"  [debug] marking {variable} as log")
    #         variable_list[iv] = variable[4:]
    #         _process_log_variable(variable)
    #         local_var_dict[f"{variable[4:]}_islog"] = True
    #     else:
    #         local_var_dict[f"{variable}_islog"] = False
    

    #transform into np arrays
    for k,v in local_var_dict.items():
        if __build_type__ == 'DEBUG': print(f"  [debug] transforming {k} into numpy array")
        local_var_dict[k] = np.array(v)

    #check that dimension match
    Npts = None        
    for k,v in local_var_dict.items():
        assert(v.ndim <= 1)
        if v.ndim == 0:
            #skip as this will be expanded later 
            pass
        elif v.ndim == 1:
            if Npts is None:
                Npts = len(v)
            else:
                assert(len(v)==Npts)
        else:
            raise ValueError(f"Entries must be 1- or 0-dimensional, but {k} has {v.ndim} dimensions!")

    #TODO: do I need this?
    #filter out nan values
    # w = np.isnan(values)
    # if ndim>0:
    #     axes  = axes     [~w]
    # values    = values   [~w]
    # err_up    = err_up   [~w]
    # err_down  = err_down [~w]
    # upper_lim = upper_lim[~w]
    # lower_lim = lower_lim[~w]
    # for k in extra_data.keys():
    #     extra_data[k] = extra_data[k][~w]

    #expand fields
    for k,v in local_var_dict.items():
        #exception for units
        if not k.endswith("_units"):
            local_var_dict[k] =  _expand_field(v, Npts)

    
    #place them in data_entry
    data_entry = DataEntry( dictionary_tag,
                            reference     = reference  ,
                            description   = description,
                            url           = url        ,
                            extracted     = extracted  ,
                            values        = local_var_dict,
                            variable_list = np.array(variable_list)
                          )
    
    return data_entry


def _LoadDataECSV(filepath):
    raise NotImplementedError   


def _LoadDataHDF5(filepath):
    raise NotImplementedError      


# def _LoadAllVariables(fields, dicts):
#     for field in fields:
#         datapath  = os.path.join(os.path.dirname(__file__), 'data')
#         fieldpath = os.path.join(datapath, field)
#         files = [i for i in os.listdir(fieldpath) if i.endswith(".py")]
#         for filename in files:
#             if filename=='__init__.py':
#                 continue
#             filepath = os.path.join(fieldpath, filename)
#             try:
#                 _LoadDataIntoDictionary(filepath, dicts[field], field)
#             except:
#                 print(f"WARNING: Cannot load {filename}. Skipping it.")


def DataHaveRequiredVariables(data_entry, field):
    for f in __fields_info__[field]["required_variables"]:
        if not f in data_entry.variable_list:
            return False
    return True

def RegisterDatainField(data_entry, field_dict):
    field_dict[data_entry.dictionary_tag] = data_entry


def _LoadAllVariables(fields, dicts):
    datapath  = os.path.join(os.path.dirname(__file__), 'data_sources')
    files = [i for i in os.listdir(datapath)]

    for filename in files:
        if filename=='__init__.py':
            continue
        filepath = os.path.join(datapath, filename)
        try:
            if __build_type__ == 'DEBUG': print('[debug] loading', filename)
            data_entry = _LoadData(filepath)

            if __build_type__ == 'DEBUG': 
                print(f"  [debug] loaded data_entry:")
                print(data_entry)

            for field in fields:
                if DataHaveRequiredVariables(data_entry, field):
                    if __build_type__ == 'DEBUG': print(f"  [debug] registering {data_entry.dictionary_tag} in field {field}")
                    RegisterDatainField(data_entry, dicts[field])
        except:
            print(f"WARNING: Cannot load {filename}. Skipping it.")