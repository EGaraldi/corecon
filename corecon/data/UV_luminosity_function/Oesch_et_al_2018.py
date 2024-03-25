dictionary_tag         = "Oesch et al. 2018"

reference              = "Oesch, Bouwens, Illingworth, Labbe, Stefanon; ApJ. 855, 105 (2018)"

url                    = "https://iopscience.iop.org/article/10.3847/1538-4357/aab03f"

description            = \
"""
Constraints based on a serach for z>10 galaxies in all HST legacy fields. UVLF based on 9 sources
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[10.0], [-22.25, -21.25, -20.25, -19.25, -18.25, -17.25]]

values                 = [[-5.76955108, -6.0, -5.0, -4.46852108, -3.7212464 ,-3.20065945]]

err_up                 = [[None, 0.50514998, 0.30103, 0.36614817, 0.36469908, 0.52699531]]

err_down               = [[None, 0.69897, 0.30103, 0.45229767, 0.43365556, 0.75794786]]

upper_lim              = [[True, False, False, False, False, False]]

lower_lim              = False
