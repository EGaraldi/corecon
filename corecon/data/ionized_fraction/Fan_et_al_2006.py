dictionary_tag = 'Fan et al. 2006'

reference   = "Fan, Strauss, Becker, White, Gunn et al.; AJ 132, 117 (2006)"  

url         = "https://iopscience.iop.org/article/10.1086/504836"

description = \
"""Data: moderate-resolution spectra of a sample of 19 quasars at 5.74 < z_em < 6.42.
IGM properties reconstructed from:
 (1) evolution of the Gunn-Peterson optical depth in the Ly-alpha, Ly-beta, and Ly-gamma
 (2) distribution of lengths of dark absorption gaps
 (3) size of HII regions around luminous quasars."""  

data_structure         = "grid" #grid or points

extracted              = True
        
ndim        = 1

dimensions_descriptors = ["redshift"]

axes        = [5.03, 5.25, 5.45, 5.65, 5.85, 6.10]

values      = [0.999945, 0.999933, 0.999934, 0.999912, 0.99987, 0.99957]

err_up      = [0.0000142, 0.0000207, 0.0000247, 0.0000365, 0.0000408, 0.0003]

err_down    = [0.0000165, 0.0000244, 0.0000301, 0.0000460, 0.0000490, 0.0003]

err_up2     = None

err_down2   = None

upper_lim     = [False, False, False, False, False, False]

lower_lim     = [False, False, False, False, False, False]
