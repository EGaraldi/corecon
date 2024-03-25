dictionary_tag         = "Harikane et al. 2023"

reference              = "Harikane, Ouchi, Oguri, Ono, Nakajima, Isobe, Umeda, Mawatari, Zhang; ApJS 265, 5 (2023)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4365/acaaa9"

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
                          [16, -23.59], [16, -20.59]]

values                 = [-4.1580152 , -4.11520464, -4.39794001, -4.38933984, -3.64975198, -2.95078198, 
                          -5.23284413, -5.19382003, -5.30103   , -4.8827287 , -4.61978876, -3.84771166, 
                          -5.61618463, -5.17914201]

err_up                 = [None, None, 0.52569252, 0.52542593, 0.03482176, 0.0039757,
                          None, None, 0.52009033, 0.36845013, 0.29921665, 0.37791135,        
                          None, 0.3683515]

err_down               = [None, None, 1.42596873, 1.40654018, 0.02927134, 0.00350396,
                          None, None, 0.83564714, 0.49402201, 0.38021124, 0.64713837,
                          None, 0.49247839]

err_right              = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5]

err_left               = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5]

upper_lim              = [True, True, False, False, False, False, 
                          True, True, False, False, False, False,
                          True, False]

lower_lim              = False
