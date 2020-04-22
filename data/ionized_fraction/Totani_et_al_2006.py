dictionary_tag = "Totani et al. 2006"

reference   = "Totani, Kawai, Kosugi, Aoki, Yamada, Iye, Ohta, Hattori; PASJ 58, 485 (2006)"

url         = "https://academic.oup.com/pasj/article/58/3/485/1503875"

description = \
"""
Based on spectral modeling of the optical afterglow to the gamma-ray burst (GRB) 050904 at z = 6.3. The spectrum is taken by the Subaru Telescope.
The damping wing redward of the Lyman break can be fit either by a damped Ly alpha system with a column density of log (N_HI/cm^{-2}) ~ 21.6 
at a redshift close to the detected metal absorption lines (z_metal = 6.295), or by almost neutral IGM extending to a slightly higher redshift 
of z_{IGM,u} ~ 6.36. Constraint on the neutral fraction is obtained by the damping wing modeling.
"""

data_structure         = "grid" #grid or points

extracted              = False

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [6.3]

values      = [0.5]

err_up      = [None]

err_down    = [None]

err_up2     = None

err_down2   = None

upper_lim     = [False]

lower_lim     = [True]
