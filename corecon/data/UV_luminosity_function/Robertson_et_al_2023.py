dictionary_tag         = "Robertson et al. 2023"

reference              = "Robertson, Johnson, Tachella, Eisenstein, Hainline, Arribas, et al.; arXiv (2023)"

url                    = "https://ui.adsabs.harvard.edu/abs/2023arXiv231210033R/abstract"

description            = \
"""
Data from 14-filters photometry of the JADES Origin Field, the deepest JWST imaging at publication time. Identify 8 
galaxy candidates at 11.5 < z < 15.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[12.5, -18.5], [12.5, -18], [12.5, -17.7], [14.25, -18.5], [14.25, -18.1]]

values                 = [-3.91721463, -3.51999306, -3.86966623, -3.88941029, -4.16749109]

err_up                 = [0.24559423, 0.24672027, 0.24624319, 0.29424401, 0.29459589]

err_down               = [0.62038737, 0.62874859, 0.62518379, 1.50852972, 1.53147892]

err_left               = [[1.0, 0.45], [1.0, 0.18], [1.0, 0.19], [0.75, 0.5], [0.75, 0.23]]

err_right              = [[1.0, 0.30], [1.0, 0.14], [1.0, 0.69], [0.75, 0.16], [0.75, 1.13]]

upper_lim              = False

lower_lim              = False
