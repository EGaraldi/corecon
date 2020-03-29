dictionary_tag         = "Rorai et al. 2018"

reference              = "Rorai, Carswell, Haehnelt, Becker, Bolton, Murphy; MNRAS 474, 2871 (2018)"  
        
description            = \
"""
Measurements based on fitting the neutral hydrogen column density and Doppler parameter of Ly-a forest absorption lines.
The results are based on a Bayesian scheme that includes the statistical correlation between the parameters; This scheme 
is applied to either only the b-distribution cut-off or to the media b value.
"""

ndim                   = 2

dimensions_descriptors = ["redshift", "method"]

axes                   = [[2.75], ["cut-off", "median"]]

values                 = [[15600, 14600]]

err_up                 = [[4400, 3700]]

err_down               = [[4400, 3700]]

err_up2                = []

err_down2              = []

upper_lim              = [[False, False]]

lower_lim              = [[False, False]]
