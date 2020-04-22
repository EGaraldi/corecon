dictionary_tag         = "Giallongo et al. 2015"

reference              = "Giallongo, Grazian, Fiore, Fontana, Pentericci, Vanzella, et al.; A&A 578, 83 (2015)"

url                    = "https://www.aanda.org/articles/aa/abs/2015/06/aa25334-14/aa25334-14.html"

description            = \
"""
Based on 22 AGNs first selected in the NIR (H band) and then in X-ray (with 4 Ms on Chandra).
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_1450"]

axes                   = [[4.25, 4.75, 5.75], [-19, -20, -21, -22.5]]

values                 = [[-4.35, -4.56, -4.83, None], [-4.14, -4.56, -4.79, -5.30], [-4.70, -4.70, -5.68, None]]

err_up                 = [[0.49, 0.27, 0.38, None], [0.31, 0.36 , 0.33, 0.51], [0.51, 0.31, 0.51, None]]

err_down               = [[0.88, 0.36, 0.46, None], [0.34, 0.47, 0.49, 0.89], [0.88, 0.31, 0.88, None]]

err_up2                = None

err_down2              = None

upper_lim              = [[False, False, False, False],
                          [False, False, False, False],
                          [False, False, False, False]]

lower_lim              = [[False, False, False, False],
                          [False, False, False, False],
                          [False, False, False, False]]
