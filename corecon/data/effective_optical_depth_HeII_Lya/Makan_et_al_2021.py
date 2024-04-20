dictionary_tag         = "Makan et al. 2021"

reference              = "Makan, Worseck, Davies, Hennawi, Prochaska, Richter; ApJ. 912, 38 (2021)"

url                    = "https://ui.adsabs.harvard.edu/abs/2021ApJ...912...38M/abstract"

description            = \
"""From high-resolution (R = 14000) spectra of the two brightest He II-transparent quasars in the far-UV (FUV) at z>3.5, i.e. 
HE2QS J2311-1417(z = 3.70) and HE2QS J1630+0435 (z = 3.81). We report the values from the high-resolution spectra and omit the one from mid-resolution.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [3.08,3.12,3.16,3.20,3.24,3.36,3.40,3.44,3.48,3.52,3.56,3.60,3.64,3.68,3.72,3.08,3.12,
                          3.16,3.20,3.24,3.36,3.40,3.44,3.48,3.52,3.56,3.60,3.64]

values                 = [2.01,3.69,4.88,4.38,4.22,4.57,4.77,4.75,4.73,4.69,4.57,3.62,4.48,4.43,4.16,4.59,4.55,
                          5.35,4.68,4.60,4.94,5.04,4.93,4.89,4.86,4.76,4.70,4.67]

err_up                 = [0.09, 0.42,  None,  None,  None,  None,  None,  None,  None,  None,  None,
                          0.55,  None,  None,  None, 0.66, 0.63,  None,  None,  None,  None,  None,
                          None,  None,  None,  None,  None,  None]

err_down               = [0.09, 0.31,  None,  None,  None,  None,  None,  None,  None,  None,  None,
                          0.36,  None,  None,  None, 0.40, 0.39,  None,  None,  None,  None,  None,
                          None,  None,  None,  None,  None,  None]

upper_lim              = False

lower_lim              = [False, False,  True,  True,  True,  True,  True,  True,  True,
                          True,  True, False,  True,  True,  True, False, False,  True,
                          True,  True,  True,  True,  True,  True,  True,  True,  True,
                          True]
