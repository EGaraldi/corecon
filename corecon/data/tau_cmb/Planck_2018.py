dictionary_tag         = "Planck 2018"

reference              = "Planck Collaboration; subm. (2018)"

url                    = "https://www.aanda.org/component/article?access=doi&doi=10.1051/0004-6361/201833910"

description            = \
"""
Cosmological parameter result from the final full-mission Planck measurements of the CMB anisotropies.
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["dataset"]

axes                   = ["TT+lowE", "TE+lowE", "EE+lowE", "TT,TE,EE+lowE", "TT,TE,EE+lowE+lensing", "TT,TE,EE+lowE+lensing+BAO"]

values                 = [0.0522, 0.0496, 0.0527, 0.0544, 0.0544, 0.0561]

err_up                 = [0.0080, 0.0085, 0.0090, 0.0070, 0.0073, 0.0071]

err_down               = [0.0080, 0.0085, 0.0090, 0.0081, 0.0073, 0.0071]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = False
