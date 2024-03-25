dictionary_tag         = "Donnan et al. 2023a"

reference              = "Donnan, McLeod, Dunlop, McLure, Carnall, Begley, Cullen, et al.; MNRAS 518, 6011 (2023)"

url                    = "https://academic.oup.com/mnras/article/518/4/6011/6849970"

description            = \
"""
Based on a combination of COSMOS and JWST's SMACS0723, GLASS and CEERS data, resulting in 55 galaxy candidates at
8 < z < 15 (6 at z>12). 
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[8, -22.17], [8, -21.42], [9, -22.30], [9, -21.30], [9, -18.50], 
                          [10.5, -22.57], [10.5, -20.10], [10.5, -19.35], [10.5, -18.85], [10.5, -18.23], 
                          [13.25, -20.35], [13.25, -19]]

values                 = [-6.20065945, -5.40671393, -6.76955108, -5.51999306, -2.92081875,
                          -6.74472749, -4.79048499, -3.86646109, -3.62911698, 
                          -3.20010832, -4.98716278, -4.56224944]

err_up                 = [0.25373789, 0.20328827, 0.52542593, 0.3650911 , 0.20344087,
                          0.52287875, 0.36567283, 0.1743848 , 0.16301608, 
                          0.18723808, 0.29423073, 0.25333093]

err_down               = [0.28082661, 0.22037406, 0.75332767, 0.45062317, 0.21944268,
                          0.77815125, 0.45364016, 0.18463715, 0.17195115, 
                          0.20022691, 0.33981632, 0.28241453]

err_left               = [0.5, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.375, 0.85, 0.5]

err_right              = [0.5, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.375, 0.85, 0.5]

upper_lim              = False

lower_lim              = False
