import numpy as np
import os.path
import os
import itertools
import copy

from .InternalFunctions import _insert_blank_spaces, _get_str_from_array1d, _get_str_from_multiarray, _get_str_from_array, _compare_arrays

###################
# DataEntry CLASS #
###################


class DataEntry:

    def __init__(self, 
                 ndim                   = None,  
                 description            = None,  
                 reference              = None,
                 url                    = None,
                 dimensions_descriptors = None,  
                 extracted              = None,
                 axes                   = None,  
                 values                 = None,  
                 err_up                 = None,  
                 err_down               = None,  
                 err_up2                = None,  
                 err_down2              = None,  
                 upper_lim              = None,  
                 lower_lim              = None):
        
        self.ndim                   = ndim                  
        self.description            = description           
        self.reference              = reference             
        self.url                    = url                   
        self.dimensions_descriptors = dimensions_descriptors
        self.extracted              = extracted
        self.axes                   = axes                  
        self.values                 = values                
        self.err_up                 = err_up                
        self.err_down               = err_down              
        self.err_up2                = err_up2               
        self.err_down2              = err_down2             
        self.upper_lim              = upper_lim             
        self.lower_lim              = lower_lim             
    
    def __repr__(self):
        """string describing the class"""
        return "corecon DataEntry class"

    def __str__(self):
        """output of print"""

        ostr=""
        ostr += "ndim                   = %i\n"%self.ndim                  
        ostr += "description            = %s\n"%_insert_blank_spaces(self.description, 25)
        ostr += "reference              = %s\n"%self.reference             
        ostr += "url                    = %s\n"%self.url                   
        ostr += "extracted              = %s\n"%self.extracted             
        ostr += _get_str_from_array1d("dimensions_descriptors = ", self.dimensions_descriptors)
        ostr += _get_str_from_array("axes                   = ", self.axes     , self.ndim)
        ostr += _get_str_from_array("values                 = ", self.values   , self.ndim)
        ostr += _get_str_from_array("err_up                 = ", self.err_up   , self.ndim)
        ostr += _get_str_from_array("err_down               = ", self.err_down , self.ndim)
        ostr += _get_str_from_array("err_up2                = ", self.err_up2  , self.ndim)
        ostr += _get_str_from_array("err_down2              = ", self.err_down2, self.ndim)
        ostr += _get_str_from_array("upper_lim              = ", self.upper_lim, self.ndim)
        ostr += _get_str_from_array("lower_lim              = ", self.lower_lim, self.ndim)
        return ostr

    def __eq__(self,other):
        """custom equality"""

        return(
                               (self.ndim                 == other.ndim                   ) & \
                               (self.description          == other.description            ) & \
                               (self.reference            == other.reference              ) & \
                               (self.url                  == other.url                    ) & \
                               (self.extracted            == other.extracted              ) & \
                _compare_arrays(self.dimensions_descriptors, other.dimensions_descriptors ) & \
                _compare_arrays(self.axes                  , other.axes                   ) & \
                _compare_arrays(self.values                , other.values                 ) & \
                _compare_arrays(self.err_up                , other.err_up                 ) & \
                _compare_arrays(self.err_down              , other.err_down               ) & \
                _compare_arrays(self.err_up2               , other.err_up2                ) & \
                _compare_arrays(self.err_down2             , other.err_down2              ) & \
                _compare_arrays(self.upper_lim             , other.upper_lim              ) & \
                _compare_arrays(self.lower_lim             , other.lower_lim              ) )
    
    def swap_limits(self):
        foo = copy.deepcopy(self.upper_lim)
        self.upper_lim = copy.deepcopy(self.lower_lim)
        self.lower_lim = copy.deepcopy(foo)

    def none_to_value(self, value):
        for f in [self.values, self.err_up, self.err_down, self.err_up2, self.err_down2]:
            w = (f == None)
            f[w] = value

    def none_to_nan(self):
        self.none_to_value(np.nan)

    def set_lim_errors(self, newval, frac_of_values=False):
        w = (self.upper_lim|self.lower_lim)
        if frac_of_values:
            newval *= self.values[w]
        self.err_up   [w] = newval
        self.err_down [w] = newval
        self.err_up2  [w] = newval
        self.err_down2[w] = newval


