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

values                 = [[8.23727789, 8.27349007, 8.21797274, 8.26471614, 8.35267131,
                           8.32270809, 8.19776935, 8.33794806, 8.29052341, 8.22773258,
                           8.2557613 , 8.31488275, 8.11858811, 8.21797274, 8.28209024,
                           8.31488275, 8.29052341]]

err_up                 = [[0.19457466, 0.17026172, 0.21387982, 0.19629465, 0.14612804,
                           0.16562583, 0.2155998 , 0.16085129, 0.18162375, 0.21011035,
                           0.20524949, 0.1627273 , 0.26884531, 0.21987018, 0.18452443,
                           0.17345116, 0.19248168]]

err_down               = [[0.36172784, 0.28399666, 0.43933269, 0.36797679, 0.22184875,
                           0.27106677, 0.44715803, 0.25827802, 0.31806333, 0.42276359,
                           0.40248764, 0.26324143, 0.84509804, 0.46736142, 0.32735893,
                           0.29320466, 0.35427551]]

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
