dictionary_tag         = "Lam et al. 2019"

reference              = "Lam, Bouwens, Labbe, Schaye, Schmidt, Maseda, Bacon, et al., A&A 627, 164 (2019)"

url                    = "https://ui.adsabs.harvard.edu/abs/2019A%26A...627A.164L/abstract"

description            = \
"""
From 200h Spitzer/IRAC (GREATS program) + ~300 3<z<6 galaxies with spec. redshifts from MUSE (GTO Deep + Wide 
programs) data of galaxies fainter than 0.2 L* at z = 4-5. These data correspond to average value in M_UV bins.
The original paper contains also values binned in log(Mstar) and beta.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[4.0, -20], [4.0, -19], [4.0, -18]]

err_left               = [[1.0, 0.5], [1.0, 0.5], [1.0, 0.5]]

err_right              = [[1.0, 0.5], [1.0, 0.5], [1.0, 0.5]]

values                 = [25.28, 25.31, 25.49]

err_up                 = [0.08, 0.12, 0.15]

err_down               = [0.09, 0.17, 0.22]

upper_lim              = False

lower_lim              = False
