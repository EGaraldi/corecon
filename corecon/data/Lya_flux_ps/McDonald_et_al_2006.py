dictionary_tag = "McDonald et al. 2006"

reference   = "McDonald, Seljak, Burles, Schlegel, Weinberg, Cen, Shih, et al.; ApJS 163, 80 (2006)"

url         = "https://iopscience.iop.org/article/10.1086/444361"

description = \
"""
3035 high-redshift quasar spectra from the Sloan Digital Sky Survey.
"""

data_structure         = "grid" #grid or points

extracted              = False 

ndim                   = 2

dimensions_descriptors = ["redshift", "ks (s/km)"]

axes        = [[2.2, 2.4, 2.6, 2.8, 3.0 ,3.2, 3.4, 3.6, 3.8, 4.0, 4.2], \
               [1.410e-03, 1.780e-03, 2.240e-03, 2.820e-03, 3.550e-03, 4.470e-03, \
                5.620e-03, 7.080e-03, 8.910e-03, 1.122e-02, 1.413e-02, 1.778e-02]
              ]

values      = [[1.742e+01, 1.692e+01, 1.839e+01, 1.832e+01, 1.534e+01, 1.236e+01,
                1.376e+01, 1.092e+01, 9.300e+00, 8.070e+00, 7.040e+00, 4.770e+00],
               [2.085e+01, 2.294e+01, 2.287e+01, 2.163e+01, 1.817e+01, 1.540e+01,
                1.776e+01, 1.300e+01, 1.250e+01, 1.042e+01, 8.240e+00, 6.180e+00],
               [2.755e+01, 2.829e+01, 3.132e+01, 2.679e+01, 2.453e+01, 2.029e+01,
                2.217e+01, 1.702e+01, 1.534e+01, 1.329e+01, 1.036e+01, 8.590e+00],
               [3.650e+01, 3.675e+01, 3.796e+01, 3.640e+01, 2.958e+01, 2.529e+01,
                2.545e+01, 2.239e+01, 2.009e+01, 1.596e+01, 1.320e+01, 9.820e+00],
               [4.564e+01, 4.183e+01, 4.688e+01, 4.153e+01, 3.646e+01, 2.912e+01,
                2.986e+01, 2.419e+01, 2.252e+01, 1.887e+01, 1.452e+01, 1.150e+01],
               [5.412e+01, 4.910e+01, 5.219e+01, 4.785e+01, 4.352e+01, 3.481e+01,
                3.436e+01, 3.108e+01, 2.703e+01, 2.239e+01, 1.864e+01, 1.546e+01],
               [5.604e+01, 7.513e+01, 5.628e+01, 5.788e+01, 5.214e+01, 4.317e+01,
                4.153e+01, 3.737e+01, 3.272e+01, 2.880e+01, 2.264e+01, 1.843e+01],
               [7.924e+01, 8.473e+01, 7.461e+01, 6.577e+01, 6.599e+01, 5.547e+01,
                4.946e+01, 4.387e+01, 4.046e+01, 3.241e+01, 2.626e+01, 2.202e+01],
               [1.1873e+02, 6.1450e+01, 7.7110e+01, 7.1590e+01, 7.7330e+01, 5.9070e+01, 
                5.7600e+01, 5.6500e+01, 4.2820e+01, 3.7420e+01, 3.0080e+01, 2.8450e+01],
               [1.2391e+02, 1.2349e+02, 9.6540e+01, 8.3870e+01, 7.1950e+01, 6.6400e+01, 
                6.8630e+01, 6.0240e+01, 5.2320e+01, 4.6190e+01, 3.1830e+01, 3.6440e+01],
               [1.6733e+02, 1.3155e+02, 1.2269e+02, 1.3466e+02, 1.1373e+02, 8.4390e+01, 
                6.8020e+01, 7.7300e+01, 6.2490e+01, 5.2110e+01, 5.0560e+01, 3.7860e+01],
              ]

err_up      = [[1.680e+00, 1.300e+00, 1.170e+00, 9.900e-01, 7.200e-01, 5.800e-01,
                5.200e-01, 4.400e-01, 3.800e-01, 3.800e-01, 3.400e-01, 3.500e-01],
               [1.850e+00, 2.030e+00, 1.350e+00, 1.210e+00, 8.700e-01, 6.400e-01,
                6.700e-01, 5.000e-01, 4.100e-01, 4.100e-01, 3.600e-01, 3.400e-01],
               [2.490e+00, 1.810e+00, 1.710e+00, 1.360e+00, 1.070e+00, 8.400e-01,
                7.100e-01, 6.000e-01, 5.000e-01, 4.800e-01, 4.200e-01, 3.800e-01],
               [2.700e+00, 2.160e+00, 1.760e+00, 1.450e+00, 1.210e+00, 9.100e-01,
                8.200e-01, 6.700e-01, 6.200e-01, 4.800e-01, 4.300e-01, 3.700e-01],
               [3.670e+00, 2.830e+00, 2.640e+00, 2.160e+00, 1.700e+00, 1.190e+00,
                1.060e+00, 8.000e-01, 7.500e-01, 6.700e-01, 5.300e-01, 4.800e-01],
               [4.920e+00, 4.090e+00, 3.250e+00, 2.550e+00, 2.300e+00, 1.530e+00,
                1.410e+00, 1.190e+00, 9.500e-01, 8.400e-01, 7.200e-01, 6.700e-01],
               [5.810e+00, 5.300e+00, 3.910e+00, 3.370e+00, 2.830e+00, 2.200e+00,
                1.730e+00, 1.430e+00, 1.200e+00, 1.170e+00, 8.900e-01, 8.000e-01],
               [8.310e+00, 8.250e+00, 5.850e+00, 4.970e+00, 4.150e+00, 3.380e+00,
                2.750e+00, 2.170e+00, 1.950e+00, 1.650e+00, 1.330e+00, 1.260e+00],
               [1.5490e+01, 9.8000e+00, 7.1000e+00, 7.4100e+00, 5.7300e+00, 4.5800e+00, 
                3.9100e+00, 3.7000e+00, 2.3800e+00, 2.3200e+00, 2.3200e+00, 1.9200e+00],
               [2.1090e+01, 1.8390e+01, 1.2210e+01, 9.9000e+00, 8.3500e+00, 5.8600e+00, 
                5.7800e+00, 4.9100e+00, 3.9800e+00, 3.6600e+00, 3.4600e+00, 3.7600e+00],
               [4.2600e+01, 2.1880e+01, 1.8370e+01, 1.7840e+01, 1.3620e+01, 9.7700e+00, 
                7.2200e+00, 8.0800e+00, 6.1300e+00, 4.7800e+00, 4.8300e+00, 4.4500e+00],
              ]

err_down    = [[1.680e+00, 1.300e+00, 1.170e+00, 9.900e-01, 7.200e-01, 5.800e-01,
                5.200e-01, 4.400e-01, 3.800e-01, 3.800e-01, 3.400e-01, 3.500e-01],
               [1.850e+00, 2.030e+00, 1.350e+00, 1.210e+00, 8.700e-01, 6.400e-01,
                6.700e-01, 5.000e-01, 4.100e-01, 4.100e-01, 3.600e-01, 3.400e-01],
               [2.490e+00, 1.810e+00, 1.710e+00, 1.360e+00, 1.070e+00, 8.400e-01,
                7.100e-01, 6.000e-01, 5.000e-01, 4.800e-01, 4.200e-01, 3.800e-01],
               [2.700e+00, 2.160e+00, 1.760e+00, 1.450e+00, 1.210e+00, 9.100e-01,
                8.200e-01, 6.700e-01, 6.200e-01, 4.800e-01, 4.300e-01, 3.700e-01],
               [3.670e+00, 2.830e+00, 2.640e+00, 2.160e+00, 1.700e+00, 1.190e+00,
                1.060e+00, 8.000e-01, 7.500e-01, 6.700e-01, 5.300e-01, 4.800e-01],
               [4.920e+00, 4.090e+00, 3.250e+00, 2.550e+00, 2.300e+00, 1.530e+00,
                1.410e+00, 1.190e+00, 9.500e-01, 8.400e-01, 7.200e-01, 6.700e-01],
               [5.810e+00, 5.300e+00, 3.910e+00, 3.370e+00, 2.830e+00, 2.200e+00,
                1.730e+00, 1.430e+00, 1.200e+00, 1.170e+00, 8.900e-01, 8.000e-01],
               [8.310e+00, 8.250e+00, 5.850e+00, 4.970e+00, 4.150e+00, 3.380e+00,
                2.750e+00, 2.170e+00, 1.950e+00, 1.650e+00, 1.330e+00, 1.260e+00],
               [1.5490e+01, 9.8000e+00, 7.1000e+00, 7.4100e+00, 5.7300e+00, 4.5800e+00, 
                3.9100e+00, 3.7000e+00, 2.3800e+00, 2.3200e+00, 2.3200e+00, 1.9200e+00],
               [2.1090e+01, 1.8390e+01, 1.2210e+01, 9.9000e+00, 8.3500e+00, 5.8600e+00, 
                5.7800e+00, 4.9100e+00, 3.9800e+00, 3.6600e+00, 3.4600e+00, 3.7600e+00],
               [4.2600e+01, 2.1880e+01, 1.8370e+01, 1.7840e+01, 1.3620e+01, 9.7700e+00, 
                7.2200e+00, 8.0800e+00, 6.1300e+00, 4.7800e+00, 4.8300e+00, 4.4500e+00],
              ]

err_up2     = None

err_down2   = None

upper_lim   = [[False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False]
              ]

lower_lim   = [[False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False],
               [False, False, False, False, False, False, \
                False, False, False, False, False, False]
              ]
