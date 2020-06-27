dictionary_tag         = "Kakiichi et al. 2018"

reference              = "Kakiichi, Ellis, Laporte, Zitrin, Eilers, et al.; MNRAS 479, 43 (2018)"

url                    = "https://academic.oup.com/mnras/article/479/1/43/4999925"

description            = \
"""
Measurements from a Keck DEIMOS spectroscopic survey centered on a Keck ESI QSO sightline. The constraints come from seven colour-selected LBGs in the range 
5.3 < z < 6.4 and the Ly-a/Ly-b transmission fluctuations in the QSO sightline.
NOTE: We have derived the correlation from the original data (i.e. the transmitted flux) by taking the most-distant point as a measure of the average transmitted 
      flux at that redshift. The original data and errors are stored in the flux, err_up_flux, and err_down_flux arrays.
NOTE: The three points between 3 and 5 pMpc are biased high by the presence of a nearby QSO.
"""

data_structure         = "grid" #grid or points

extracted              = True #False if the original paper provides number, True if extracted from plots

ndim                   = 2

dimensions_descriptors = ["redshift", "proper distance (pMpc)"]

axes                   = [[6.0], [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]]

values                 = [[2.22076336,  0.71755725,  0.63572519,  0.40458015,  2.52793893, 1.63419847,  3.49435115, -0.21496183, -0.33038168,  0.0]]

err_up                 = [[2.78149211,  0.75185978,  0.62679114,  0.46659183,  1.96928336, 1.47762254,  3.87712682, -0.17919231, -0.31903575,  0.0]]

err_down               = [[2.78149211,  0.75185978,  0.62679114,  0.46659183,  1.96928336, 1.47762254,  3.87712682, -0.17919231, -0.31903575,  0.0]]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = False

err_left               = 0.25

err_right              = 0.25

flux                   = [[0.010548, 0.005625, 0.005357, 0.0046  , 0.011554, 0.008627, 0.014719, 0.002571, 0.002193, 0.003275]]

err_up_flux            = [[6.2770e-03, 2.1960e-03, 1.7600e-03, 2.2810e-03, 1.4050e-03, 2.1290e-03, 6.6550e-03, 4.5300e-04, 6.7600e-04, 2.1530e-03]]

err_down_flux          = [[6.2770e-03, 2.1960e-03, 1.7600e-03, 2.2810e-03, 1.4050e-03, 2.1290e-03, 6.6550e-03, 4.5300e-04, 6.7600e-04, 2.1530e-03]]
