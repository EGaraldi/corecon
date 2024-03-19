dictionary_tag         = "Venturi et al. 2024"

reference              = "G. Venturi, S. Carniani, E. Parlanti, M. Kohandel, M. Curti, et al., (subm.)"

url                    = "https://ui.adsabs.harvard.edu/abs/2024arXiv240303977V/abstract"

description            = \
"""
spatially resolved metallicity in three systems at z~6-8 with JWST NIRSpec IFU low-resolution (R ∼ 100) spectroscopic observations
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[7.879, 8.69], [7.880, 8.40], [7.881, 7.83], [7.877, 7.82], [7.872, 7.58], [7.883, 8.58], [7.882, 8.44], [7.878, 8.01],
                          [7.114, 7.90], [7.114, 8.21], [7.112, 7.62], [6.361, 9.29], [6.358, 8.81], [6.359, 8.89], [6.362, 8.53], [6.356, 8.40]]

err_right              = [[0.0, 0.18], [0.0, 0.27], [0.0, 0.46], [0.0, 0.41], [0.0, 0.18], [0.0, 0.28], [0.0, 0.43], [0.0, 0.28],
                          [0.0, 0.25], [0.0, 0.30], [0.0, 0.44], [0.0, 0.09], [0.0, 0.11], [0.0, 0.10], [0.0, 0.30], [0.0, 0.72]]

err_left               = [[0.0, 0.17], [0.0, 0.13], [0.0, 0.22], [0.0, 0.48], [0.0, 0.37], [0.0, 0.19], [0.0, 0.23], [0.0, 0.47], 
                          [0.0, 0.13], [0.0, 0.11], [0.0, 0.14], [0.0, 0.08], [0.0, 0.17], [0.0, 0.06], [0.0, 0.22], [0.0, 0.32]]

values                 = [8.19, 8.27, None, None, None, 8.11, 7.98, 7.72, 7.68, 7.69, 7.80, 8.20, 8.11, 8.33, 8.01, 7.95]

err_up                 = [0.09, 0.16, None, None, None, 0.05, 0.07, 0.20, 0.13, 0.10, 0.15, 0.05, 0.04, 0.08, 0.08, 0.14]

err_down               = [0.13, 0.20, None, None, None, 0.07, 0.09, 0.20, 0.09, 0.06, 0.38, 0.06, 0.07, 0.10, 0.12, 0.17]

upper_lim              = False

lower_lim              = False

SFR                    = [2.2, 1.0, 0.87, 1.1, 1.1, 2.85, 2.02, 1.09, 3.47, 4.2, 1.5, 14.4, 9.8, 1.74, 14.5, 3.43]

err_down_SFR           = [0.2, None, None, None, None, 0.18, 0.13, 0.16, 0.13, 0.2, 0.2, 1.3, 0.3, 0.09, 1.3, 0.11]

err_up_SFR             = [0.2, None, None, None, None, 0.18, 0.13, 0.16, 0.13, 0.2, 0.2, 1.3, 0.3, 0.09, 1.3, 0.11]

upper_lim_SFR          = [False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False]

lower_lim_SFR          = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
