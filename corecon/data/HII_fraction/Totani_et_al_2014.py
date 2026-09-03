dictionary_tag = "Totani et al. 2014"

reference = "Totani, T., Aoki, K., Hattori, T., Kosugi, G., Niino, Y., Hashimoto, T., et al., PASJ, 66, 63 (2014)"

url = "https://academic.oup.com/pasj/article-abstract/66/3/63/1437340"

description = \
"""
Neutral hydrogen fraction derived from the spectral analysis of the damping wing of the GRB 130606A afterglow at $z=5.913$. 
The IGM model assumes a uniform distribution of HI, either with fixed redshift interval (5.67 < z < 5.913 = z_GRB) or treating the upper redshift as free parameter.
"""

extracted = False

data_structure         = "grid" #grid or points

ndim                   = 2

dimensions_descriptors = ["redshift", "IGM_model"]

axes                   = [[5.8], ["fixed_dz", "variable_dz"]]

values   = [[0.914, 0.53]]

err_down = [[0.012, 0.08]]

err_up   = [[0.011, 0.07]]

upper_lim = False

lower_lim = False
