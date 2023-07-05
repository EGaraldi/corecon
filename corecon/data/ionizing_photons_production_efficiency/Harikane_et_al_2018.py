dictionary_tag         = "Harikane et al. 2018"

reference              = "Harikane, Ouchi, Shibuya, Kojima, Zhang, Itoh, Ono, et al., ApJ 859, 84 (2018)"

url                    = "https://ui.adsabs.harvard.edu/abs/2018ApJ...859...84H/abstract"

description            = \
"""
Measurements from the SILVERRUSH survey at z ~ 4.9, divided in subsamples based on the EW(Ly-alpha). It includes a 'bin' with all LAEs.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "EW(Lya)"]

axes                   = [[4.9, 'all'], [4.9, '0-20'], [4.9, '20-70'], [4.9, '70-1000']]

values                 = [25.48, 25.27, 25.51, 25.50]

err_up                 = [0.06, 0.19, 0.05, None]

err_down               = [0.06, 0.17, 0.05, None]

upper_lim              = False

lower_lim              = [False, False, False, True]
