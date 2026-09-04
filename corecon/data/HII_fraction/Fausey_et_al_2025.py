dictionary_tag = "Fausey et al. 2024"

reference = "Fausey, H. M., Vejlgaard, S., van der Horst, A. J., Heintz, K. E., Izzo, L., Malesani, D. B., et al., MNRAS 536 2839 (2024)"

url = "https://academic.oup.com/mnras/article/536/3/2839/7925868"

description = \
"""
From the damping wing of the GRB 210905A afterglow at z~6.3. Absorption is decoupled into DLAs and IGM.
Two DLAs at z = 6.3186 and z = 6.3118 are included in the fit; reported here are the results for the case in which their
column densities are left uncoupled, which is the statistically preferred model (Table 3 of the paper). The spectral index
is either fixed to beta = 0.40 or 0.60, or left free. All values are 3-sigma (99.7 per cent) upper limits on the neutral
fraction x_HI, reported here as lower limits on the ionized fraction Q_HII = 1 - x_HI.
"""

data_structure         = "grid" #grid or points

extracted = False

ndim = 3

dimensions_descriptors = ['redshift', 'spectral_index', 'IGM_model']

axes = [[6.3], ['0.40', '0.60', 'free'], ['Miralda-Escude 1998', 'McQuinn et al. 2008']]

values = [[[0.85, 0.77], [0.87, 0.88], [0.72, 0.43]]]

err_up = None

err_down = None

upper_lim = False

lower_lim = True

limit_confidence_level = 0.997
