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

values                 = [[28.84031503, 30.1995172 , 21.87761624, 32.35936569, 69.18309709,
                           41.68693835, 23.98832919, 26.30267992, 20.41737945, 15.84893192,
                           15.13561248, 47.86300923, 17.37800829, 13.80384265, 26.30267992,
                           41.68693835, 25.11886432]]

err_up                 = [[43.60328098, 35.8698276 , 39.78188395, 45.26534597, 48.3066584 ,
                           49.51414559, 32.24580333, 41.30561762, 42.678355  , 28.81942729,
                           28.51597074, 49.86071286, 26.27357494, 26.00687441, 42.88041717,
                           53.81232026, 39.44655859]]

err_down               = [[17.35877882, 16.39567456, 14.11514507, 18.86973687, 28.44506931,
                           22.63233117, 13.75539927, 16.06975   , 13.81044497, 10.22551867,
                            9.88753788, 24.42072108, 10.45969858,  9.01754172, 16.30267992,
                           23.48992976, 15.34649211]]

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

IRAC_detection_above_3sigma = [[ True,  True,  True,  True,  True, False, False, False, False,
                                 False, False, False, False, False, False, False, False ]]

individual_redshifts =  [[8,8,8,8,9,8,8,8,8,8,8,8,8,8,8,8,10]]
