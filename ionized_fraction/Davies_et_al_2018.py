dictionary_tag         = "Davies et al. 2018"

reference              = "Davies, Hennawi, Banados, Lukić, Decarli, Fan, Farina, Mazzucchelli, Rix, Venemans, Walter, Wang, Yang; ApJ 864, 142 (2018)"
        
description            = \
"""
Uses a large-volume semi-numerical simulation of reionization topology combined with 1D radiative transfer through high-resolution 
hydrodynamical simulations of the high-redshift universe to construct models of quasar transmission spectra during reionization.
Uses a Bayesian method to jointly constrain the neutral fraction of the universe and the quasar lifetime from individual quasar spectra. 
This methodology is applied to the spectra of ULAS J1120+0641 and ULAS J1342+0928.
"""

data_structure         = "grid" #grid or points
 
ndim                   = 1

dimensions_descriptors = ["redshift"]

axes               = [7.09, 7.54]

values               = [0.48, 0.60]

err_up                 = [0.26, 0.20]

err_down               = [0.26, 0.23]

err_up2                = None

err_down2              = None

upper_lim              = [False, False]

lower_lim              = [False, False]
