dictionary_tag         = "Madau & Dickinson 2014"

reference              = "https://www.annualreviews.org/doi/10.1146/annurev-astro-081811-125615"

url                    = "Madau, Dickinson; ARA&A 52, 415 (2014)"

description            = \
"""
Collection of data on the cosmic star formation rate density from different sources. See the individual references
for the methods used to derive them. The original data were re-analysed in an homogeneous way.
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 2

dimensions_descriptors = ["redshift", "original reference"]

axes                   = [[0.055000, 'Wyder et al. (2005)'], [0.300000, 'Schiminovich et al. (2005)'],
                          [0.500000, 'Schiminovich et al. (2005)'], [0.700000, 'Schiminovich et al. (2005)'],
                          [1.000000, 'Schiminovich et al. (2005)'], [0.050000, 'Robotham and Driver (2011)'],
                          [0.125000, 'Cucciati et al. (2012)'], [0.300000, 'Cucciati et al. (2012)'],
                          [0.500000, 'Cucciati et al. (2012)'], [0.700000, 'Cucciati et al. (2012)'],
                          [0.900000, 'Cucciati et al. (2012)'], [1.100000, 'Cucciati et al. (2012)'],
                          [1.450000, 'Cucciati et al. (2012)'], [2.100000, 'Cucciati et al. (2012)'],
                          [3.000000, 'Cucciati et al. (2012)'], [4.000000, 'Cucciati et al. (2012)'],
                          [1.125000, 'Dahlen et al. (2007)'], [1.750000, 'Dahlen et al. (2007)'],
                          [2.225000, 'Dahlen et al. (2007)'], [2.300000, 'Reddy and Steidel (2009)'],
                          [3.050000, 'Reddy and Steidel (2009)'], [3.800000, 'Bouwens et al. (2012a),(2012b)'],
                          [4.900000, 'Bouwens et al. (2012a),(2012b)'], [5.900000, 'Bouwens et al. (2012a),(2012b)'],
                          [7.000000, 'Bouwens et al. (2012a),(2012b)'], [7.900000, 'Bouwens et al. (2012a),(2012b)'],
                          [7.000000, 'Schenker et al. (2013)'], [8.000000, 'Schenker et al. (2013)'],
                          [0.030000, 'Sanders et al. (2003)'], [0.030000, 'Takeuchi et al. (2003)'],
                          [0.550000, 'Magnelli et al. (2011)'], [0.850000, 'Magnelli et al. (2011)'],
                          [1.150000, 'Magnelli et al. (2011)'], [1.550000, 'Magnelli et al. (2011)'],
                          [2.050000, 'Magnelli et al. (2011)'], [0.550000, 'Magnelli et al. (2013)'],
                          [0.850000, 'Magnelli et al. (2013)'], [1.150000, 'Magnelli et al. (2013)'],
                          [1.550000, 'Magnelli et al. (2013)'], [2.050000, 'Magnelli et al. (2013)'],
                          [0.150000, 'Gruppioni et al. (2013)'], [0.375000, 'Gruppioni et al. (2013)'],
                          [0.525000, 'Gruppioni et al. (2013)'], [0.700000, 'Gruppioni et al. (2013)'],
                          [0.900000, 'Gruppioni et al. (2013)'], [1.100000, 'Gruppioni et al. (2013)'],
                          [1.450000, 'Gruppioni et al. (2013)'], [1.850000, 'Gruppioni et al. (2013)'],
                          [2.250000, 'Gruppioni et al. (2013)'], [2.750000, 'Gruppioni et al. (2013)'],
                          [3.600000, 'Gruppioni et al. (2013)']
                         ]

values                 = [-1.82, -1.5 , -1.39, -1.2 , -1.25, -1.77, -1.75, -1.55, -1.44,
                          -1.24, -0.99, -0.94, -0.95, -0.75, -1.04, -1.69, -1.02, -0.75,
                          -0.87, -0.75, -0.97, -1.29, -1.42, -1.65, -1.79, -2.09, -2.  ,
                          -2.21, -1.72, -1.95, -1.34, -0.96, -0.89, -0.91, -0.89, -1.22,
                          -1.1 , -0.96, -0.94, -0.8 , -1.64, -1.42, -1.32, -1.14, -0.94,
                          -0.81, -0.84, -0.86, -0.91, -0.86, -1.36]

err_up                 = [0.09, 0.05, 0.15, 0.31, 0.31, 0.08, 0.18, 0.12, 0.1 , 0.1 , 0.09,
                          0.09, 0.15, 0.49, 0.26, 0.22, 0.08, 0.12, 0.09, 0.09, 0.11, 0.05,
                          0.06, 0.08, 0.1 , 0.11, 0.1 , 0.14, 0.02, 0.2 , 0.22, 0.15, 0.27,
                          0.17, 0.21, 0.08, 0.1 , 0.13, 0.13, 0.18, 0.09, 0.03, 0.05, 0.06,
                          0.05, 0.04, 0.04, 0.02, 0.09, 0.15, 0.23]

err_down               = [0.02, 0.05, 0.08, 0.13, 0.13, 0.09, 0.18, 0.12, 0.1 , 0.1 , 0.08,
                          0.09, 0.08, 0.09, 0.15, 0.32, 0.08, 0.12, 0.09, 0.11, 0.15, 0.05,
                          0.06, 0.08, 0.1 , 0.11, 0.11, 0.14, 0.03, 0.2 , 0.11, 0.19, 0.21,
                          0.21, 0.25, 0.11, 0.13, 0.2 , 0.18, 0.15, 0.11, 0.04, 0.05, 0.06,
                          0.06, 0.05, 0.04, 0.03, 0.12, 0.23, 0.5 ]

err_up2                = None

err_down2              = None

upper_lim              = False

lower_lim              = False
