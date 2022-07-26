dictionary_tag         = "WMAP 7yr"

reference              = "Komatsu, Smith, Dunkley, Bennett, Gold, et al.; ApJSS 192, 18 (2011)"

url                    = "https://iopscience.iop.org/article/10.1088/0067-0049/192/2/18/pdf"

description            = \
"""
Cosmological parameter result from the 7yr WMAP data.
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["dataset"]

axes                   = ["WMAP", "WMAP+BAO+H0"]

values                 = [0.088, 0.088]

err_up                 = [0.015, 0.014]

err_down               = [0.015, 0.014]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = False
