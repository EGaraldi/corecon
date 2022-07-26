dictionary_tag         = "Giallongo et al. 2019"

reference              = "Giallongo, Grazian, Fiore, Kodra, Urrutia, Castellano, et al.; ApJ. 884, 19 (2019)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/ab39e1"

description            = \
"""
Based on 32 AGN candidatess, updating the sample of Giallongo et al. 2015.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_1450"]

axes                   = [[4.5, 5.55], [-19, -20, -21, -22]]

values                 = [[-4.83743559, -4.94043658, -5.29413629, -5.8827287 ], 
                          [-5.13846559, -5.32148162, -6.16115091, -6.21467016]]

err_up                 = [[0.2040453 , 0.20407265, 0.22508532, 0.36702854], 
                          [0.29652638, 0.25395539, 0.52287875, 0.52642403]]

err_down               = [[0.22155016, 0.22197498, 0.24798182, 0.47381862], 
                          [0.34965105, 0.28758327, 0.88460658, 0.94023179]]

err_up2                = None

err_down2              = None

upper_lim              = [[False, False, False, False],
                          [False, False, False, False]]

lower_lim              = [[False, False, False, False],
                          [False, False, False, False]]
