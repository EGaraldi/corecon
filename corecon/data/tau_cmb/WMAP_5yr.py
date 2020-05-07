dictionary_tag         = "WMAP 5yr"

reference              = "Komatsu, Dunkley, Nolta, Bennett, Gold, et al.; ApJSS 180, 330 (2009)"

url                    = "https://iopscience.iop.org/article/10.1088/0067-0049/180/2/330/pdf"

description            = \
"""
Cosmological parameter result from the final 5yr WMAP data.
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["dataset"]

axes                   = ["WMAP", "WMAP+BAO+SN"]

values                 = [0.087, 0.084]

err_up                 = [0.017, 0.016]

err_down               = [0.017, 0.016]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = False
