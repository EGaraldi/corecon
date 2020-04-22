dictionary_tag         = "Morishita et al. 2018"

reference              = "Morishita, Trenti, Stiavelli, Bradley, Coe, et al.; ApJ. 867, 150 (2018)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/aae68c"

description            = \
"""
Based on the BoRG[z9] survey (~370 arcmin^2). 
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[9, 10], [-23, -22, -21]]

values                 = [[-5.9, -5.9, -5.4], [-6.1, -5.9, -4.6]]

err_up                 = [[None, 0.5, 0.5], [0.5, None, None]]

err_down               = [[None, 0.8, 0.8], [0.8, None, None]]

err_up2                = None

err_down2              = None

upper_lim              = [[True, False, False], [False, True, True]]

lower_lim              = False
