dictionary_tag         = "Lu et al. 2020"

reference              = "Lu, Goto, Tang, Hashimoto, Wong, Chiang, et al.; ApJ. 893, 69 (2020)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/ab7db7/pdf"

description            = \
"""
Constraints based on the Lyman forest absorption in the QSO PSO J006.1240+39.2219. The constraints are
derived from the dark pixel statistics, using both a '2-sigma' threshold and a 'zero-flux' threshold.
The last point is based on the Lyman-beta forest, the others on the Lyman-alpha.
"""

data_structure         = "grid" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 2

dimensions_descriptors = ["redshift", "flux threshold"]

axes                   = [[6.43, 6.25, 6.08, 5.92, 5.76, 5.61, 6.45], ["2-sigma", "zero-flux"]]

values                 = [[0.06, 0.22], [0.04, 0.19], [0.06, 0.22], [0.00, 0.09], [0.06, 0.44], [0.06, 0.28], [0.02, 0.03]]

err_up                 = [[0.08, 0.07], [0.08, 0.08], [0.08, 0.08], [0.09, 0.09], [0.09, 0.07], [0.09, 0.08], [0.09, 0.09]]

err_down               = [[0.06, 0.07], [0.04, 0.08], [0.06, 0.08], [0.00, 0.09], [0.06, 0.07], [0.06, 0.08], [0.02, 0.03]]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = True
