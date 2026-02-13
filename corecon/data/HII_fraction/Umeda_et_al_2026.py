dictionary_tag = "Umeda et al. 2026"

reference = "Umeda, H., Ouchi, M., Kageura, Y., Harikane, Y., Nakane, M., Thai, T.~T., et~al., ApJ 997 86 (2026)"

url = "https://iopscience.iop.org/article/10.3847/1538-4357/ae232b"

description = \
"""Derived from joint analysis of Gunn-Peterson trough + galaxy damping wing, based on JWST/NIRSpec spectroscopy of 581 galaxies at $z=4.5-13$. 
Uses composite spectra binned by redshift and matched for UV properties, compared against low-redshift templates. IGM inhomogeneity included using semi-numerical simulations.
"""

data_structure         = "points" #grid or points

extracted = False

ndim = 1

dimensions_descriptors = ['redshift']

axes = [5.0, 5.8, 7.0, 8.6, 10.4]

values   = [1.00, 0.75, 0.35, 0.00, 0.00]

err_down = [0.12, 0.10, 0.27, 0.00, 0.00]

err_up   = [0.00, 0.20, 0.35, 0.20, 0.40]

upper_lim = False

lower_lim = False
