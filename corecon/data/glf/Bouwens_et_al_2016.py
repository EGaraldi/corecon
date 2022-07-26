dictionary_tag         = "Bouwens et al. 2016"

reference              = "Bouwens, Oesch, Labbe, Illingworth, Fazio, et al.; ApJ. 830, 67 (2016)"

url                    = "https://iopscience.iop.org/article/10.3847/0004-637X/830/2/67"

description            = \
"""
Using data from the z9-CANDELS project. Candidates pre-selected from the full HST, 
Spitzer/IRAC, S-CANDELS, CFHTLS-DEEP + HUGS + UltraVISTA + ZFOURGE observations. 15 galaxies
were identified at 9 < z < 10.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_1600"]

axes                   = [[9.0, -21.94], [9.0, -21.14], [9.0, -20.34], [10.0, -22.05], [10.0, -21.25], [10.0, -20.45]]

values                 = [-5.61978876, -5.35654732, -4.49214413, -5.76955108, -6.04575749, -4.74472749]

err_up                 = [None, 0.29104577, 0.22373289, None, 0.52287875, 0.29373076]

err_down               = [None, 0.34242268, 0.24303805, None, 0.65321251, 0.34145865]

err_up2                = None

err_down2              = None

upper_lim              = [True, False, False, True, False, False]

lower_lim              = False
