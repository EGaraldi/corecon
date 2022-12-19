import numpy as np
import copy

from .DataEntryClass import DataEntry

###############
# Field CLASS #
###############

class Field(dict):
    """Class representing all constraints on a single physical quantity.
    """
    
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)
        self.field_symbol      = None
        self.field_description = None
        self.field_units       = None
        self.field_remarks     = None

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"field_symbol = {self.field_symbol}\n"+\
               f"field_description = {self.field_description}\n"+\
               f"field_units = {self.field_units}\n"+\
               f"field_remarks = {self.field_remarks}\n"+\
               super().__repr__()

    def __add__(self, other):
        assert(isinstance(other, Field))

        combinedFields = Field()
        combinedFields.field_symbol =      '[combined Fields]\n' + self.field_symbol + '\n\t+\n' + other.field_symbol
        combinedFields.field_description = '[combined Fields]\n' + self.field_description + '\n\t+\n' + other.field_description
        combinedFields.field_units =       '[combined Fields]\n' + self.field_units + '\n\t+\n' + other.field_units
        combinedFields.field_remarks =     '[combined Fields]\n' + self.field_remarks + '\n\t+\n' + other.field_remarks

        combinedFields.update(self)
        combinedFields.update(other)

        return combinedFields


    def __radd__(self, other):
        if other==0:
            return self
        else:
            return self.__add__(other)

    def get_all_references(self):
        '''Returns all references of the elements of this dict

        :return: A list of references.
        :rtype: list of string.
        '''
        refs = []
        for k in self.keys():
            refs.append( self[k].reference )
        return refs


    def get_all_urls(self):
        '''Returns all URLs of the elements of this dict

        :return: A list of URLs.
        :rtype: list of string.
        '''
        urls = []
        for k in self.keys():
            urls.append( self[k].url )
        return urls


    def filter_by_redshift_range(self, zmin, zmax):
        '''Returns all the datapoint for a given parameter that lie in a redshift range zmin <= z < zmax.

        :param zmin: lower edge of the redshift range.
        :type zmin: float.
        :param zmax: upper edge of the redshift range.
        :type zmax: float.
        :return: A dictionary of constraints.
        :rtype: dict.
        '''

        if zmin > zmax:
            raise ValueError("zmax cannot be smaller than zmin, you provided zmin = "+str(zmin)+" and zmax="+str(zmax))

        dict_zslice = Field()
        dict_zslice.field_symbol      = self.field_symbol      
        dict_zslice.field_description = self.field_description 

        for k in self.keys():
            w = (self[k].dimensions_descriptors == 'redshift')
            if not np.any(w):
                print("WARNING: missing redshift dimension for entry %s. Skipping it."%(k))
                continue
            zdim = np.where(w)[0][0]
            
            if self[k].ndim == 1:
                redshift = self[k].axes
            else:
                redshift = self[k].axes[:,zdim]

            w = (zmin <= redshift) & (redshift < zmax)
            if any(w):
                dict_zslice[k] = copy.deepcopy(self[k])
                dict_zslice[k].axes      = dict_zslice[k].axes     [w]
                dict_zslice[k].values    = dict_zslice[k].values   [w]
                dict_zslice[k].err_up    = dict_zslice[k].err_up   [w]
                dict_zslice[k].err_down  = dict_zslice[k].err_down [w]
                dict_zslice[k].upper_lim = dict_zslice[k].upper_lim[w]
                dict_zslice[k].lower_lim = dict_zslice[k].lower_lim[w]
                
                for e in dict_zslice[k].extra_data:
                    _temp = getattr(dict_zslice[k], e)
                    setattr(dict_zslice[k], e, _temp[w])

        return dict_zslice

    def filter_by_extracted(self, extracted):
        '''Filters the datapoint for a given parameter based on the value of their 'extracted' field.

        :param extracted: value of the 'extracted' field
        :type zmin: bool
        :return: A dictionary of constraints.
        :rtype: dict.
        '''

        dict_extracted = Field()
        dict_extracted.field_symbol      = self.field_symbol      
        dict_extracted.field_description = self.field_description 

        for k in self.keys():
            if self[k].extracted == extracted:
                dict_extracted[k] = copy.deepcopy(self[k])

        return dict_extracted


    def get_lower_limits(self):
        '''Returns all the lower limits for a given parameter as a dictionary.
        
        :return: A dictionary of constraints.
        :rtype: dict.
        '''

        dict_lls = Field()
        dict_lls.field_symbol      = self.field_symbol      
        dict_lls.field_description = self.field_description 

        for k in self.keys():              
            if any(self[k].lower_lim):
                dict_lls[k] = copy.deepcopy(self[k])
                dict_lls[k].axes      = dict_lls[k].axes     [self[k].lower_lim]
                dict_lls[k].values    = dict_lls[k].values   [self[k].lower_lim]
                dict_lls[k].err_up    = dict_lls[k].err_up   [self[k].lower_lim]
                dict_lls[k].err_down  = dict_lls[k].err_down [self[k].lower_lim]
                dict_lls[k].upper_lim = dict_lls[k].upper_lim[self[k].lower_lim]
                dict_lls[k].lower_lim = dict_lls[k].lower_lim[self[k].lower_lim]
                
                for e in dict_lls[k].extra_data:
                    _temp = getattr(dict_lls[k], e)
                    setattr(dict_lls[k], e, _temp[self[k].lower_lim])

        return dict_lls


    def get_upper_limits(self):
        '''Returns all the upper limits for a given parameter as a dictionary.
        
        :return: A dictionary of constraints.
        :rtype: dict.
        '''

        dict_uls = Field()
        dict_uls.field_symbol      = self.field_symbol      
        dict_uls.field_description = self.field_description 

        for k in self.keys():
            if any(self[k].upper_lim):
                dict_uls[k] = copy.deepcopy(self[k])
                dict_uls[k].axes      = dict_uls[k].axes     [self[k].upper_lim]
                dict_uls[k].values    = dict_uls[k].values   [self[k].upper_lim]
                dict_uls[k].err_up    = dict_uls[k].err_up   [self[k].upper_lim]
                dict_uls[k].err_down  = dict_uls[k].err_down [self[k].upper_lim]
                dict_uls[k].upper_lim = dict_uls[k].upper_lim[self[k].upper_lim]
                dict_uls[k].lower_lim = dict_uls[k].lower_lim[self[k].upper_lim]
                
                for e in dict_ulls[k].extra_data:
                    _temp = getattr(dict_ulls[k], e)
                    setattr(dict_ulls[k], e, _temp[self[k].upper_lim])

        return dict_uls

