dictionary_tag         = "Langeroodi et al. 2022 (subm.)"

reference              = "Langeroodi, Hjorth, Weniel, Kelly, Williams, et al.; subm. (2022)"

url                    = "https://ui.adsabs.harvard.edu/abs/2022arXiv221202491L/abstract"

description            = \
"""
Based on 11 z~8 galaxies (two emission-line galaxies at redshift z=8.15 and z=8.16 in JWST NIRCam imaging and NIRSpec spectroscopy, 
gravitationally lensed by the cluster RX J2129.4+0009, plus nine re-analysed galaxies at 7.2<z<9.5). Of these 11, six have JWST metallicities and five ALMA metallicities.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[ 8.16 ,  8.49 ], [ 8.15 ,  7.52 ], [ 9.51 ,  7.74 ], [ 8.498,  8.   ],
			  [ 7.665,  8.22 ], [ 7.663,  8.4  ], [ 7.212,  9.31 ], [ 7.152,  9.9  ],
			  [ 8.312,  9.96 ], [ 8.382, 10.03 ], [ 9.11 ,  9.31 ]]

err_left               = [[0.  , 0.32], [0.  , 0.35], [0.  , 0.29], [0.  , 0.51], [0.  , 0.18],
       			  [0.  , 0.24], [0.  , 0.47], [0.  , 0.33], [0.  , 0.23], [0.  , 0.38], [0.  , 0.14]]

err_right              = [[0.  , 0.24], [0.  , 0.33], [0.  , 0.23], [0.  , 0.36], [0.  , 0.2 ],
     			  [0.  , 0.15], [0.  , 0.41], [0.  , 0.25], [0.  , 0.28], [0.  , 0.4 ], [0.  , 0.19]]

values                 = [7.65, 7.51, 7.47, 6.99, 8.24, 7.73, 7.36, 7.94, 8.03, 7.44, 7.95]

err_up                 = [0.07, 0.  , 0.09, 0.11, 0.07, 0.12, 0.91, 0.3 , 0.3 , 0.48, 0.35]

err_down               = [0.07, 0.  , 0.09, 0.11, 0.07, 0.12, 0.41, 0.36, 0.89, 0.52, 0.34]

upper_lim              = [False, True, False, False, False, False, False, False, False, False, False]

lower_lim              = False
