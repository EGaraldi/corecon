dictionary_tag = "Wyithe & Bolton 2011"

reference   = "Wyithe, Bolton, MNRAS 412, 1926 (2011)"

url         = "https://academic.oup.com/mnras/article/412/3/1926/1056129"

description = \
"""From the proximity effect of 15 QSOs at 4.6 < z < 6.4. Gamma is derived by 
pixel-by-pixel modeling of the combined radiation from the quasar and from the 
background."""

data_structure         = "points" #grid or points

extracted              = True
        
ndim        = 1

dimensions_descriptors = ["redshift"]

axes        = [5.0, 6.0]

values      = [4.7e-13, 1.8e-13]

err_up      = [3e-13, 1.8e-13]

err_down    = [2e-13, 0.9e-13]

upper_lim     = False

lower_lim     = False
