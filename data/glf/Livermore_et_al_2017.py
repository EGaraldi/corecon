dictionary_tag         = "Livermore et a. 2017"

reference              = "Livermore, Finkelstein, Lotz; ApJ. 835, 113 (2017)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/835/2/113"

description            = \
"""
Based on a re-analysis of the Hubble Frontier Fields around Abell 2744 and MACS 0416 using wavelet 
decomposition to remove the cluster light. The final sample consists of 167 galaxies at z>6.
"""

data_structure         = "points" #grid or points

extracted              = True

ndim                   = 2

dimensions_descriptors = ["M_1500", "redshift"]

axes                   = [[-19.5, 6.0], [-19.0, 6.0], [-18.5, 6.0], [-18.0, 6.0], [-17.5, 6.0], [-17.0, 6.0],
                          [-16.5, 6.0], [-16.0, 6.0], [-15.5, 6.0], [-15.0, 6.0], [-14.5, 6.0], [-14.0, 6.0],
                          [-13.5, 6.0], [-13.0, 6.0], [-12.5, 6.0], [-19.0, 7.0], [-18.5, 7.0], [-18.0, 7.0], 
                          [-17.5, 7.0], [-17.0, 7.0], [-16.5, 7.0], [-16.0, 7.0], [-15.5, 7.0], [-15.0, 7.0],
                          [-14.5, 7.0], [-20.5, 8.0], [-20.0, 8.0], [-19.5, 8.0], [-19.0, 8.0], [-18.5, 8.0], 
                          [-18.0, 8.0], [-17.5, 8.0], [-17.0, 8.0], [-16.5, 8.0], [-16.0, 8.0], [-15.5, 8.0], 
                          [-15.0, 8.0]
                         ]

values                 = [-2.91100259, -2.87982335, -2.84071963, -2.21430024, -2.02439029,
                          -1.548753  , -1.17630274, -1.09750428, -0.78060977, -0.77325219,
                          -0.68650513, -0.60771874, -0.21940747,  0.16892793,  0.55725126, 
                          -3.34602996, -2.82856428, -2.44039779, -2.25425149, -1.69638803,
                          -1.59913063, -1.59076211, -1.21875098, -0.66088751, -0.47474122,
                          -3.30894309, -3.29268293, -2.79674797, -3.23577236, -2.69105691,
                          -2.71544715, -2.77235772, -2.10569106, -2.04065041, -1.65853659,
                          -1.00813008, -0.93495935
                         ]

err_up                 = [0.30950075, 0.34125896, 0.50000172, 0.19047685, 0.19048891,
                          0.1269725 , 0.14285764, 0.19046479, 0.16666724, 0.33333448,
                          0.42061225, 0.5396844 ,       None,       None, 0.50793826,
                          0.52525253, 0.37171092, 0.21009476, 0.24242424, 0.14544829,
                          0.25859211, 0.47676768, 0.37979173, 0.29898364, 0.37978547,
                          0.52845528, 0.10569106, 0.30894309,       None, 0.30894309,
                          0.36585366, 0.5203252 , 0.37398374, 0.52845528,       None,
                          0.3902439 , 0.51219512
                         ]

err_down               = [0.42858497, 0.44445804, 0.42857291, 0.24603259, 0.15079417,
                          0.22222299, 0.19841338, 0.20637404, 0.31748553, 0.309549  ,
                          0.7381219 , 0.76190739,       None,       None, 0.76984392, 
                          0.77575758, 0.44444444, 0.33939394, 0.33939394, 0.34746849,
                          0.29898364, 0.45252525, 0.7434406 , 0.86464646, 0.73535979,
                          0.76422764, 0.20325203, 0.84552846,       None, 0.45528455,
                          0.75609756, 0.77235772, 0.7398374 , 0.75609756,       None,
                          0.7398374 , 0.77235772
                         ]

err_up2                = None

err_down2              = None

upper_lim              = [False, False, False, False, False, False, False, False, False,
                          False, False, False,  True,  True, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False,  True, False, False, False, False, False,  True, False,
                          False
                         ]

lower_lim              = [False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False
                         ]
