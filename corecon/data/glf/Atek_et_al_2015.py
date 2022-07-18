dictionary_tag         = "Atek et al. 2015"

reference              = "Atek, Richard, Kneib, Jauzac, Schaerer, Clement, et al.; ApJ 800, 18 (2015)"

url                    = "https://ui.adsabs.harvard.edu/abs/2015ApJ...800...18A/abstract"

description            = \
"""
Based on the Hubble Frontier Fields cluster A2744, based on detection of 50 galaxy candidates at z~7 and 8 at z~8.
"""

data_structure         = "grid" #grid or points

extracted              = True

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[7.0, 8.0], 
                          [-20.25, -19.75, -19.25, -18.75, -18.25, -17.75, -17.25,
                           -16.75, -16.25, -15.75, -15.25]
                         ]

values                 = [[-3.4184, -3.0263, -2.9044, -2.7418, -2.3896, -2.1032, 
                           -1.8201, -1.7548, -1.6044, -1.4012, -1.4012], 
                          [None, -3.3170, -2.9260, -2.8386, None, -2.0524, -1.6198,
                           None, None, None, None]
                         ]                         

err_up                 = [[0.1576, 0.1658, 0.1431, 0.1332, 0.1401, 0.1990, 0.1940, 
                           0.1893, 0.2117, 0.3123, 0.3122],
                          [None, 0.2621, 0.2454, 0.2995, None, 1.2354, 1.1276,
                           None, None, None, None]
                         ]

err_down               = [[0.1576, 0.1658, 0.1431, 0.1332, 0.1401, 0.1990, 0.1940, 
                           0.1893, 0.2117, 0.3123, 0.3122],
                          [None, 0.2912, 0.4825, 0.3078, None, 1.2354, 1.4684,
                           None, None, None, None]
                         ]

err_up2                =  0.0

err_down2              =  0.0

upper_lim              = False

lower_lim              = False
