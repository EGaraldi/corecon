dictionary_tag         = "Oesch et al. 2014"

reference              = "Oesch, Bouwens, Illingworth, Labbe, Smit, Franx, et al.; ApJ. 786, 108 (2014)"

url                    = "https://iopscience.iop.org/article/10.1088/0004-637X/786/2/108"

description            = \
"""
Constraints based on 6 galaxy candidates at z~10 in the GOODS-N and GOODS-S fields. 3 (1) of the 4 (2) galaxies 
in the GOODS-N (S) field are significantly detected at >4.5 sigma in deep Spitzer/IRAC 4.5 micrometer data.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[10.0], [-21.28, -20.78, -20.28, -19.78, -19.28, -18.78, -18.28, -17.78]]

values                 = [[-5.56863624, -5.00, -5.1079054 , -4.69897, -4.05060999, -3.60205999, -3.16749109, -2.88605665]]

err_up                 = [[0.30103, 0.20411998, None, None, None, None, None, 0.30103]]

err_down               = [[0.82930377, 0.30103, None, None, None, None, None, 0.81291336]]

err_up2                = None

err_down2              = None

upper_lim              = [[False, False, True, True, True, True, True, False]]

lower_lim              = False
