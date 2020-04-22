dictionary_tag = "Schenker et al. 2014"

reference   = "Schenker, Ellis, Konidaris, Stark; ApJ 795, 20 (2014)"

url         = "https://iopscience.iop.org/article/10.1088/0004-637X/795/1/20"

description = \
"""
Method based on rest-frame UV continua of galaxies, applied to NIR spectra of z>7 galaxies (Keck MOSFIRE spectroscopic survey at 7 < z < 8).
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [7.0, 8.0]

values      = [0.66, 0.35]

err_up      = [0.12, None]

err_down    = [0.09, None]

err_up2     = None

err_down2   = None

upper_lim     = [False, True]

lower_lim     = [False, False]
