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

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[9, -23.03], [9, -22.03], [9, -21.03], [9, -20.03], [9, -19.03], [9, -18.03], 
                          [12, -23.21], [12, -22.21], [12, -21.21], [12, -20.21], [12, -19.21], [12, -18.21],
                          [17, -23.59], [17, -20.59]]

values                 = [-4.1580152 , -4.11350927, -4.38933984, -4.38933984, -3.5214335, -3.27083521, 
                          -5.22841252, -5.18641901, -5.34872199, -4.88941029, -4.83564714, -3.98716278, 
                          -5.66756154, -5.26841123]

err_up                 = [None, None, 0.52510835, 0.52510835, 0.23743685, 0.25983983,
                          None, None, 0.51957019, 0.36797679, 0.36840152, 0.30730906,        
                          None, 0.36705496]

err_down               = [None, None, 1.40654018, 1.40654018, 0.41038063, 0.50385551,
                          None, None, 0.83173408, 0.48734042, 0.492255  , 0.45653472,
                          None, 0.47151738]

err_right              = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5]

err_left               = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5]

upper_lim              = [True, True, False, False, False, False, 
                          True, True, False, False, False, False,
                          True, False]

lower_lim              = False
