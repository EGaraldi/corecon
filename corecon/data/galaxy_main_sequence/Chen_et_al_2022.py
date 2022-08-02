dictionary_tag         = "Chen et al. 2022"

reference              = "Chen, Stark, Endsley, Topping, Whitler, Charlot, et al.; arXiv (2022)"

url                    = "https://arxiv.org/pdf/2207.12657.pdf"

description            = \
"""
Based on 12 of the most luminous and massive  z = 6 - 8 galaxies in the portion of the EGS field observed with recent
JWST/NIRCam imaging. NOTE: the SFR has been computed from the sSFR and stellar masses.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[5.53, 9.37], [6.27, 7.62], [6.31, 8.27], [6.45, 8.6 ], [6.54, 8.22], [6.66, 8.31], \
                          [6.68, 8.97], [6.74, 7.59], [6.79, 7.85], [7.17, 8.15], [7.44, 8.55], [7.6 , 8.57]]

values                 = [11.72114408,  4.16869383,  7.82076597,  8.36025058, 10.12348014, \
                          20.41737945,  8.39928871,  3.89045145,  2.83178314,  9.46400155, \
                          17.38585607, 14.48987393]

err_up                 = [24.70327929,   2.14087961,  44.13517259,  37.99242447, 19.09349121, 2.49129708,  
                          23.13286253,   3.35390815, 2.51617534,  24.86294665, 135.9469892 ,  64.1486213 ]

err_down               = [7.48353144,  0.36679987,  7.0770747 ,  6.73844048,  7.65517982, 1.36277227,  
                          6.25116152,  0.2596709 ,  1.38179729,  7.90652082, 16.57647834, 12.11233282]

err_right              = [[0.02, 0.15], [0.15, 0.18], [0.12, 0.45], [0.17, 0.24], [1.33, 0.25], [0.01, 0.05],\
                          [0.02, 0.25], [0.01, 0.27], [0.09, 0.13], [0.16, 0.39], [0.09, 0.64], [0.02, 0.33]]

err_left               = [[0.13, 0.22], [0.35, 0.04], [0.17, 0.44], [0.38, 0.39], [0.11, 0.29], [0.01, 0.03],\
                          [0.04, 0.24], [0.01, 0.03], [0.06, 0.12], [0.09, 0.3 ], [0.34, 0.42], [0.06, 0.34]]

upper_lim              = False

lower_lim              = False
