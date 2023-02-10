dictionary_tag         = "Bouwens et al. 2022"

reference              = "Bouwens, Stefanon, Brammer, Oesch, Herard-Demanche, Illingworth, et al., sub."

url                    = "https://arxiv.org/pdf/2211.02607.pdf"

description            = \
"""
Based on JWST NIRCam observations of galaxies in the HUDF. Total of 10 galaxies at 8 < z < 13.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[8.7, -20.02], [8.7, -18.77], [10.5, -18.65], [12.6, -20.31], [12.6, -19.31]]

values                 = [0.000164, 0.000378, 0.00029 , 0.000116, 0.00019 ]

err_up                 = [0.29837375, 0.2575643 , 0.26023592, 0.25776131, 0.25527251]

err_down               = [1.91381385, 0.7201593 , 0.74639465, 0.72203531, 0.69897   ]

upper_lim              = False

lower_lim              = False
