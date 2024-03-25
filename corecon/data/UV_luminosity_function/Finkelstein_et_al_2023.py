dictionary_tag         = "Finkelstein et al. 2023"

reference              = "Finkelstein, Leung, Bagley, Dickinson, Ferguson, Papovich, Akins, et al.; arXiv (2023)" 

url                    = "https://arxiv.org/pdf/2311.04279.pdf"

description            = \
"""
Based on 88 candidate galaxies at 8.5<z<14.5 from the CEERS survey. The data cover ~90 arcmin^2 using six broad band filters and one mediu band filter
"""

data_structure         = "points" #grid or points

extracted              = False

ndim                   = 2

dimensions_descriptors = ["redshift", "M_UV"]

axes                   = [[9, -22.5], [9, -22], [9, -21.5], [9, -21], [9, -20.5], [9, -20], [9, -19.5], [9, -19], [9, -18.5],
                          [11, -21], [11, -20.5], [11, -20], [11, -19.5], [11, -19], [11, -18.5], 
                          [14, -20.5], [14, -20.0], [14, -19.5]]

values                 = [-5.04575749, -4.95860731, -5.04575749, -4.65757732, -4.08618615, -4.01772877, -3.54363397, -3.57186521, -2.86646109, 
                          -5.30103   , -4.74472749, -4.26760624, -4.11918641, -3.75448733, -3.58004425,
                          -4.74472749, -4.58502665, -4.13667714]

err_up                 = [      None, 0.21387982,       None, 0.20164536, 0.17254598, 0.17001711, 0.14677834, 0.16515127, 0.16092732,
                                None, 0.22184875, 0.17609126, 0.17988425, 0.20009154, 0.22840426,
                                None, 0.35587866, 0.28896548]

err_down               = [      None, 0.34242268,       None, 0.26324143, 0.21484385, 0.20411998, 0.16633142, 0.20282551, 0.19853576,
                                None, 0.30103   , 0.21387982, 0.21805576, 0.25874093, 0.3060124 ,
                                None, 0.51188336, 0.40092486]

upper_lim              = [True, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False]

lower_lim              = False
