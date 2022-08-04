dictionary_tag         = "Harikane et al. 2022"

reference              = "Harikane, Ouchi, Oguri, Ono, Nakajima, Isobe, Umeda, Mawatari, Zhang; arXiv (2022)"

url                    = "https://arxiv.org/pdf/2208.01612.pdf"

description            = \
"""
Based on 25 dropout galaxy candidates at 9 < z < 17 identified in 90 arcmin2 JWST/NIRCam images taken by the early release 
observations (ERO) and early release science (ERS) programs.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [9, 12, 17]

values                 = [-2.65, -3.31, -3.63]

err_up                 = [0.16, 0.30, 0.31]

err_down               = [0.14, 0.28, 100]

upper_lim              = False

lower_lim              = False

values_no_dust_correction = [-2.70, -3.41, -3.74]

err_up_no_dust_correction = [0.17, 0.27, 0.31]

err_down_no_dust_correction = [0.14, 0.26, 100]
