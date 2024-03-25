dictionary_tag         = "Leung et al. 2023"

reference              = "Leung, Bagley, Finkelstein, Ferguson, Koekemoer, Perez-Gonzalez, et al.; ApJL 954, L46 (2023)"

url                    = "https://iopscience.iop.org/article/10.3847/2041-8213/acf365/pdf"

description            = \
"""
From the NGDEEP survey. NIRCam imaging over 9.7 arcmin^2 of the HUDF Parallel Field 2 reaching m=30.4
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[9, -21.1], [9, -20.1], [9, -19.1], [9, -18.35], [9, -17.85], [9, -17.35],
                          [10.75, -20.05], [10.75, -19.35], [10.75, -18.65], [10.75, -17.95], [10.75, -17.25]]

values                 = [-4.05060999, -3.83268267, -3.7235382 , -3.13076828, -2.76955108, -2.28483264, 
                          -4.01322827, -3.73282827, -3.55752023, -3.22841252,  -2.57024772]

err_up                 = [       None, 0.24430237, 0.23808595, 0.19297409, 0.17609126, 0.16962801,
                                 None, 0.21570186, 0.22027806, 0.23273389, 0.20873698]

err_down               = [       None, 0.29225607, 0.2764618 , 0.21601921, 0.20925962, 0.20866233,
                                 None, 0.25857156, 0.27516243, 0.29737122, 0.26838428]

err_left               = [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.25], [0.5, 0.25], [0.5, 0.25],
                          [1.25, 0.35], [1.25, 0.35], [1.25, 0.35], [1.25, 0.35], [1.25, 0.35]]

err_right              = [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [0.5, 0.25], [0.5, 0.25], [0.5, 0.25],
                          [1.25, 0.35], [1.25, 0.35], [1.25, 0.35], [1.25, 0.35], [1.25, 0.35]]

upper_lim              = [True, False, False, False, False, False, True, False, False, False, False]

lower_lim              = False
