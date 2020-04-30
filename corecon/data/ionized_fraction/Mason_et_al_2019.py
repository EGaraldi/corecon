dictionary_tag = "Mason et al. 2019"

reference   = "Mason, Fontana, Treu, Schmidt, Hoag, Abramson, Amorin, Bradac, Guaita, Jones, Henry, Malkan, Pentericci, Trenti, Vanzella; MNRAS 485, 3947 (2019)"

url         = "https://academic.oup.com/mnras/article/485/3/3947/5369632"

description = \
"""
Bayesian framework based on detection/non-detection of Ly-alpha emission from lensed LBGs in the KLASS survey.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "confidence level"]

axes                   = [[8.0],[0.68, 0.95]]

values      = [[0.24,0.54]]

err_up      = None

err_down    = None

err_up2     = None

err_down2   = None

upper_lim     = [[True, True]]

lower_lim     = [[False,False]]
