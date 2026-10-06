dictionary_tag = "Greig et al. 2022"

reference = "Greig, B., Mesinger, A., Davies, F. B., Wang, F., Yang, J., Hennawi, J. F., MNRAS 512 5390 (2022)"

url = "https://academic.oup.com/mnras/article/512/4/5390/6554258"

description = \
"""
Constraints from the Lyman-alpha damping wing of four z > 7 QSOs, obtained with a covariance matrix reconstruction of
the intrinsic QSO continuum and fitting to simulations. DESJ0252-0503 (z = 7.00) and J1007+2115 (z = 7.51) are analysed
with this pipeline for the first time, while ULASJ1120+0641 (z = 7.09) and ULASJ1342+0928 (z = 7.54) are a reanalysis
superseding Greig et al. 2017 and Greig et al. 2019, following the inclusion of the N V emission line in the
reconstruction pipeline. All four objects have independent damping-wing analyses elsewhere in this archive (Wang et al.
2020, Yang et al. 2020, Greig et al. 2017, Greig et al. 2019).
The third datapoint is the joint constraint obtained by multiplying the four individual likelihoods, quoted at the mean
redshift of the four QSOs, z = 7.29 +- 0.27 (given as err_left and err_right). It is NOT independent of the other four
datapoints, and the two sets must not be used together: the joint_constraint field flags it, being True on the joint
datapoint and False on the four individual ones.
All uncertainties are 68 per cent confidence intervals on the neutral fraction, converted here to the ionized fraction
Q_HII = 1 - x_HI (which swaps the upper and lower errors).
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes = [7.00, 7.09, 7.29, 7.51, 7.54]

err_left  = [None, None, 0.27, None, None]

err_right = [None, None, 0.27, None, None]

values = [0.36, 0.56, 0.51, 0.73, 0.69]

err_up = [0.23, 0.24, 0.14, 0.17, 0.19]

err_down = [0.19, 0.23, 0.13, 0.21, 0.18]

upper_lim = False

lower_lim = False

#True on the joint constraint obtained by multiplying the four individual likelihoods, False on the individual QSOs.
#Select joint_constraint==False to use the four independent datapoints, or joint_constraint==True to use the single
#joint one; the two sets must not be combined.
joint_constraint = [False, False, True, False, False]

