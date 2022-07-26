dictionary_tag = "D'Aloisio et al. 2018"

reference   = "D’Aloisio, McQuinn, Davies, Furlanetto; 473, 560 (2018)"

url         = "https://academic.oup.com/mnras/article-abstract/473/1/560/4159371"

description = \
"""
From a re-analysis of the 21 QSO in McGreer, Mesinger & D’Odorico (2015), using an hydrodynamical simulaiton
"""

data_structure         = "grid" #grid or points

extracted              = True 

ndim                   = 2

dimensions_descriptors = ["redshift", "ks (s/km)"]

axes                   = [[5.2, 5.4, 5.6], \
                          [0.000942, 0.001908, 0.002850, 0.003840 ,0.005445 ,0.007871, \
                           0.011096, 0.015741, 0.022128, 0.031038, 0.043413, 0.061164]
                         ]

values      = [[639.8, 319.9, 336.6, 286.1, 218.8, 244.4, 186.7, 162.1, 125.4, \
                96.79, 73.05, 34.98],
               [786.2, 477.5, 622.3, 378.6, 426.6, 273.2, 288.7, 167.9, 174.6, \
                116.9, 66.19, 48.75],
               [1193, 596.4, 612.4, 522.4, 624.6, 300.7, 371.3, 254.4, 254.6, \
                218.5, 160.1, 108.9]
              ]

err_up      = [[168.3, 84.18, 100.9, 75.74, 39.27, 43.36, 26.25, 16.2, 9.977, \
                8.066, 5.729, 2.535],
               [239.3, 148.2, 177.8, 123.5, 82.95, 44.85, 45.29, 21.73, 19.88, \
                11.19, 5.818, 3.079],
               [419.3, 209.5, 236.4, 174.1, 179.3, 63.31, 71.52, 33.78, 33.94, \
                24.27, 18.19, 9.897]
              ]

err_down    = [[168.4, 84.18, 101, 84.16, 33.66, 55.19, 29.17, 18.23, 14.25, \
                8.066, 5.013, 2.028],
               [239.3, 148.2, 188.9, 115.2, 94.81, 48.93, 42.46, 19.75, 18.46, \
                9.152, 5.091, 3.079],
               [451.6, 209.5, 236.4, 166.2, 156.2, 59.36, 68.77, 45.71, 38.18, \
                23.26, 14.55, 7.293]
              ]

err_up2     = None

err_down2   = None

upper_lim     = [[False, False, False, False, False, False, \
                  False, False, False, False, False, False],
                 [False, False, False, False, False, False, \
                  False, False, False, False, False, False],
                 [False, False, False, False, False, False, \
                  False, False, False, False, False, False]
                ]

lower_lim     = [[False, False, False, False, False, False, \
                  False, False, False, False, False, False],
                 [False, False, False, False, False, False, \
                  False, False, False, False, False, False],
                 [False, False, False, False, False, False, \
                  False, False, False, False, False, False]
                ]
