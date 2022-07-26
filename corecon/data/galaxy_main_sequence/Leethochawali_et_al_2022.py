dictionary_tag         = "Leethochawali et al. 2022"

reference              = "Leethochawali, Trenti, Santini, Yang, Merlin, Castellano, et al.; subm. (2022)"

url                    = "https://arxiv.org/pdf/2207.11135.pdf"

description            = \
"""
Based on broadband imaging (0.8-5 micron) using the NIRCam instrument on JWST, as part of the GLASS-JWST program. Angular resolution < ~0.14 arcsec. 8 galaxies identified at S/N>8.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[7.3, 8.7], [8.0, 8.2], [6.7, 9.5], [7.7, 8.6], [7.3, 8.6], [8.4, 7.9], [8.8, 8.7], \
                          [8.2, 8.4], [8.2, 8.6], [7.9, 8.9], [8.1, 9.0], [8.3, 8.7], [8.3, 9.0], [8.3, 8.8]]

values                 = [1.9, 1.1, 12.9, 4.5, 2.1, 0.8, 2.6, 1.9, 2.2, 4.8, 4.5, 3.1, 4.7, 2.9]

err_up                 = [0.8, 0.4, 3.9, 1.9, 0.5, 0.1, 0.8, 0.5, 0.5, 1.3, 2.8, 1.0, 3.8, 1.3]

err_down               = [0.5, 0.5, 3.3, 1.6, 0.6, 0.1, 0.5, 0.7, 0.7, 1.9, 1.2, 0.7, 2.1, 2.6]

err_left               = [[5.2, 0.3], [0.6, 0.5], [0.2, 0.1], [0.4, 0.2], [5.4, 0.3], [0.2, 0.0], [0.5, 0.2],\
                          [0.4, 0.4], [0.6, 0.4], [6.1, 0.4], [0.6, 0.2], [0.5, 0.2], [0.5, 0.6], [5.6, 0.4]]

err_right              = [[0.5, 0.1], [0.6, 0.2], [0.2, 0.1], [0.3, 0.2], [0.5, 0.2], [0.2, 0.1], [0.4, 0.2],\
                          [0.4, 0.3], [0.6, 0.2], [0.4, 0.1], [0.6, 0.2], [0.4, 0.1], [0.5, 0.3], [0.5, 0.1]]

upper_lim              = False

lower_lim              = False
