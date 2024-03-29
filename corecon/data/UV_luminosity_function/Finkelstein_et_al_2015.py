dictionary_tag         = "Finkelstein et al. 2015"

reference              = "Finkelstein, Ryan, Papovich, Dickinson, Song, et al.; ApJ. 810, 71 (2015)"

url                    = "https://iopscience.iop.org/article/10.1088/0004-637X/810/1/71"

description            = \
"""
Data from the Cosmic Assembly Near-infrared Deep Extragalactic Legacy Survey/GOODS fields, the Hubble Ultra 
Deep Field, and the Hubble Frontier Field deep parallel observations near the Abell 2744 and MACS J0416.1-2403 clusters,
for a final sample of 7446 candidate galaxies at 3.5 < z < 8.5, with > 1000 galaxies at z ~ 6–8. For this dataset M_UV = M_1500
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[4,5,6,7,8], [-23, -22.5, -22, -21.5, -21, -20.5, -20, -19.5, -19, -18.5, -18, -17.5]]

values                 = [[-5.79588002, -5.03151705, -4.55658054, -3.92372374, -3.5275361 ,
                           -3.18768839, -2.89835601, -2.7787162 , -2.5785277 , -2.4416635 ,
                           -2.23401124, -2.18803645],
                          [-5.63827216, -5.08618615, -5.08618615, -4.12033079, -3.59108198,
                           -3.28558641, -3.03081714, -2.91771741, -2.68039432, -2.43313844,
                           -2.32457914, -2.14970919],
                          [-5.60205999, -5.60205999, -5.04095861, -4.4710833 , -4.15304467,
                           -3.71896663, -3.40120949, -3.23225063, -3.07701518, -2.61172114,
                           -2.43578385, -2.2282215 ],
                          [-5.537602  , -5.537602  , -5.33724217, -4.7242281 , -4.16115091,
                           -3.8857227 , -3.56193255, -3.41476494, -3.24420134, -2.59091263,
                           -2.51173138,        None],
                          [-5.45593196, -5.45593196, -5.45593196, -5.10237291, -4.82390874,
                           -4.21112488, -3.95979337, -3.66274046, -3.21659672, -2.82073554,
                                  None,        None]
                         ]

err_up                 = [[     None, 0.17139614, 0.1026294 , 0.04985515, 0.03241456,
                           0.02350575, 0.01665382, 0.01613426, 0.01918494, 0.07480864,
                           0.06124478, 0.06323666],
                          [      None, 0.20676008, 0.21003779, 0.07215383, 0.04117706,
                           0.02956627, 0.02168855, 0.01719087, 0.02451139, 0.04326605,
                           0.0421165 , 0.07228415],
                          [      None,       None, 0.21122032, 0.11748703, 0.08297424,
                           0.05321928, 0.04109424, 0.03741153, 0.04507764, 0.06407501,
                           0.10545397, 0.09514062],
                          [      None,       None, 0.31496577, 0.1615029 , 0.08852127,
                           0.07324342, 0.05622632, 0.06613988, 0.14336498, 0.12728166,
                           0.13100215,       None],
                          [      None,       None,       None, 0.26969024, 0.21129857,
                           0.12068091, 0.12205899, 0.2625144 , 0.19769014, 0.23296081,
                                  None,       None]
                         ]

err_down               = [[      None, 0.1903317 , 0.10977071, 0.05097039, 0.03328916,
                           0.0238604 , 0.01660328, 0.01643156, 0.0196067 , 0.08008755,
                           0.06581309, 0.06852435],
                          [      None, 0.24171599, 0.25105602, 0.0782655 , 0.0426819 ,
                           0.02929912, 0.02307463, 0.02461649, 0.02454463, 0.04623394,
                           0.04247792, 0.07593446],
                          [      None,       None, 0.24303805, 0.12579618, 0.08728748,
                           0.05546565, 0.04092255, 0.03366996, 0.04498035, 0.0674059 ,
                           0.11302863, 0.10164402],
                          [      None,       None, 0.40748533, 0.19048132, 0.10165645,
                           0.07248998, 0.05551013, 0.07175111, 0.16674313, 0.14217395,
                           0.14713098,       None],
                          [      None,       None,       None, 0.37911315, 0.27300127,
                           0.1356626 , 0.14368041, 0.37158757, 0.2447039 , 0.31050251,
                                 None,       None]
                         ]

err_up2                = None

err_down2              = None

upper_lim              = [[ True, False, False, False, False, False, False, False, False,
                           False, False, False],
                          [ True, False, False, False, False, False, False, False, False,
                           False, False, False],
                          [ True,  True, False, False, False, False, False, False, False,
                           False, False, False],
                          [ True,  True, False, False, False, False, False, False, False,
                           False, False, False],
                          [ True,  True,  True, False, False, False, False, False, False,
                           False, False, False]
                         ]

lower_lim              = False
