dictionary_tag         = "Venturi et al. 2024"

reference              = "G. Venturi, S. Carniani, E. Parlanti, M. Kohandel, M. Curti, et al., (subm.)"

url                    = "https://ui.adsabs.harvard.edu/abs/2024arXiv240303977V/abstract"

description            = \
"""
spatially resolved metallicity in three systems at z~6-8 with JWST NIRSpec IFU low-resolution (R ∼ 100) spectroscopic observations
"""

#data_structure         = "points" #grid or points

extracted              = False

#ndim                   = 2

#dimensions_descriptors = ["redshift", "log stellar mass [Msun]"]

redshift               = [7.879, 7.880, 7.881, 7.877, 7.872, 7.883, 7.882, 7.878,7.114, 7.114, 7.112, 6.361, 6.358, 6.359, 6.362, 6.356]
redshift_err_up        = 0.0
redshift_err_down      = 0.0
redshift_upper_lim     = False
redshift_lower_lim     = False
redshift_units         = ""

log_stellar_mass           = [8.69, 8.40, 7.83, 7.82, 7.58, 8.58, 8.44, 8.01,7.90, 8.21, 7.62, 9.29, 8.81, 8.89, 8.53, 8.40]
log_stellar_mass_err_up    = [0.18, 0.27, 0.46, 0.41, 0.18, 0.28, 0.43, 0.28, 0.25, 0.30, 0.44, 0.09, 0.11, 0.10, 0.30, 0.72]
log_stellar_mass_err_down  = [0.17, 0.13, 0.22, 0.48, 0.37, 0.19, 0.23, 0.47, 0.13, 0.11, 0.14, 0.08, 0.17, 0.06, 0.22, 0.32]
log_stellar_mass_upper_lim = False
log_stellar_mass_lower_lim = False
log_stellar_mass_units     = "Msun"

log_gas_metallicity           = [8.19, 8.27, None, None, None, 8.11, 7.98, 7.72, 7.68, 7.69, 7.80, 8.20, 8.11, 8.33, 8.01, 7.95]
log_gas_metallicity_err_up    = [0.09, 0.16, None, None, None, 0.05, 0.07, 0.20, 0.13, 0.10, 0.15, 0.05, 0.04, 0.08, 0.08, 0.14]
log_gas_metallicity_err_down  = [0.13, 0.20, None, None, None, 0.07, 0.09, 0.20, 0.09, 0.06, 0.38, 0.06, 0.07, 0.10, 0.12, 0.17]
log_gas_metallicity_upper_lim = False
log_gas_metallicity_lower_lim = False
log_gas_metallicity_units     = ""

SFR                    = [2.2, 1.0, 0.87, 1.1, 1.1, 2.85, 2.02, 1.09, 3.47, 4.2, 1.5, 14.4, 9.8, 1.74, 14.5, 3.43]
SFR_err_up             = [0.2, None, None, None, None, 0.18, 0.13, 0.16, 0.13, 0.2, 0.2, 1.3, 0.3, 0.09, 1.3, 0.11]
SFR_err_down           = [0.2, None, None, None, None, 0.18, 0.13, 0.16, 0.13, 0.2, 0.2, 1.3, 0.3, 0.09, 1.3, 0.11]
SFR_upper_limit        = [False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False]
SFR_lower_limit        = False
SFR_units              = "Msun/yr"