dictionary_tag         = "Tacchella et al. 2022"

reference              = "Tacchella, Finkelstein, Bagley, Dickinson, Ferguson, Giavalisco, et al.; ApJ 927, 170 (2022)"

url                    = "https://ui.adsabs.harvard.edu/abs/2022ApJ...927..170T/abstract"

description            = \
"""
Based on the stellar population analysis of 11 bright (H < 26.6) galaxies at z = 9-11 (three spectroscopically confirmed).
NOTE: The author find inconsistent results when using different priors, and caution against relying on their results.
We use here the results from their fiducial choice of priors.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [ 9.77,  9.83,  8.68,  8.66,  9.16,  8.51,  9.06,  9.4 ,  8.48, 10.96,  9.54]

values                 = [-0.62, -2.11, -1.61, -1.87, -2.37, -1.60, -1.94, -1.80, -1.45, -2.34, -1.41]

err_up                 = [0.11, 0.20, 0.18, 0.11, 0.15, 0.22, 0.14, 0.33, 0.28, 0.13, 0.08]

err_down               = [0.12, 0.18, 0.12, 0.11, 0.11, 0.20, 0.21, 0.24, 0.28, 0.14, 0.06]

err_right              = [0.19, 0.28, 0.  , 0.  , 0.28, 0.33, 0.29, 0.36, 0.39, 0.  , 0.09]

err_left               = [0.19, 0.39, 0.  , 0.  , 0.24, 0.49, 0.28, 0.33, 0.54, 0.  , 0.1 ]

upper_lim              = False

lower_lim              = False

log_Mstar              = [10.9,  9.3, 10.6, 10.2,  9.1, 10. ,  9.6,  9.7,  9.9,  9.1, 11. ]

err_up_log_Mstar       = [0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.4, 0.3, 0.4]

err_down_log_Mstar     = [0.2, 0.4, 0.3, 0.2, 0.3, 0.4, 0.3, 0.4, 0.4, 0.2, 0.2]

M_UV                   = [-22.1, -21.01, -22.1, -21.87, -21.47, -21.12, -21.25, -21.28, -20.70, -21.71, -22.14]

err_up_M_UV            = [0.09, 0.12, 0.05, 0.05, 0.09, 0.18, 0.10, 0.13, 0.23, 0.08, 0.07]

err_down_M_UV          = [0.09, 0.12, 0.05, 0.05, 0.09, 0.14, 0.10, 0.13, 0.16, 0.09, 0.07]
