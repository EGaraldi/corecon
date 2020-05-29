import numpy as np
import os.path
import os
import itertools
import copy

from .InternalFunctions import _insert_blank_spaces, _get_str_from_array1d, _get_str_from_multiarray, _get_str_from_array#, _compare_arrays

###################
# DataEntry CLASS #
###################


class DataEntry:
    """Class representing a single constraint set.
    """

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
                 lower_lim              = None,
                 extra_data             = None ):
        """construct method
        """
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
        self.extra_data = []
        if extra_data is not None:
            for k in extra_data.keys():
                setattr(self, k, extra_data[k])
                self.extra_data.append(k)
        self.extra_data = np.array(self.extra_data)

    def __repr__(self):
        """string describing the class
        """
        return "corecon DataEntry class"

    def __str__(self):
        """output of print
        """

        ostr=""
        ostr +=                       "ndim                   = %i\n"%self.ndim                  
        ostr +=                       "description            = %s\n"%_insert_blank_spaces(self.description, 25)
        ostr +=                       "reference              = %s\n"%self.reference             
        ostr +=                       "url                    = %s\n"%self.url                   
        ostr +=                       "extracted              = %s\n"%self.extracted             
        ostr += _get_str_from_array1d("dimensions_descriptors = ", self.dimensions_descriptors)
        ostr += _get_str_from_array  ("axes                   = ", self.axes     , self.ndim)
        ostr += _get_str_from_array1d("values                 = ", self.values   )
        ostr += _get_str_from_array1d("err_up                 = ", self.err_up   )
        ostr += _get_str_from_array1d("err_down               = ", self.err_down )
        ostr += _get_str_from_array1d("err_up2                = ", self.err_up2  )
        ostr += _get_str_from_array1d("err_down2              = ", self.err_down2)
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
                               (self.url                    == other.url                                      ) & \
                               (self.extracted              == other.extracted                                ) & \
                    np.all     (self.dimensions_descriptors == other.dimensions_descriptors                   ) & \
                    np.all     (self.axes                   == other.axes                                     ) & \
                    np.allclose(self.values                 ,  other.values                 , equal_nan=True  ) & \
                    np.allclose(self.err_up                 ,  other.err_up                 , equal_nan=True  ) & \
                    np.allclose(self.err_down               ,  other.err_down               , equal_nan=True  ) & \
                    np.allclose(self.err_up2                ,  other.err_up2                , equal_nan=True  ) & \
                    np.allclose(self.err_down2              ,  other.err_down2              , equal_nan=True  ) & \
                    np.all     (self.upper_lim              == other.upper_lim                                ) & \
                    np.all     (self.lower_lim              == other.lower_lim                                ) )

    def swap_limits(self):
        """Swap upper and lower limits. Useful when computing a derived quantity.
        """
        foo = copy.deepcopy(self.upper_lim)
        self.upper_lim = copy.deepcopy(self.lower_lim)
        self.lower_lim = copy.deepcopy(foo)

    #def none_to_value(self, value):
    #    for f in [self.values, self.err_up, self.err_down, self.err_up2, self.err_down2]:
    #        w = (f == None)
    #        f[w] = value

    #def none_to_nan(self):
    #    self.none_to_value(np.nan)
    
    def nan_to_values(self, array, new_vals):
        """Replaces all NaN with values.

        :param array: name of the :class:`corecon.DataEntry` array variable to work on. Use 'all' to replace NaNs in all array variables.
        :type array: str
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
        #if array=='err_up2' or array=='all':
        #    w = np.isnan(self.err_up2)
        #    self.err_up2[w] = new_vals
        #if array=='err_down2' or array=='all':
        #    w = np.isnan(self.err_down2)
        #    self.err_down2[w] = new_vals       
        names = []
        if array=='all':
            names.append('values')
            names.append('err_up')
            names.append('err_down')
            names.append('err_up2')
            names.append('err_down2')
            for k in self.extra_data:
                names.append(k)
        else:
            names.append(array)

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
        self.err_up2  [w] = newval
        self.err_down2[w] = newval


