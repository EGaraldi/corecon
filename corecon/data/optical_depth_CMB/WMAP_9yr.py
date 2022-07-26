dictionary_tag         = "WMAP 9yr"

reference              = "Hinshaw, Larson, Komatsu, Spergel, Bennet, et al.; ApJSS 208, 19 (2013)"

url                    = "https://iopscience.iop.org/article/10.1088/0067-0049/208/2/19/pdf"

description            = \
"""
Cosmological parameter result from the final 9yr WMAP data.
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["dataset"]

axes                   = ["WMAP", "WMAP+BAO+H0"]

values                 = [0.089, 0.088]

err_up                 = [0.014, 0.013]

err_down               = [0.014, 0.013]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = False
