dictionary_tag         = "Roberts-Borsani et al. 2022"

reference              = "Roberts-Borsani, Morishita, Treu, Leethochawalit, Trenti; ApJ 927, 236 (2022)"

url                    = "https://ui.adsabs.harvard.edu/abs/2022ApJ...927..236R/abstract"

description            = \
"""
Based on a systematic search for luminous z~8 galaxy candidates with HST, using ~1267 arcmin2 of (pure-)parallel observations from a compilation of 
288 random sightlines with Advanced Camera for Surveys and Wide Field Camera 3 observations, resulting in 31 galaxy candidates.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[8.0], [9.62, 9.69, 9.47, 9.65, 9.77, 9.68, 9.59, 9.58, 9.45, 9.37, 9.37,
                                  9.73, 9.43, 9.31, 9.56, 9.65, 9.46]]

values                 = [[0.46, 0.5 , 0.44, 0.49, 0.6 , 0.56, 0.42, 0.58, 0.52, 0.45, 0.48,
                           0.55, 0.35, 0.44, 0.51, 0.55, 0.52]]

err_up                 = [[0.26, 0.24, 0.28, 0.28, 0.24, 0.26, 0.27, 0.26, 0.27, 0.28, 0.29,
                            0.25, 0.3 , 0.29, 0.27, 0.27, 0.29]]

err_down               = [[0.26, 0.24, 0.28, 0.28, 0.24, 0.26, 0.27, 0.26, 0.27, 0.28, 0.29,
                           0.25, 0.3 , 0.29, 0.27, 0.27, 0.29]]

#err_left               = [[0.0], [0.25, 0.22, 0.3 , 0.22, 0.17, 0.2 , 0.22, 0.26, 0.34, 0.29, 0.3 ,
#                                  0.17, 0.24, 0.3 , 0.27, 0.21, 0.29]]
#
#err_right              = [[0.0], [0.25, 0.22, 0.3 , 0.22, 0.17, 0.2 , 0.22, 0.26, 0.34, 0.29, 0.3 ,
#                                  0.17, 0.24, 0.3 , 0.27, 0.21, 0.29]]

err_left               = [[0.25, 0.22, 0.3 , 0.22, 0.17, 0.2 , 0.22, 0.26, 0.34, 0.29, 0.3 ,
                           0.17, 0.24, 0.3 , 0.27, 0.21, 0.29]]

err_right              = [[0.25, 0.22, 0.3 , 0.22, 0.17, 0.2 , 0.22, 0.26, 0.34, 0.29, 0.3 ,
                           0.17, 0.24, 0.3 , 0.27, 0.21, 0.29]]

upper_lim              = False

lower_lim              = False
