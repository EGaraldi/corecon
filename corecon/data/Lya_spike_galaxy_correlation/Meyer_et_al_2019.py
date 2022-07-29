dictionary_tag         = "Meyer et al. 2019"

reference              = "Meyer, Bosman, Kakiichi, Ellis; MNRAS 483, 19 (2019)"

url                    = "https://academic.oup.com/mnras/article/483/1/19/5159477"

description            = \
"""
From a sample of 25 high signal-to-noise ratio QSO spectra 150 CIV absorbers are identified at 4.5 < z < 6.2. They are used to determine the
correlation of CIV-absorber systems with transmission spikes in the Ly-a forest.
"""

data_structure         = "grid" #grid or points

extracted              = True #False if the original paper provides number, True if extracted from plots

ndim                   = 2

dimensions_descriptors = ["redshift", "proper distance [pMpc]"]

axes                   = [[5.4], [0.28, 0.86, 1.43, 2.0 , 2.57, 3.14, 3.72, 4.29, 4.86, 5.43, 6.0 ,6.57, 7.15]]

values                 = [[-0.706173, -0.303704,  0.017284, -0.040741,  0.277778,  0.116049, 0.246914,  0.030864, \
                           0.185185,  0.166667,  0.158025,  0.109877, 0.045679]]

err_up                 = [[0.074074, 0.140741, 0.160494, 0.116049, 0.166667, 0.161111, 0.176543, 0.112963, 0.122222, \
                           0.205556, 0.151852, 0.169136, 0.166049]]

err_down               = [[0.074074, 0.140741, 0.160494, 0.116049, 0.166667, 0.161111, 0.176543, 0.112963, 0.122222, \
                           0.205556, 0.151852, 0.169136, 0.166049]]

upper_lim              = False

lower_lim              = False

err_left               = 0.29 

err_right              = 0.29
