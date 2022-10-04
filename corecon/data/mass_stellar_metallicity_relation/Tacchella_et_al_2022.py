dictionary_tag         = "Tacchella et al. 2022"

reference              = "Tacchella, Finkelstein, Bagley, Dickinson, Ferguson, Giavalisco, et al.; ApJ 927, 170 (2022)"

url                    = "https://ui.adsabs.harvard.edu/abs/2022ApJ...927..170T/abstract"

description            = \
"""
Based on the stellar population analysis of 11 bright (H < 26.6) galaxies at z = 9-11 (three spectroscopically confirmed).
NOTE: The author find inconsistent results when using different priors, and caution against relying on their results.
We use here the results from their fiducial choice of priors.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[9.77, 10.9], [9.83, 9.3], [8.68, 10.6], [8.66, 10.2], [9.16, 9.1], [8.51, 10.0], \
                          [9.06, 9.6], [9.40, 9.7], [8.48, 9.9], [10.96, 9.1], [9.54, 11.0]]

values                 = [-0.4, -1.2, -0.5, -1.3, -1.5, -1.0, -1.1, -1.1, -1.0, -1.1, 0.0]

err_up                 = [0.3, 0.7, 0.4, 0.6, 0.5, 0.7, 0.7, 0.8, 0.6, 0.8, 0.1]

err_down               = [0.7, 0.6, 0.7, 0.4, 0.3, 0.6, 0.6, 0.6, 0.7, 0.6, 0.5]

err_right              = [[0.19, 0.2], [0.28, 0.3], [0.0, 0.2], [0.0, 0.2], [0.28, 0.2], [0.33, 0.3], \
                          [0.29, 0.3], [0.36, 0.3], [0.39, 0.4], [0.0, 0.3], [0.09, 0.4]]

err_left               = [[0.19, 0.2], [0.39, 0.4], [0.0, 0.3], [0.0, 0.2], [0.24, 0.3], [0.49, 0.4], \
                          [0.28, 0.3], [0.33, 0.4], [0.54, 0.4], [0.0, 0.2], [0.1, 0.2]]

upper_lim              = False

lower_lim              = False
