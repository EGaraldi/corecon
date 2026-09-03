dictionary_tag = "Bolan et al. 2022"

reference = "Bolan, P., Lemaux, B. C., Mason, C., Brada\\v{c}, M., Treu, T., Strait, V., et al., MNRAS 517 3263 (2022)"

url = "https://academic.oup.com/mnras/article/517/3/3263/6763455"

description = \
"""From Bayesian inference applied to the Ly-a EW distribution of a large spectroscopic samples of low-luminosity gravitationally-lensed Lyman break galaxies observed with Keck/DEIMOS and Keck/MOSFIRE.
The paper infers an upper limit x_HI <= 0.25 (0.44) at z = 6.7 +- 0.2 and x_HI = 0.83 (+0.08, -0.11) (+0.11, -0.21) at
z = 7.6 +- 0.6, both within 68 (95) per cent uncertainty. These are converted here to the ionized fraction
Q_HII = 1 - x_HI, which swaps the upper and lower errors and turns the upper limits on x_HI into lower limits on Q_HII.
The two limits at z = 6.7 are the same constraint at the two confidence levels, and are reported as two datapoints
distinguished by the confidence_level field; for the measurement at z = 7.6 the 68 and 95 per cent uncertainties are in
err_up/err_down and err_up2/err_down2 respectively.
"""

data_structure         = "grid" #grid or points

extracted = True
 
ndim                   = 1

dimensions_descriptors = ["redshift"]

axes = [6.7, 6.7, 7.6]

err_left = [0.2, 0.2, 0.6]

err_right = [0.2, 0.2, 0.6]

values = [0.75, 0.56, 0.17]

err_down = [None, None, 0.08]

err_up = [None, None, 0.11]

err_down2 = [None, None, 0.11]

err_up2 = [None, None, 0.21]

lower_lim = [True, True, False]

upper_lim = False

confidence_level = [0.68, 0.95, None]
