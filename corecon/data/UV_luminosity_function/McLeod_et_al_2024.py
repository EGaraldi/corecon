dictionary_tag         = "McLeod et al. 2024"

reference              = "McLeod, Donnan, McLure, Dunlop, Magee, Begley, Carnall, et al.; MNRAS 527, 5004 (2024)"

url                    = "https://academic.oup.com/mnras/article/527/3/5004/7408621"

description            = \
"""
based on a wide-area (>250 arcmin2) data set of JWST NIRCam near-infrared imaging assembled from 13 public JWST surveys. 61 robust z > 9.5 candidates detected at >8 sigma
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[11, -22.57], [11, -21.80], [11, -20.80], [11, -20.05], [11, -19.55], [11, -18.85], [11, -18.23],
                          [13.5, -19.45], [13.5, -18.95]]

values                 = [-6.92081875, -5.88941029, -4.90170246, -4.40077214, -4.00599097, -3.62911698, -3.20010832, 
                          -4.60747891, -4.20767836]

err_up                 = [0.30103   , 0.29934341, 0.12752845, 0.12619369, 0.15397629, 0.14339903, 0.16261971, 
                          0.2232186 , 0.21512741]

err_down               = [    np.inf, 2.11058971, 0.18131749, 0.17861209, 0.24073246, 0.21554698, 0.26295466, 
                          0.48403607, 0.44499162]

upper_lim              = False

lower_lim              = False
