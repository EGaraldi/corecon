dictionary_tag         = "Furtak et al. 2022"

reference              = "Furtak, Shuntov, Atek, Zitrin, Richard, Lehnert, Chevallard, subm. (2022)"

url                    = "https://arxiv.org/pdf/2208.05473.pdf"

description            = \
"""
detailed sedMfitting analysis of the 16 gravitationally lensed z ~ 10 - 16 galaxy candidates detected behind the galaxy cluster smacs J0723.37327 in
Atek et al. (2022).
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["log stellar mass [Msun]", "redshift"]

axes                   = [[9.03, 9.97], [9.81, 9.79], [9.80, 10.08], [7.41, 9.64], [7.24, 10.46],
                          [7.43, 10.67], [7.43, 10.95], [7.64, 11.30], [7.20, 11.21], [8.08, 11.03], 
                          [7.21, 11.54], [8.14, 12.00], [8.10, 12.44], [8.31, 16.02], [8.00, 15.79]]

values                 = [-1.82, -0.31, -1.84, -0.92, -0.84,
                          -1.06, -0.59, -0.79, -1.43, -1.32,
                          -1.11, -1.30, -1.02, -1.16, -1.00]

err_up                 = [0.24, 0.01, 0.81, 0.25, 0.36, 0.18, 0.2, 0.29, 0.24, 0.59, 0.35, 0.55, 0.53, 0.36, 0.43]

err_down               = [0.1, 0.01, 0.11, 0.23, 0.25, 0.25, 0.23, 0.23, 0.25, 0.46, 0.47, 0.48, 0.51, 0.26, 0.67]

err_left               = [[0.23, 0.1], [0.07, 0.2], [0.2, 0.13], [0.97, 1.28], [0.92, 2.6],
                          [0.97, 0.2], [0.1, 0.16], [1.26, 0.24], [1.09, 0.18], [1.48, 0.61],
                          [0.93, 0.27], [1.42, 0.16], [1.55, 0.26], [1.33, 0.27], [1.53, 0.31]]

err_right              = [[0.23, 0.07], [0.07, 0.2], [0.08, 0.09], [0.77, 0.70], [1.13, 0.4], 
                          [1.00, 0.22], [1.18, 0.15], [1.15, 0.21], [1.35, 0.14], [1.32, 0.48],
                          [1.15, 0.23], [0.54, 0.16], [0.85, 0.65], [0.39, 0.24], [1.23, 0.32]]

upper_lim              = False

lower_lim              = False
