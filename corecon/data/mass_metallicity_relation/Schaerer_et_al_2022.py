dictionary_tag         = "Schaerer et al. 2022"

reference              = "Schaerer, Marques-Chaves, Oesch, Naidu, Barrufet, et al.; subm. (2022)"

url                    = "https://arxiv.org/pdf/2207.10034.pdf"

description            = \
"""
From the ERO JWST observations of SMACS J0723.3-7327 with NIRSpec. Based on two galaxies at z=7.7 and one at z=8.5.
NOTE: The authors provide 3 determinations of O/H. We use as fiducial value the "direct" method when available and the "strong line" 
when not. The upper/lower error encloses the range of values obtained with the three methods.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

axes                   = [[8.495, 8.1024], [7.664, 8.9696], [7.660, 8.6696]]

values                 = [7.36, 7.85, 7.85]

err_up                 = [0.14, 0.0, 0.15]

err_down               = [0.0, 0.09, 0.0]

upper_lim              = False

lower_lim              = False
