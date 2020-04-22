dictionary_tag         = "Schaye et al. 2000"

reference              = "Schaye, Theuns, Rauch, Efstathiou, Sargent; MNRAS 318, 817 (2000)"  
 
url                    = "http://articles.adsabs.harvard.edu/pdf/2000MNRAS.318..817S"

description            = \
"""
Based on the cut-off in the distribution of Ly-alpha absorption lines b parameter in 9 QSO spectra.
"""

data_structure         = "grid" #grid or points

extracted              = True

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [1.95, 2.2 , 2.27, 2.5 , 2.6 , 2.66, 2.84, 3.01, 3.09, 3.24, 3.36, 3.54, 3.72, 3.84, 3.9 , 4.3 ]

values                 = [10665., 13800., 11776., 13900., 15770., 22540., 17140., 22750., 19590., 22390., \
                          15400., 10900., 12650., 13180., 15300., 11450.]

err_up                 = [3000., 5000., 1750., 2530., 1400., 6900., 3080., 4550., 1520., \
                          8500., 1700., 2100., 1780., 2440., 3960., 2165.]

err_down               = [3000., 5000., 1750., 2530., 1400., 6900., 3080., 4550., 1520., \
                          8500., 1700., 2100., 1780., 2440., 3960., 2165.]

err_up2                = None

err_down2              = None

upper_lim              = [False, False, False, False, False, False, False, False, False, False, False, \
                          False, False, False, False, False ]

lower_lim              = [False, False, False, False, False, False, False, False, False, False, False, \
                          False, False, False, False, False ]
