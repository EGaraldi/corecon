dictionary_tag         = "Faisst et al. 2016"

reference              = "Faisst, Capak, Davidzon, Salvato, Laigle, Ilbert, et al.; ApJ 822, 29 (2016)"

url                    = "https://ui.adsabs.harvard.edu/abs/2016ApJ...822...29F/abstract"

description            = \
"""
Builds a relation between line EW and metallicity at z~0, verify up to z~3 and apply to 3.5 <= z <= 6 (<z>=4.8) in COSMOS + DEIMOS + SPLASH. 
"""

data_structure         = "points" #grid or points

extracted              = True

ndim                   = 3

dimensions_descriptors = ["redshift", "log stellar mass [Msun]", "galaxy Lya"]

axes                   = [[4.8, 8.827051, "average"], [4.8, 9.45898004, "average"], [4.8, 10.33665928, "average"], \
                          [4.8, 8.828542, "with Lya"], [4.8, 9.4240246, "with Lya"], [4.8, 10.35147, "with Lya"], \
                          [4.8, 9.605407, "no Lya"], [4.8, 10.310403, "no Lya"]]

values                 = [8.05361305, 8.12043512, 8.32090132, 8.01799856, 8.03959683, 8.16054716, 8.4600432 , 8.70050396]

err_up                 = [0.27661228, 0.16627817, 0.1989122, 0.28797696, 0.17854572, 0.22894168, 0.11951044, 0.13678906]

err_down               = [0.37451437, 0.26107226, 0.37296037, 0.3700504 , 0.26061915, 0.38156947, 0.25917927, 0.34701224]

upper_lim              = False

lower_lim              = False
