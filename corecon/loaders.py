import numpy as np
import os.path
import os
import itertools

from .DataEntryClass import DataEntry

def _LoadData(filepath):
                
    if filepath.endswith(".py"):
        _LoadDataPy(filepath)
    elif filepath.endswith(".ecsv"):
        _LoadDataECSV(filepath)
    elif filepath.endswith(".hdf5"):
        _LoadDataHDF5(filepath)
    else:
        return


def _LoadDataPy(filepath):

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

    dictionary_tag = local_var_dict['dictionary_tag'] ; del local_var_dict['dictionary_tag']
    reference      = local_var_dict['reference']      ; del local_var_dict['reference']
    description    = local_var_dict['description']    ; del local_var_dict['description']
    url            = local_var_dict['url']            ; del local_var_dict['url']
    extracted      = local_var_dict['extracted']      ; del local_var_dict['extracted']


    mandatory_auxiliary_info = ["err_up", "err_down", "upper_limit", "lower_limit", "units"]
    #build list of variable in the file
    for k in local_var_dict.keys():
        for mai in mandatory_auxiliary_info:
            if k.endswith("_"+mai):
                continue
        data_entry.variable_list.append(k)

    #check that each variable has required fields
    #TODO: what about auxiliary fields that do not have errors, etc. -> maybe make exception for fields starting with "aux_"
    for variable in data_entry.variable_list:
        for mai in mandatory_auxiliary_info:
            if not variable+"_"+mai in local_var_dict.keys():
                raise KeyError(variable+"_"+mai+" not found!")
    

    #check that dimension match
    Npts = None        
    for k in local_var_dict.keys():
        assert(k.ndim == 1)
        #skip values that will be expanded later
        if len(k) > 1:
            if Npts is None:
                Npts = len(k)
            else:
                assert(len(k)==Npts)

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
    for k in local_var_dict.keys():
        local_var_dict[k] =  _expand_field(local_var_dict[k], Npts)

    
    #place them in data_entry
    data_entry = DataEntry( dictionary_tag,
                            reference   = reference  ,
                            description = description,
                            url         = url        ,
                            extracted   = extracted  ,
                            values      = local_var_dict
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


def DataHaveRequiredVariables(data_dict, field):
    for f in __fields_info__[field]["required_variables"]:
        if not f in data_dict.variable_list:
            return False
    return True

def RegisterDatainField(data_dict, field):
    raise NotImplementedError
    #something like:
    #field.available_constrain.append(data_dict)


def _LoadAllVariables(fields, dicts):
    datapath  = os.path.join(os.path.dirname(__file__), 'data_sources')
    files = [i for i in os.listdir(datapath)]

    for filename in files:
        if filename=='__init__.py':
            continue
        filepath = os.path.join(fieldpath, filename)
        try:
            data_dict = _LoadData(filepath)
        except:
            print(f"WARNING: Cannot load {filename}. Skipping it.")

        for field in fields:
            if DataHaveRequiredVariables(data_dict, field):
                RegisterDatainField(data_dict, field)