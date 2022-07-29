dictionary_tag         = "Stefanon et al. 2022"

reference              = "Stefanon, Bouwens, Labbe, Illingworth, Oesch, van Dokkum, Gonzalez; ApJ 927, 48 (2022)"

url                    = "https://ui.adsabs.harvard.edu/abs/2022ApJ...927...48S/abstract"

description            = \
"""
Based on stacking of >100 Lyman-break galaxies in the GREATS+CANDELS/UDS + CANDELS/COSMOS fields.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 3

dimensions_descriptors = ["redshift", "log stellar mass [Msun]", "SFR method"]

axes                   = [[7.76, 9.2, "UV"], [7.76, 9.2, "OIII+Hbeta"], [7.69, 8.4, "UV"], [7.69, 8.4, "OIII+Hbeta"], \
                          [7.75, 7.8, "UV"], [7.75, 7.8, "OIII+Hbeta"], [7.70, 7.1, "UV"], [7.70, 7.1, "OIII+Hbeta"]]

values                 = [22.2, 35.6, 6.7, 19.3, 3.4, 8.7, 1.2, 3.1]

err_up                 = [1.4, 12.3, 0.5, 5.2, 0.2, 3.5, 0.1, None]

err_down               = [1.4, 12.3, 0.5, 5.2, 0.2, 3.5, 0.1, None]

err_right              = [[0.0, 0.2, None], [0.0, 0.2, None], [0.0, 0.2, None], [0.0, 0.2, None], \
                          [0.0, 0.6, None], [0.0, 0.6, None], [0.0, 0.9, None], [0.0, 0.9, None]]

err_left               = [[0.0, 0.2, None], [0.0, 0.2, None], [0.0, 0.5, None], [0.0, 0.5, None], \
                          [0.0, 0.1, None], [0.0, 0.1, None], [0.0, 0.0, None], [0.0, 0.0, None]]

upper_lim              = False

lower_lim              = [False, False, False, False, False, False, False, True]
