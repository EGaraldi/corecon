dictionary_tag         = "Atek et al. 2018"

reference              = "Atek, Richard, Kneib, Schaerer; MNRAS 479, 5184 (2018)"

url                    = "https://academic.oup.com/mnras/article/479/4/5184/5050078"

description            = \
"""
Based on the Hubble Frontier Fields and focused on assessing the uncertainities of the lensing model.
NOTE: we assign errors of 0.0 when the plotted errorbars are smaller than the data point, preventing 
us from retrieving the value.
"""

data_structure         = "grid" #grid or points

extracted              = True

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[6.0], 
                          [-18.6061706 , -18.2522686 , -17.75317604, -17.24500907,
                           -16.75499093, -16.24682396, -15.7477314 , -15.25771325,
                           -14.75862069, -14.25045372, -13.75136116, -13.2522686]
                         ]

values                 = [[-2.68823529, -2.41764706, -2.21764706, -1.98823529, -1.81176471,
                           -1.71764706, -1.53529412, -1.36470588, -1.38823529, -1.38235294,
                           -1.46470588, -1.55882353]]

err_up                 = [[       0.0,         0.0,         0.0,         0.0,  0.21176471,
                           0.16470588,  0.35882353,  0.37647059,  0.70588235,  0.52941176,
                           0.73529412,  1.4       ]]

err_down               = [[       0.0,         0.0,         0.0,         0.0,  0.20588235,
                           0.15294118,  0.35882353,  0.37647059,  0.72352941,  0.52941176,
                           0.74705882,  1.41764706]]

err_up2                =  0.0

err_down2              =  0.0

upper_lim              = False

lower_lim              = False
