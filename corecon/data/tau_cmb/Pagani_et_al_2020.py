dictionary_tag         = "Pagano et al. 2020"

reference              = "Pagano, Delouis, Mottet, Puget, Vibert; A&A 635, 99 (2020)"

url                    = "https://ui.adsabs.harvard.edu/abs/2020A%26A...635A..99P/abstract"

description            = \
"""
From improved analysis of the Planck High Frequency Instrument (HFI), that greatly reduces the residual large-scale contamination.
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["data used"]

axes                   = ["large-scale polarization", "large-scale polarization + large-scale temperature likelihood + LCDM"]

values                 = [0.0566, 0.059]

err_up                 = [0.0053, 0.006]

err_down               = [0.0062, 0.006] 

err_up2                = None

err_down2              = None

upper_lim              = [False, False]

lower_lim              = [False, False]
