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

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [0.055, 0.3  , 0.5  , 0.7  , 1.   , 0.05 , 0.125, 0.3  , 0.5  ,
                          0.7  , 0.9  , 1.1  , 1.45 , 2.1  , 3.   , 4.   , 1.125, 1.75 ,
                          2.225, 2.3  , 3.05 , 3.8  , 4.9  , 5.9  , 7.   , 7.9  , 7.   ,
                          8.   , 0.03 , 0.03 , 0.55 , 0.85 , 1.15 , 1.55 , 2.05 , 0.55 ,
                          0.85 , 1.15 , 1.55 , 2.05 , 0.15 , 0.375, 0.525, 0.7  , 0.9  ,
                          1.1  , 1.45 , 1.85 , 2.25 , 2.75 , 3.6  ]

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

upper_lim              = False

lower_lim              = False

original_reference     = ['Wyder et al. (2005)', 'Schiminovich et al. (2005)',
                          'Schiminovich et al. (2005)', 'Schiminovich et al. (2005)',
                          'Schiminovich et al. (2005)', 'Robotham and Driver (2011)',
                          'Cucciati et al. (2012)', 'Cucciati et al. (2012)',
                          'Cucciati et al. (2012)', 'Cucciati et al. (2012)',
                          'Cucciati et al. (2012)', 'Cucciati et al. (2012)',
                          'Cucciati et al. (2012)', 'Cucciati et al. (2012)',
                          'Cucciati et al. (2012)', 'Cucciati et al. (2012)',
                          'Dahlen et al. (2007)', 'Dahlen et al. (2007)',
                          'Dahlen et al. (2007)', 'Reddy and Steidel (2009)',
                          'Reddy and Steidel (2009)', 'Bouwens et al. (2012a),(2012b)',
                          'Bouwens et al. (2012a),(2012b)', 'Bouwens et al. (2012a),(2012b)',
                          'Bouwens et al. (2012a),(2012b)', 'Bouwens et al. (2012a),(2012b)',
                          'Schenker et al. (2013)', 'Schenker et al. (2013)',
                          'Sanders et al. (2003)', 'Takeuchi et al. (2003)',
                          'Magnelli et al. (2011)', 'Magnelli et al. (2011)',
                          'Magnelli et al. (2011)', 'Magnelli et al. (2011)',
                          'Magnelli et al. (2011)', 'Magnelli et al. (2013)',
                          'Magnelli et al. (2013)', 'Magnelli et al. (2013)',
                          'Magnelli et al. (2013)', 'Magnelli et al. (2013)',
                          'Gruppioni et al. (2013)', 'Gruppioni et al. (2013)',
                          'Gruppioni et al. (2013)', 'Gruppioni et al. (2013)',
                          'Gruppioni et al. (2013)', 'Gruppioni et al. (2013)',
                          'Gruppioni et al. (2013)', 'Gruppioni et al. (2013)',
                          'Gruppioni et al. (2013)', 'Gruppioni et al. (2013)',
                          'Gruppioni et al. (2013)']
