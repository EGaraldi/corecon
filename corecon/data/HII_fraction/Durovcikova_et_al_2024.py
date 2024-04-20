dictionary_tag = "Durovcikova et al. 2024 (subm.)"

reference   = "Durovcikova, Eilers, Chen, Satyavolu, Kulkarni, Simcoe, Keating, et al.; arXiv:2401.10328"
 
url         = "https://ui.adsabs.harvard.edu/abs/2024arXiv240110328D/abstract"

description = \
"""From the damping wing of 18 QSOs in the range 6.1<z<7, compared to two sets of simulations (CROC and ATON-based models). The inference marginalizes over the QSO lifetime.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "simulation model"]

axes                   = [[6.10, "ATON"], [6.10, "CROC"], [6.46, "ATON"], [6.46, "CROC"], [6.87, "ATON"], [6.87, "CROC"]]

err_left               = [[0.1, None], [0.1, None], [0.16, None], [0.16, None], [0.17, None], [0.17, None]]

err_right              = [[0.2, None], [0.2, None], [0.24, None], [0.24, None], [0.23, None], [0.23, None]]

values      = [0.21, 0.10, 0.21, 0.57, 0.37, 0.57]

err_down    = [0.07, 1e-4, 0.07, 0.47, 0.17, 0.21]

err_up      = [0.17, 0.73, 0.33, 0.26, 0.17, 0.26]

upper_lim     = False

lower_lim     = False
