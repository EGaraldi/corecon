dictionary_tag         = "Bouwens et al. 2023a"

reference              = "Bouwens, Illingworth, Oesch, Naidu, van Leeuwen, Magee, MNRAS 523, 1009 (2023)"

url                    = "https://ui.adsabs.harvard.edu/abs/2023MNRAS.523.1009B/"

description            = \
"""
Based on JWST NIRCam observations of galaxies in the SMACS0723, GLASS Parallel, and CEERS fields. Total of 18 z ~ 8, 12 z ~ 10, 5 z ~ 13, and 1 z ~ 17 candidate galaxies.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[8, -21.13], [8, -20.13], [8, -19.13], [10, -20.49], [10, -19.49], [13, -20.96], [13, -19.96], [17, -21.96]]

values                 = [-4.33724217, -4.35654732, -2.9788107 , -4.74472749, -3.88605665, -5., -4.49485002, -4.74472749]
 
err_up                 = [0.25105602, 0.25963731, 0.14435178, 0.27620641, 0.18272184, 0.25527251, 0.30103   , 0.24987747]

err_down               = [0.66275783, 0.74036269, 0.21773218, 0.95424251, 0.32155166, 0.69897   ,     np.inf, 0.65321251]

upper_lim              = False

lower_lim              = False
