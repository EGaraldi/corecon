dictionary_tag         = "Walther et al. 2019"

reference              = "Walther, Onorbe, Hennawi, Lukic; ApJ. 872, 13 (2019)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/aafad1"

description            = \
"""
Constraints obtained comparing the Lyman-alpha forest power spectrum to hydrodynamical simulations. Uses Bayesian inference and end-to-end 
forward modeling.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4. , 4.2, 4.6, 5. , 5.4]

values                 = [ 6840.,  7340.,  7890.,  8310., 10000., 10000., 14290., 11150., \
                           13300., 10100., 10290.,  8630.,  9050.,  9100.,  5350.,  5970.]

err_up                 = [1800.,  930.,  850., 1120., 1460., 1120., 3130., 2300., 2950., \
                          3600., 2870., 2710., 1220., 1190., 1170., 1520.]

err_down               = [1220.,  710.,  680.,  780.,  900.,  870., 2710., 1490., 2150., \
                          2960., 2460., 1870.,  820., 1170.,  920., 1320.]

err_up2                = None

err_down2              = None

upper_lim              = [False, False, False, False, False, False, False, False, False, \
                          False, False, False, False, False, False, False]

lower_lim              = [False, False, False, False, False, False, False, False, False, \
                          False, False, False, False, False, False, False]
