dictionary_tag         = "Bouwens et al. 2009"

reference              = "Bouwens, Illingworth, Franx, Chary, Meurer, Conselice, Ford, Giavalisco, van Dokkum, ApJ 705, 936 (2009)"

url                    = "https://iopscience.iop.org/article/10.1088/0004-637X/705/1/936/pdf"

description            = \
"""
From deep opticl and infrared data over the Chandra deep field south, Hubble deep field north and UDF. The values are corrected for both selection bias 
and photometric scatter.
Note: the authors provide systematic, random and 'corrected' errors. err_up and err_down contain the latter, while the others are provided as extra fields.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [2.5, 2.5, 2.5, 2.5, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 
                          5.0, 5.0, 5.0, 5.0, 6.0, 6.0]

values                 = [-1.18, -1.58, -1.54, -1.88, -1.32, -1.33, -1.44, -1.51, -1.58,
                          -1.68, -1.73, -1.93, -1.98, -2.03, -1.91, -1.81, -1.76, -2.17,
                          -2.64, -2.16, -2.32]

err_up                 = [0.32, 0.27, 0.34, 0.36, 0.51, 0.31, 0.44, 0.4 , 0.34, 0.35, 0.55,
                          0.31, 0.54, 0.29, 0.26, 0.45, 0.64, 0.66, 1.02, 0.41, 0.91]

err_down               = [0.32, 0.27, 0.34, 0.36, 0.51, 0.31, 0.44, 0.4 , 0.34, 0.35, 0.55,
                          0.31, 0.54, 0.29, 0.26, 0.45, 0.64, 0.66, 1.02, 0.41, 0.91]

upper_lim              = False

lower_lim              = False

err_up_systematic      = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
                          0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]

err_down_systematic    = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
                          0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]

err_up_random          = [0.17, 0.1 , 0.06, 0.05, 0.12, 0.07, 0.04, 0.03, 0.1 , 0.09, 0.07,
                          0.06, 0.05, 0.04, 0.05, 0.22, 0.1 , 0.08, 0.16, 0.15, 0.19]

err_down_random        = [0.17, 0.1 , 0.06, 0.05, 0.12, 0.07, 0.04, 0.03, 0.1 , 0.09, 0.07,
                          0.06, 0.05, 0.04, 0.05, 0.22, 0.1 , 0.08, 0.16, 0.15, 0.19]

M_UV                   = [-21.73, -20.73, -19.73, -18.73, -22.22, -21.72, -21.22, -20.72,
                          -20.22, -19.72, -19.22, -18.72, -18.22, -17.72, -17.22, -21.9 ,
                          -20.9 , -19.9 , -18.9 , -20.76, -18.76]
