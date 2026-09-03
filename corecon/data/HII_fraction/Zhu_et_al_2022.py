dictionary_tag = "Zhu et al. 2022"

reference   = "Zhu, Becker, Bosman, Keating, D'ODorico, Davies, et al.; ApJ 932, 76 (2022)"
 
url         = "https://ui.adsabs.harvard.edu/abs/2022ApJ...932...76Z/abstract"

description = \
"""From dark gaps in the Ly-beta forest of 42 QSOs at z>5.5
The paper infers the upper limits x_HI <= 0.05 (+0.04, -0.04), 0.17 (+0.05, -0.05) and 0.29 (+0.09, -0.10) at
z = 5.55, 5.75 and 5.95, over redshift bins of width dz = 0.2 (given as err_left and err_right). These are converted
here to lower limits on the ionized fraction Q_HII = 1 - x_HI, which swaps the upper and lower errors.
The values are 68 per cent (1 sigma) limits, as recorded in the confidence_level field; the errors quoted alongside
them are the uncertainty on the limit itself, obtained by resampling the neutral fraction from the gap length
distribution f(x_HI|L) 10,000 times.
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [5.55, 5.75, 5.95]

err_left               = [0.1, 0.1, 0.1]

err_right              = [0.1, 0.1, 0.1]

values      = [0.95, 0.83, 0.71]

err_down    = [0.04, 0.05, 0.09]

err_up      = [0.04, 0.05, 0.10]

upper_lim     = False

lower_lim     = True

limit_confidence_level = 0.68
