dictionary_tag         = "Faisst et al. 2016"

reference              = "Faisst, Capak, Davidzon, Salvato, Laigle, Ilbert, et al.; ApJ 822, 29 (2016)"

url                    = "https://ui.adsabs.harvard.edu/abs/2016ApJ...822...29F/abstract"

description            = \
"""
Builds a relation between line EW and metallicity at z~0, verify up to z~3 and apply to 3.5 <= z <= 6 (<z>=4.8) in COSMOS + DEIMOS + SPLASH. 
"""

data_structure         = "grid" #grid or points

extracted              = True

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[4.8],[8.827051, 9.45898004, 10.33665928]]

values                 = [[8.05361305, 8.12043512, 8.32090132]]

err_up                 = [[0.27661228, 0.16627817, 0.1989122]]

err_down               = [[0.37451437, 0.26107226, 0.37296037]]

upper_lim              = False

lower_lim              = False
