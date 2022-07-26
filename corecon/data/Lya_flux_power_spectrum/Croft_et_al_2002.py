dictionary_tag = "Croft et al. 2002"

reference   = "Croft, Weinberg, Bolte, Burles, Hernquist, Katz, Kirkman, Tytler; ApJ 581, 20 (2002)"

url         = "https://iopscience.iop.org/article/10.1086/344099"

description = \
"""
30 Keck HIRES spectra and 23 Keck LRIS spectra. 
"""

data_structure         = "grid" #grid or points

extracted              = False 

ndim                   = 2

dimensions_descriptors = ["redshift", "ks (s/km)"]

axes                   = [[2.13, 2.47, 2.74, 3.03, 3.51], \
                          [1.99e-03, 2.59e-03, 3.37e-03, 4.37e-03, 5.68e-03, 7.38e-03, \
                           9.58e-03, 1.24e-02, 1.62e-02, 2.10e-02, 2.72e-02, 3.55e-02, \
                           4.61e-02, 5.98e-02, 7.77e-02, 1.01e-01, 1.31e-01, 1.70e-01, \
                           2.21e-01, 2.87e-01]
                         ]

values      = [[1.59e+01, 1.86e+01, 1.75e+01, 9.19e+00, 1.49e+01, 1.29e+01, \
                1.10e+01, 8.15e+00, 6.37e+00, 5.71e+00, 3.40e+00, 2.18e+00, \
                1.25e+00, 6.42e-01, 3.70e-01, 1.73e-01, 1.07e-01, 7.05e-02, \
                5.93e-02, 4.69e-02],
               [4.21e+01, 3.19e+01, 2.75e+01, 2.53e+01, 2.45e+01, 2.04e+01, \
                1.70e+01, 1.34e+01, 1.04e+01, 6.65e+00, 5.09e+00, 3.34e+00, \
                1.69e+00, 9.04e-01, 4.46e-01, 2.12e-01, 1.05e-01, 6.42e-02, \
                4.73e-02, 3.82e-02],
               [4.23e+01, 3.88e+01, 3.39e+01, 2.21e+01, 2.44e+01, 2.08e+01, \
                1.76e+01, 1.40e+01, 1.17e+01, 8.51e+00, 5.96e+00, 3.78e+00, \
                2.38e+00, 1.13e+00, 5.41e-01, 2.15e-01, 9.38e-02, 5.74e-02, \
                4.09e-02, 2.90e-02],
               [4.66e+01, 3.75e+01, 2.67e+01, 2.82e+01, 3.07e+01, 1.98e+01, \
                2.60e+01, 1.63e+01, 1.36e+01, 1.08e+01, 9.02e+00, 5.44e+00, \
                2.83e+00, 1.75e+00, 7.58e-01, 3.38e-01, 1.66e-01, 1.14e-01, \
                9.86e-02, 6.28e-02],
               [5.01e+01, 7.08e+01, 4.34e+01, 5.72e+01, 5.24e+01, 4.02e+01, \
                3.11e+01, 2.56e+01, 2.39e+01, 1.57e+01, 1.23e+01, 8.37e+00, \
                5.47e+00, 3.16e+00, 1.42e+00, 6.37e-01, 3.28e-01, 2.01e-01, \
                1.42e-01, 9.83e-02]
              ]

err_up      = [[7.50e+00, 5.30e+00, 6.00e+00, 4.30e+00, 4.00e+00, 3.20e+00, \
                1.50e+00, 1.32e+00, 1.42e+00, 6.30e-01, 5.20e-01, 2.20e-01, \
                2.50e-01, 1.53e-01, 1.10e-01, 6.60e-02, 4.30e-02, 3.76e-02, \
                3.40e-02, 2.30e-02],
               [7.30e+00, 4.00e+00, 2.90e+00, 2.90e+00, 2.80e+00, 2.60e+00, \
                2.50e+00, 1.00e+00, 8.00e-01, 5.20e-01, 3.50e-01, 2.10e-01, \
                1.20e-01, 5.90e-02, 4.00e-02, 2.50e-02, 1.30e-02, 1.24e-02, \
                1.11e-02, 9.90e-03],
               [6.80e+00, 4.80e+00, 4.30e+00, 2.70e+00, 2.20e+00, 3.10e+00, \
                1.70e+00, 1.00e+00, 1.30e+00, 6.20e-01, 4.30e-01, 2.70e-01, \
                1.80e-01, 7.60e-02, 4.55e-02, 2.11e-02, 1.43e-02, 1.19e-02, \
                1.12e-02, 9.80e-03],
               [1.50e+01, 9.10e+00, 5.10e+00, 4.80e+00, 4.50e+00, 3.70e+00, \
                5.10e+00, 2.20e+00, 1.10e+00, 1.10e+00, 7.10e-01, 5.40e-01, \
                3.50e-01, 1.40e-01, 1.31e-01, 9.70e-02, 8.10e-02, 7.70e-02, \
                8.26e-02, 5.17e-02],
               [1.03e+01, 1.39e+01, 9.80e+00, 1.38e+01, 1.02e+01, 4.00e+00, \
                5.50e+00, 3.30e+00, 4.00e+00, 1.50e+00, 1.00e+00, 6.30e-01, \
                4.80e-01, 2.90e-01, 1.60e-01, 1.35e-01, 1.57e-01, 1.41e-01, \
                1.14e-01, 8.44e-02]
              ]

err_down    = [[7.50e+00, 5.30e+00, 6.00e+00, 4.30e+00, 4.00e+00, 3.20e+00, \
                1.50e+00, 1.32e+00, 1.42e+00, 6.30e-01, 5.20e-01, 2.20e-01, \
                2.50e-01, 1.53e-01, 1.10e-01, 6.60e-02, 4.30e-02, 3.76e-02, \
                3.40e-02, 2.30e-02],
               [7.30e+00, 4.00e+00, 2.90e+00, 2.90e+00, 2.80e+00, 2.60e+00, \
                2.50e+00, 1.00e+00, 8.00e-01, 5.20e-01, 3.50e-01, 2.10e-01, \
                1.20e-01, 5.90e-02, 4.00e-02, 2.50e-02, 1.30e-02, 1.24e-02, \
                1.11e-02, 9.90e-03],
               [6.80e+00, 4.80e+00, 4.30e+00, 2.70e+00, 2.20e+00, 3.10e+00, \
                1.70e+00, 1.00e+00, 1.30e+00, 6.20e-01, 4.30e-01, 2.70e-01, \
                1.80e-01, 7.60e-02, 4.55e-02, 2.11e-02, 1.43e-02, 1.19e-02, \
                1.12e-02, 9.80e-03],
               [1.50e+01, 9.10e+00, 5.10e+00, 4.80e+00, 4.50e+00, 3.70e+00, \
                5.10e+00, 2.20e+00, 1.10e+00, 1.10e+00, 7.10e-01, 5.40e-01, \
                3.50e-01, 1.40e-01, 1.31e-01, 9.70e-02, 8.10e-02, 7.70e-02, \
                8.26e-02, 5.17e-02],
               [1.03e+01, 1.39e+01, 9.80e+00, 1.38e+01, 1.02e+01, 4.00e+00, \
                5.50e+00, 3.30e+00, 4.00e+00, 1.50e+00, 1.00e+00, 6.30e-01, \
                4.80e-01, 2.90e-01, 1.60e-01, 1.35e-01, 1.57e-01, 1.41e-01, \
                1.14e-01, 8.44e-02]
              ]

err_up2     = None
           #    [[False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False],
           #    [False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False],
           #    [False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False],
           #    [False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False],
           #    [False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False, False, False, False, False, \
           #     False, False]
           #   ]

err_down2   = None
              #[[False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False],
              # [False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False],
              # [False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False],
              # [False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False],
              # [False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False, False, False, False, False, \
              #  False, False]
              #]

upper_lim     = [[False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False]
              ]

lower_lim     = [[False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False, False, False, False, False, \
                False, False]
              ]
