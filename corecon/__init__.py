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
import copy

from .FieldClass import Field
from .DataEntryClass import DataEntry
from .check_updates import _check_data_updates
from .loaders import _LoadAllVariables

#check for updates in data
_check_data_updates(force=False, silent=True)

#get version number
with open(os.path.join(os.path.dirname(__file__), 'version.py')) as f:  exec(f.read())

#get fields info
with open(os.path.join(os.path.dirname(__file__), 'fields_info.py')) as f:  exec(f.read())

       

__fields__ = list( __fields_info__.keys() )

#build synonyms->key map
__synonym_to_key__ = {}
__all_synonyms__ = []
for f in __fields__:
    __synonym_to_key__[f] = f
    __all_synonyms__.append(f)
    for s in __fields_info__[f]["synonyms"]:
        __synonym_to_key__[s] = f
        __all_synonyms__.append(s)

__dicts__ = {}
for f in __fields__:
    __dicts__[f] = Field()
    __dicts__[f].field_symbol      = __fields_info__[f]["symbol"]
    __dicts__[f].field_description = __fields_info__[f]["description"]
    __dicts__[f].field_units       = __fields_info__[f]["units"]
    __dicts__[f].field_remarks     = __fields_info__[f]["remarks"]





####################
# PUBLIC FUNCTIONS #
####################


def get_fields():
    """List all available fields, i.e. physical quantities with available constraints.

    :return: A list of physical quantities with available constraints.
    :rtype: list of strings.
    """
    return copy.deepcopy(__fields__)

def get_field_synonyms(field):
    """List all available synonyms for a field.
    
    :param field: name of the physical parameter to retrieve the synonyms of.
    :type field: str.
    
    :return: A list of physical quantities with available constraints.
    :rtype: list of strings.
    """
    return copy.deepcopy(__fields_info__[__synonym_to_key__[field]]["synonyms"])

def get_all_dicts():
    """Returns all constraints dictionaries.
    
    :return: A list of all availabl dictionaries with constraints.
    :rtype: list of dict.
    """
    return copy.deepcopy(__dicts__)

def get_field(field):
    """Retrieve constraints for a single physical quantity (Field).
    
    :param field: name of the physical parameter to retrieve limits from.
    :type field: str.
    :return: A dictionary of constraints.
    :rtype: dict (None if field is not available).
    """
    assert field in __all_synonyms__, f'ERROR: {field} is not a valid field.'
    return copy.deepcopy(__dicts__[__synonym_to_key__[field]])

def get_dataentry(field):
    """Retrieve constraints for a single constraints set (DataEntry).
    
    :param field: name of the physical parameter to retrieve limits from, in the form 'Field/DataEntry'
    :type field: str.
    :return: A dictionary of constraints.
    :rtype: dict (None if field is not available).
    """

    realfield, dataentry = field.split("/")
    fieldclass = get_field(realfield)
    assert dataentry in fieldclass.keys(), f'ERROR: {dataentry} is not a valid constraint within {realfield}.'
    return fieldclass[dataentry]

def get(field):
    """Retrieve constraints for a single physical quantity (field) or single entry, depending
    on the structure of the string passed. If it is in the form 'Field/DataEntry', it will return a 
    single DataEntry instance, if it's in the form 'Field' it will return the entire Field class.
    
    
    :param field: name of the physical parameter or constraints set to retrieve.
    :type field: str.
    :return: A dictionary of constraints.
    :rtype: dict (None if field is not available).
    """

    if "/" in field:
        return get_dataentry(field)
    else:
        return get_field(field)

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
    update_done = _check_data_updates(force=True, silent=False)
    
    if update_done:
        _LoadAllVariables(__fields__, __dicts__)

_LoadAllVariables(__fields__, __dicts__)
