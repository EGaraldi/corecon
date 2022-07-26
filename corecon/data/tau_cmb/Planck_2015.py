dictionary_tag         = "Planck 2015"

reference              = "Planck Collaboration; A&A 594, A13 (2016)"

url                    = "https://www.aanda.org/articles/aa/full_html/2016/10/aa25830-15/aa25830-15.html"

description            = \
"""
Cosmological parameter result from the full-mission Planck measurements of the CMB anisotropies.
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["dataset"]

axes                   = ["TT+lowP", "TT+lensing", "TT+lowP+lensing", "TT+lensing+BAO", "TT+lowP+lensing+BAO"]

values                 = [0.078, 0.070, 0.066, 0.067, 0.066]

err_up                 = [0.019, 0.024, 0.016, 0.016, 0.013]

err_down               = [0.019, 0.024, 0.016, 0.016, 0.013]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = False
