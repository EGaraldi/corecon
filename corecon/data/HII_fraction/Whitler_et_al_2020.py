dictionary_tag = "Whitler et al. 2020"

reference = "Whitler, L. R., Mason, C. A., Ren, K., Dijkstra, M., Mesinger, A., Pentericci, L., et~al., MNRAS 495 3602 (2020)"

url = "https://academic.oup.com/mnras/article/495/4/3602/5831078"

description = \
"""From a sample of 68 Lyman-break galaxies at z~7 in legacy fields. From modeling the galaxy UV luminosity, with and without scatter in the DM halo-L_UV relation, and of the IGM attenuation.
The paper quotes the neutral fraction, x_HI = 0.55 (+0.11, -0.13) including a scatter of 0.5 mag in the UV luminosity
to halo mass relation, and x_HI = 0.59 (+0.12, -0.14) without scatter, both at z ~ 7 and as 68 per cent credible
intervals. These are converted here to the ionized fraction Q_HII = 1 - x_HI, which swaps the upper and lower errors.
The no-scatter case is a reanalysis of the sample of Mason et al. 2018, and is therefore not an independent constraint.
"""

data_structure         = "grid" #grid or points

extracted = True
 
ndim                   = 2

dimensions_descriptors = ["redshift", "scatter"]

axes = [[7], ["yes", "no"]]

values = [[0.45, 0.41]]

err_up = [[0.13, 0.14]]

err_down = [[0.11, 0.12]]

upper_lim = False

lower_lim = False
