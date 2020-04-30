dictionary_tag         = "McLeod et al. 2016"

reference              = "McLeod, McLure, Dunlop; MNRAS 459, 3812 (2016)"

url                    = "https://academic.oup.com/mnras/article/459/4/3812/2624050"

description            = \
"""
From first 20 pointings of Frontier Field and CLASH surveys of HST, for a total of ~130 arcmin^2. The constraints are based
on 33 galaxies at z >= 8.4.
"""

data_structure         = "points" #grid or points

extracted              = True

ndim                   = 2

dimensions_descriptors = ["redshift", "M_1500"]

axes                   = [[9.0, -17.498], [9.0, -18.000], [9.0, -19.198], [9.0, -20.202], [9.0, -21.198], [10.0, -19.7]]

values                 = [-2.683, -2.792, -3.446, -4.220, -4.902, -3.90]

err_up                 = [0.158, 0.158, 0.110, 0.224, None, 0.13]

err_down               = [0.234, 0.248, 0.172, 0.525, None, 0.20]

err_up2                = None

err_down2              = None

upper_lim              = [False, False, False, False, True, False]

lower_lim              = False
