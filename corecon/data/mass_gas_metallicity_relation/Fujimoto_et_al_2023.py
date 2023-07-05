dictionary_tag         = "Fujimoto et al. 2023"

reference              = "Fujimoto, Pablo Arrabal, Dickinson, Finkelstein, Kartaltepe, et al.; ApJL 949, 25 (2023)"

url                    = "https://ui.adsabs.harvard.edu/abs/2023ApJ...949L..25F/abstract"

description            = \
"""
Based on JWST NIRSpec spectroscopy for 11 galaxy candidates with photometric redshifts of z = 9-13 and -21 < MUV < -18 identified in CEERS NIRCam imaging
"""

data_structure         = "points" #grid or points

extracted              = True

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[8.005 ,  8.30],[8.876 ,  8.08],[7.769 ,  9.49],[8.8805,  7.30],[8.998 ,  7.78]]

err_left               = [[0.0, 0.2 ],[0.0, 0.3 ],[0.0, 0.24],[0.0, 0.3 ],[0.0, 0.3 ]]

err_right              = [[0.0, 0.27],[0.0, 0.24],[0.0, 0.22],[0.0, 0.3 ],[0.0, 0.3 ]]

values                 = [7.77963215, 7.14918256, 7.38726158, 7.67847411, 7.66621253]

err_up                 = [0.34230245, 0.24420981, 0.27486376, 0.42915531, 0.44141689]

err_down               = [0.44652589, 0.25340599, 0.30347411, 0.58242507, 0.34025886]

upper_lim              = False

lower_lim              = False

MUV                    = [-20.47, -20.75, -18.55 , -18.38, -19.08]

SFR                    = [9.8, 3.9 , 64.3, 0.8 , 2.7]

err_down_SFR           = [3.2, 0.6 , 50.8, 0.3 , 1.0 ]

err_up_SFR             = [2.9, 1.1, 18.6, 0.7, 1.5]
