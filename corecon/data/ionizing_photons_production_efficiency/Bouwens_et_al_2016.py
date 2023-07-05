dictionary_tag         = "Bouwens et al. 2016"

reference              = "Bouwens, Smit, Labbe, Franx, Caruana, Oesch, Stefanon, Rasappu, ApJ 831, 176 (2016)"

url                    = "https://ui.adsabs.harvard.edu/abs/2016ApJ...831..176B/abstract"

description            = \
"""
Based on the impact of Halpha on the IRAC fluxes of sources selected in deep HST observations (GOODS fields). 
The data below correspond to the one binned in M_UV and for the SMC dust attenuation curve.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[4.4, 5.25], [-22.5, -21.5, -20.5, -19.5]]

values                 = [[25.14, 25.28, 25.34, 25.34], [None, 25.43, 25.48, 25.73]]

err_up                 = [[0.14, 0.03, 0.03, 0.05], [None, 0.10, 0.17, 0.08]]

err_down               = [[0.26, 0.03, 0.03, 0.06], [None, 0.11, 0.14, 0.10]]

upper_lim              = False

lower_lim              = False
