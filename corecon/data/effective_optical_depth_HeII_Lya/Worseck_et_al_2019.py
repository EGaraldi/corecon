dictionary_tag         = "Worseck et al. 2019"

reference              = "Worseck, Davies, Hennawi, Prochaska; ApJ. 875, 11 (2019)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/ab0fa1"

description            = \
"""
Measurements in 16 HeII-transparent QSOs observed with HST/COS.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [2.60,2.64,2.68,2.72,2.76,2.56,2.60,2.64,2.68,2.72,2.76,2.80,2.68,2.72,2.76,2.80,2.84,
                          2.88,2.72,2.76,2.80,2.84,2.88,3.12,3.16,3.20,2.76,2.80,2.84,2.88,2.92,3.08,3.12,3.16,2.68,2.72,
                          2.76,2.80,2.84,2.88,3.08,3.12,3.16,3.20,3.24,2.72,2.76,2.80,2.84,2.88,2.92,3.08,3.12,3.16,3.20,
                          3.24,2.80,2.84,2.88,3.12,3.16,3.20,3.36,2.84,2.88,3.12,3.16,3.20,3.24,3.36,2.84,2.88,3.12,3.16,
                          3.20,3.36,3.44,3.08,3.12,3.16,3.20,3.24,3.36,3.40,3.44,3.48,3.52,3.56,3.60,3.64,3.16,3.20,3.24,
                          3.36,3.40,3.52,3.56,3.60,3.64,3.68,3.72,3.08,3.12,3.16,3.20,3.24,3.36,3.40,3.44,3.48,3.52,3.56,
                          3.60,3.64,3.68,3.72,3.20,3.36,3.40,3.52,3.56,3.60,3.64,3.68,3.72,3.36,3.40,3.52,3.56,3.60,3.64,
                          3.68,3.72,3.76,3.20,3.36,3.40,3.44,3.48,3.52,3.56,3.60,3.64,3.68,3.72,3.76,3.80,3.84]

values                 = [1.69,1.12,2.19,2.73,3.04,1.37,1.43,1.09,1.58,1.75,1.55,2.29,2.42,2.24,2.01,1.68,2.26,
                          2.20,1.17,1.52,4.19,1.83,1.91,4.50,4.39,4.41,1.75,2.17,2.07,3.74,4.34,5.29,5.73,4.41,2.12,1.93,
                          2.32,1.84,1.47,3.16,2.14,2.89,5.21,5.37,4.45,2.12,2.74,2.06,2.63,5.02,4.66,4.47,5.36,3.30,4.07,
                          5.70,1.56,1.47,1.93,5.57,5.42,5.56,5.29,2.95,2.62,3.38,3.02,5.42,5.54,5.57,3.13,2.56,5.36,5.74,
                          5.76,5.88,5.94,5.81,3.25,3.91,5.22,5.60,5.56,5.40,5.39,5.24,5.17,5.12,5.19,5.12,5.01,5.23,5.21,
                          5.13,5.01,5.02,4.80,4.77,4.71,4.68,3.96,1.63,4.14,5.44,5.51,5.46,5.28,5.39,5.35,4.89,5.32,5.37,
                          3.86,5.27,5.30,5.29,4.86,4.68,4.73,4.56,4.58,4.52,4.47,4.46,4.38,5.38,4.43,5.45,5.45,5.39,5.34,
                          5.29,5.19,5.15,5.40,5.06,4.85,2.39,3.97,4.72,4.65,4.53,4.46,3.98,4.28,3.04,3.59,3.38]

err_up                 = [0.61, 0.1 , 0.08, 0.15, 0.18, 0.24, 0.04, 0.04, 0.03, 0.02, 0.02,
                          0.02, 0.18, 0.13, 0.09, 0.07, 0.09, 0.1 , 0.16, 0.13,  None, 0.14,
                          0.15,  None,  None,  None, 0.06, 0.07, 0.05, 0.22, 0.45, 0.93,  None,
                          0.3 , 0.32, 0.15, 0.13, 0.09, 0.07, 0.21, 0.08, 0.14,  None,  None,
                          0.64, 0.08, 0.08, 0.09, 0.07, 0.66, 0.45, 0.43, 1.03, 0.09, 0.22,
                          None, 0.06, 0.05, 0.08,  None,  None,  None,  None, 0.15, 0.1 , 0.18,
                          0.14,  None,  None,  None, 0.14, 0.09, 1.05,  None,  None,  None,  None,
                          None, 0.14, 0.24, 1.04,  None,  None,  None,  None,  None,  None,  None,
                          None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,
                          None,  None,  None, 0.84, 0.06, 0.36,  None,  None,  None,  None,  None,
                          None, 1.05,  None,  None, 0.42,  None,  None,  None,  None,  None,  None,
                          None,  None,  None,  None,  None,  None, 1.16, 0.4 ,  None,  None,  None,
                          None,  None,  None,  None,  None,  None, 1.18, 0.15, 0.76,  None,  None,
                          None,  None, 0.44, 1.  , 0.84]

err_down               = [0.01, 0.03, 0.11, 0.09, 0.09, 0.15, 0.11, 0.03, 0.03, 0.04, 0.02,
                          0.05, 0.19, 0.12, 0.09, 0.07, 0.09, 0.09, 0.13, 0.13,  None, 0.12,
                          0.14,  None,  None,  None, 0.06, 0.07, 0.05, 0.18, 0.27, 0.54,  None,
                          0.24, 0.22, 0.13, 0.12, 0.09, 0.06, 0.18, 0.09, 0.13,  None,  None,
                          0.4 , 0.07, 0.12, 0.01, 0.07, 0.49, 0.28, 0.28, 0.52, 0.1 , 0.16,
                          None, 0.06, 0.05, 0.07,  None,  None,  None,  None, 0.13, 0.11, 0.16,
                          0.13,  None,  None,  None, 0.13, 0.08, 0.55,  None,  None,  None,  None,
                          None, 0.13, 0.21, 0.56,  None,  None,  None,  None,  None,  None,  None,
                          None,  None,  None,  None,  None,  None,  None,  None,  None,  None,  None,
                          None,  None,  None, 0.46, 0.06, 0.27,  None,  None,  None,  None,  None,
                          None, 0.59,  None,  None, 0.31,  None,  None,  None,  None,  None,  None,
                          None,  None,  None,  None,  None,  None, 0.59, 0.28,  None,  None,  None,
                          None,  None,  None,  None,  None,  None, 0.65, 0.11, 0.4 ,  None,  None,
                          None,  None, 0.34, 0.54, 0.47]

upper_lim              = False

lower_lim              = [False, False, False, False, False, False, False, False, False,
                          False, False, False, False, False, False, False, False, False,
                          False, False,  True, False, False,  True,  True,  True, False,
                          False, False, False, False, False,  True, False, False, False,
                          False, False, False, False, False, False,  True,  True, False,
                          False, False, False, False, False, False, False, False, False,
                          False,  True, False, False, False,  True,  True,  True,  True,
                          False, False, False, False,  True,  True,  True, False, False,
                          False,  True,  True,  True,  True,  True, False, False, False,
                           True,  True,  True,  True,  True,  True,  True,  True,  True,
                           True,  True,  True,  True,  True,  True,  True,  True,  True,
                           True,  True,  True, False, False, False,  True,  True,  True,
                           True,  True,  True, False,  True,  True, False,  True,  True,
                           True,  True,  True,  True,  True,  True,  True,  True,  True,
                           True, False, False,  True,  True,  True,  True,  True,  True,
                           True,  True,  True, False, False, False,  True,  True,  True,
                           True, False, False, False]
