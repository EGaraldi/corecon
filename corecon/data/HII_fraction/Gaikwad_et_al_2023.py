dictionary_tag = 'Gaikwad et al. 2023'

reference   = "Gaikwad, Haehnelt, Davies, Bosman, Molaro, Kulkarni, et al., subm."

url         = "https://ui.adsabs.harvard.edu/abs/2023arXiv230402038G/abstract"

description = \
"""From 67 quasars at 4.85 < z < 6.05. The properties are measured from the distribution 
of effective optical depths, modeled post-processing the Sherwood simulations with the Ex-CITE code."""

data_structure         = "points" #grid or points

extracted              = True
        
ndim        = 1

dimensions_descriptors = ["redshift"]

axes        = [4.9, 5. , 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6. ]

err_left    = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

err_right   = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

values      = [0.99997466, 0.99997733, 0.99997332, 0.99997242, 0.99949   ,
               0.996467  , 0.992754  , 0.9837    , 0.94404   , 0.90636   ,
               0.8718    , 0.8256    ]

err_up      = [5.8500e-06, 8.4000e-06, 1.3430e-05, 8.1100e-06, 8.0440e-04,
               1.5084e-02, 2.7311e-02, 2.5440e-02, 7.1410e-02, 6.1820e-02,
               1.2600e-01, 9.2500e-02]

err_down    = [4.440e-06, 4.490e-06, 5.530e-06, 5.550e-06, 4.036e-04, 2.457e-03,
               3.506e-03, 8.340e-03, 3.362e-02, 6.391e-02, 7.360e-02, 1.089e-01]

upper_lim     = False

lower_lim     = False
