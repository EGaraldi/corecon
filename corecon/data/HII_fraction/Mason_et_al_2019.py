dictionary_tag = "Mason et al. 2019"

reference   = "Mason, Fontana, Treu, Schmidt, Hoag, Abramson, Amorin, Bradac, Guaita, Jones, Henry, Malkan, Pentericci, Trenti, Vanzella; MNRAS 485, 3947 (2019)"

url         = "https://academic.oup.com/mnras/article/485/3/3947/5369632"

description = \
"""
Bayesian framework based on detection/non-detection of Ly-alpha emission from lensed LBGs in the KLASS survey.
The two datapoints are the same constraint at z = 8 quoted at the 68 and 95 per cent confidence level, and are
reported here as two datapoints distinguished by the confidence_level field. They are upper limits on the ionized
fraction Q_HII = 1 - x_HI, corresponding to lower limits on the neutral fraction x_HI.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [8.0, 8.0]

values      = [0.24, 0.54]

err_up      = None

err_down    = None

upper_lim     = True

lower_lim     = False

confidence_level = [0.68, 0.95]
