dictionary_tag         = "Kauffmann et al. 2022"

reference              = "Kauffmann, Ilbert, Weaver, McCracken, Milvang-Jensen, Brammer, et al.; arXiv (2022)"

url                    = "https://arxiv.org/pdf/2207.11740.pdf"

description            = \
"""
Based on a search for z > 7.5 galaxies in the COSMOS 2020 catalog, covering 1.4 deg2, resulting in 17 candidates
with redshift 7.5 < z < 10
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[8, -22.75], [8, -22.25], [8, -21.75], [9, -22.5], [9, -21.75], [10, -22.5]]

values                 = [-6.45593196, -5.86327943, -5.69036983, -6.08618615, -5.44611697, -6.67778071 ]

err_up                 = [None, 0.19165904, 0.19005692, 0.20676008, 0.23357745, 0.34987856]

err_down               = [None, 0.35139073, 0.34584234, 0.40866387, 0.5410458, 100]

err_left               = [0.25, 0.25, 0.25, 0.5, 0.25, 0.5]

err_right              = [0.25, 0.25, 0.25, 0.5, 0.25, 0.5]

upper_lim              = [True, False, False, False, False, False]

lower_lim              = False
