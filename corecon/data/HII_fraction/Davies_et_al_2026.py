dictionary_tag = "Davies et al. 2026"

reference = "Davies, F. B., Bosman, S. E. I., D'Odorico, V., Campo, S., Mesinger, A., Qin, Y., et al., MNRAS 545 1862 (2026)"

url = "https://academic.oup.com/mnras/article/545/2/staf1862/8305915"

description = \
"""From dark-pixel statistics of the E-XQR-30 sample (34 quasar spectra at 5.8<z<6.6. Using Ly-a, Ly-b and Ly-g forest. Constraints derived using three methods: threshold, negative pixel, and lognormal mixture methods, applied to 3.3~Mpc binned spectral segments.
Table 3 of the paper gives upper limits on the neutral fraction as the central value of the dark fraction plus its +1
sigma (+2 sigma) uncertainty, i.e. the quoted limit is value + error; these are converted here to lower limits on the
ionized fraction Q_HII = 1 - x_HI, with the 1 and 2 sigma uncertainties on the bound in err_up/err_down and
err_up2/err_down2 respectively.
The authors adopt the negative pixel method as their fiducial one.
"""

data_structure         = "grid" #grid or points

extracted = False

ndim                   = 2

dimensions_descriptors = ["redshift", "method"]

axes = [[4.875, 5.056, 5.272, 5.481, 5.654, 5.831, 6.043, 6.225], ['threshold', 'negative', 'mixture']]

values = [[0.905, 0.94 , 0.956], [0.905, 0.937, 0.965], [0.873, 0.945, 0.928],[0.869, 0.97 , 0.924], [0.779, 0.905, 0.849], [0.707, 0.809, 0.778], [0.604, 0.801, 0.705], [0.396, 0.391, 0.531]]

err_up = [[0.023, 0.023, 0.017], [0.018, 0.017, 0.001], [0.022, 0.031, 0.014], [0.056, 0.048, 0.031], [0.047, 0.037, 0.039], [0.039, 0.056, 0.044], [0.093, 0.087, 0.061], [0.153, 0.143, 0.139]]

err_down = [[0.023, 0.023, 0.017], [0.018, 0.017, 0.001], [0.022, 0.031, 0.014], [0.056, 0.048, 0.031], [0.047, 0.037, 0.039], [0.039, 0.056, 0.044], [0.093, 0.087, 0.061], [0.153, 0.143, 0.139]]

err_up2 = [[0.052, 0.053, 0.036], [0.038, 0.036, 0.023], [0.045, 0.075, 0.030], [0.117, 0.141, 0.075], [0.095, 0.085, 0.076], [0.081, 0.126, 0.081], [0.205, 0.202, 0.118], [0.267, 0.293, 0.245]]

err_down2 = [[0.052, 0.053, 0.036], [0.038, 0.036, 0.023], [0.045, 0.075, 0.030], [0.117, 0.141, 0.075], [0.095, 0.085, 0.076], [0.081, 0.126, 0.081], [0.205, 0.202, 0.118], [0.267, 0.293, 0.245]]

lower_lim = True

upper_lim = False
