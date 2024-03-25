dictionary_tag         = "Bouwens et al. 2023b"

reference              = "Bouwens, Stefanon, Brammer, Oesch, Herard-Demanche, Illingworth, et al., MNRAS 523, 1936 (2023)"

url                    = "https://ui.adsabs.harvard.edu/abs/2023MNRAS.523.1036B/abstract"

description            = \
"""
Based on JWST NIRCam observations of galaxies in the HUDF. Total of 10 galaxies at 8 < z < 13.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[8.7, -20.02], [8.7, -18.77], [10.5, -18.9], [10.5, -17.9], [12.6, -20.06], [12.6, -18.81]]

values                 = [-3.77989191, -3.59859946, -4.06550155, -3.12726117, -4.1079054 ,-3.7212464 ]
 
err_up                 = [0.25410818, 0.29930318, 0.37936877, 0.29869507, 0.25403343,  0.25527251]

err_down               = [0.68862917, 2.10037055,     np.inf, 1.96964884, 0.68797462, 0.69897   ]

upper_lim              = False

lower_lim              = False
