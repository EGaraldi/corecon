dictionary_tag         = "Yang et al. 2020b"

reference              = "Yang, Wang, Fan, Hennawi, Davies, Yue, Eilers, et al.; ApJ 904, 26 (2020)"

url                    = "https://ui.adsabs.harvard.edu/abs/2020ApJ...904...26Y/abstract"

description            = \
"""
Based on the optical depth of Ly-alpha and Ly-beta forest in a new sample of 32 quasars at 6.308 ≤ z ≤ 7.00 (observed with VLT, Keck, Gemini, LBT, and MMT).
"""

data_structure         = "points" #grid or points

extracted              = True #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [5.4,  5.6, 5.8,  6.0, 6.2]

values                 = [0.9999437, 0.9999241, 0.9999115, 0.999887 , 0.9998975]

err_up                 = [1.23e-05, 6.15e-06, 1.28e-05, 1.875e-05, 1.06e-05]

err_down               = [5.58e-06, 1.62e-05, 1.76e-05, 2e-4, 2e-4]

err_up2                = None

err_down2              = None

upper_lim              = [False, False, False, True, True]

lower_lim              = [False, False, False, False, False]
