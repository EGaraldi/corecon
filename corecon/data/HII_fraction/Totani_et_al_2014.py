dictionary_tag = "Totani et al. 2014"

reference = "Totani, T., Aoki, K., Hattori, T., Kosugi, G., Niino, Y., Hashimoto, T., et al., PASJ, 66, 63 (2014)"

url = "https://academic.oup.com/pasj/article-abstract/66/3/63/1437340"

description = \
"""
Neutral hydrogen fraction derived from the spectral analysis of the damping wing of the GRB 130606A afterglow at $z=5.913$.
The IGM model assumes a uniform distribution of HI in a redshift interval [z_IGM_low, z_IGM_up], with the lower bound always
fixed at z_IGM_low = 5.67 (the onset of the dark Gunn-Peterson troughs along this sightline). In the "fixed_dz" model
(IGM-zGRB in the paper) the upper bound is fixed at the GRB redshift, z_IGM_up = z_GRB = 5.913, giving f_HI = 0.086
(+0.012, -0.011); in the "variable_dz" model (IGM-lowzu) z_IGM_up is a free parameter, whose best fit is z_IGM_up = 5.83,
giving f_HI = 0.47 (+0.08, -0.07). Values are reported here as ionized fractions, Q_HII = 1 - f_HI, at the redshift of the
GRB; the redshift interval over which the HI is distributed is given by the z_IGM_low and z_IGM_up fields.
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
