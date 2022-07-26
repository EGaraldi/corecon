dictionary_tag         = "Ishigaki et al. 2018"

reference              = "Ishigaki, Kawamata, Ouchi, Oguri, Shimasaku, Ono; ApJ. 854, 73 (2018)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/aaa544"

description            = \
"""
Based on ~450 droput-selected galaxies from the Hubble Frontier Fields at 6<z<10.
NOTE: we assign errors of 0.0 when the plotted errorbars are smaller than the data point, preventing 
us from retrieving the value.
"""

data_structure         = "points" #grid or points

extracted              = True

ndim                   = 2

dimensions_descriptors = ["M_1500", "redshift"]

axes                   = [[-23.259, 6.5], [-22.256, 6.5], [-21.259, 6.5], [-20.501, 6.5], [-20.003, 6.5],
                          [-19.505, 6.5], [-19.000, 6.5], [-18.494, 6.5], [-18.010, 6.5], [-17.505, 6.5],
                          [-17.000, 6.5], [-16.509, 6.5], [-16.003, 6.5], [-15.245, 6.5], [-14.249, 6.5],
                          [-13.245, 6.5], [-21.513, 8.0], [-21.009, 8.0], [-20.512, 8.0], [-20.015, 8.0],
                          [-19.510, 8.0], [-19.007, 8.0], [-18.259, 8.0], [-17.258, 8.0], [-16.257, 8.0], 
                          [-15.255, 8.0], [-14.247, 8.0], [-23.000, 9.0], [-22.000, 9.0], [-21.000, 9.0], 
                          [-20.000, 9.0], [-19.000, 9.0], [-18.000, 9.0], [-17.000, 9.0], [-16.000, 9.0],
                          [-15.000, 9.0], [-14.000, 9.0], [-22.000, 10.0], [-21.000, 10.0], [-20.000, 10.0],
                          [-19.000, 10.0], [-18.000, 10.0], [-17.000, 10.0], [-16.000, 10.0], [-15.000, 10.0]
                         ]

values                 = [-4.86903973, -4.83951933, -4.13219762, -3.48618751, -3.14793102,
                          -2.92520727, -2.63317314, -2.64152412, -2.28784473, -2.15755643,
                          -1.88862885, -1.64278928, -1.62803372, -1.18998253, -0.68291756,
                           0.07060797, -4.70344921, -4.39598551, -3.97981925, -3.60592357, 
                          -3.38300105, -2.87022306, -3.32991233, -2.83575128, -1.9370003 , 
                          -1.40660732, -0.61655891, -4.52941176, -4.53529412, -4.77647059, 
                          -3.5       , -3.08823529, -3.2       , -2.31176471, -2.05882353, 
                          -1.3       , -0.24117647, -4.47760102, -4.45161861, -4.26807668, 
                          -3.56159114, -2.91955861, -2.19874632, -1.4492632 , -0.66399789
                         ]

err_up                 = [None, 0.361993299,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
                           0.0,  0.0, 0.346598203, None, 0.51327895, 0.3623261 , 0.15095962,  0.0,  0.0,
                           0.0, 0.27777138, 0.35024202, 0.28985546, None, None, None, None, 0.51764706, 0.0, 0.0,
                          None, 0.29411765, 0.52352941, 0.51176471, None, None, None, None, None, None, None, 
                          None, None
                         ]

err_down               = [None,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
                           0.0,  0.0,  0.30039438,  0.30040365,  0.46213094, None, 
                           0.75483194,  0.45893105,  0.26570761,  0.13889585,  0.0,
                           0.0,  0.35025556,  0.46498324,  0.34421013,  None, None,
                          None,  None,  0.75882353, 0.0, 0.0, None, 0.34117647,  
                          0.75294118,  0.76470588,  None, None, None, None, None, None, 
                          None, None, None
                         ]

err_up2                = None

err_down2              = None

upper_lim              = [True, False, False, False, False, False, False, False, False, False, 
                          False, False, False, False, False, True, False, False, False, False, False, 
                          False, False, False, False, True, True, True, True, False, False, False, 
                          True, False, False, False, True, True, True, True, True, True, True, True, True
                         ]

lower_lim              = [False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                         ]
