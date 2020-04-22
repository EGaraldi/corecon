dictionary_tag         = "Ross et al. 2013"

reference              = "Ross, McGreer, White, Richards, Myers, Palanque-Delabrouille, et al.; ApJ. 773, 14 (2013)"

url                    = "https://iopscience.iop.org/article/10.1088/0004-637X/773/1/14"

description            = \
"""
Constraints from SDSS-III: BOSS DR9. Uniform sample of 22301 i < 21.8 over an area of 2236 deg2, with confirmed
spectroscopic redshift in 2.2 < z < 3.5.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_1450"]

axes                   = [[2.4, 2.8, 3.25], 
                          [-28.95, -28.65, -28.35, -28.05, -27.75, -27.45, -27.15, -26.85,
                           -26.55, -26.25, -25.95, -25.65, -25.35, -25.05, -24.75, -24.45, -24.15]
                         ]

values                 = [[None, -8.526, -7.625, -7.271, -7.021, -6.818, -6.627, -6.424, -6.31 ,
                           -6.163, -6.053, -5.929, -5.851, -5.811, -5.797, -5.825, -6.412],
                          [-8.505, -7.766, -7.378, -7.192, -6.882, -6.679, -6.591, -6.412,
                           -6.247, -6.199, -6.157, -6.061, -6.038, -6.004, -6.155, -7.434, None],
                          [-8.12 , -7.697, -7.411, -7.255, -7.031, -6.878, -6.714, -6.637,
                           -6.518, -6.452, -6.393, -6.277, -6.098, -6.024, -7.167, None, None]
                         ]

err_up                 = [[None, 0.12144292, 0.04702711, 0.03185706, 0.02410113, 0.01918881,
                           0.01546857, 0.01228493, 0.01079093, 0.00913256, 0.00804984,
                           0.00699145, 0.00639702, 0.00610875, 0.0060113 , 0.0062073 ,
                           0.01211832],
                          [0.11927267, 0.0550217 , 0.03595753, 0.02927126, 0.0206973 ,
                           0.01645176, 0.01489994, 0.01215867, 0.01008813, 0.00954357,
                           0.00910074, 0.00816131, 0.00794936, 0.00764057, 0.00907516,
                           0.03827896, None],
                          [0.07331385, 0.04652867, 0.03397039, 0.02857016, 0.02222513,
                           0.01872216, 0.0155483 , 0.01424562, 0.01244837, 0.01155973,
                           0.01080199, 0.00947438, 0.00772056, 0.00709342, 0.02587353,
                           None, None]
                         ]

err_down               = [[None, 0.16918292, 0.05274478, 0.03438019, 0.02551761, 0.020076  ,
                           0.01603994, 0.01264258, 0.0110659 , 0.00932874, 0.00820187,
                           0.00710585, 0.00649265, 0.0061959 , 0.00609568, 0.0062973 ,
                           0.01246619],
                          [0.16497618, 0.0630178 , 0.03920559, 0.03138763, 0.02173325,
                           0.01709961, 0.01542935, 0.0125089 , 0.01032805, 0.00975801,
                           0.00929554, 0.00831762, 0.00809758, 0.0077774 , 0.00926886,
                           0.04198189, None],
                          [0.08825493, 0.05211842, 0.03685475, 0.03058284, 0.02342415,
                           0.01956577, 0.01612569, 0.01472879, 0.01281573, 0.01187585,
                           0.01107753, 0.00968569, 0.0078603 , 0.00721121, 0.02751317,
                           None, None]
                         ]

err_up2                = None

err_down2              = None

upper_lim              = [[False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False],
                          [False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False],
                          [False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False]
                         ]

lower_lim              = [[False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False],
                          [False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False],
                          [False, False, False, False, False, False, False, False, False,
                           False, False, False, False, False, False, False, False]
                         ]
