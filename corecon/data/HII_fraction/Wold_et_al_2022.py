dictionary_tag = "Wold et al. 2022"

reference = "Wold, I. G. B., Malhotra, S., Rhoads, J., Wang, J., Hu, W., Perez, L. A., et al., ApJ, 927, 36 (2022)"

url = "https://iopscience.iop.org/article/10.3847/1538-4357/ac4997"

description = \
"""Constraints from the $Ly\\alpha$ luminosity function at redshift $z = 6.9$ derived from four LAGER survey fields (WIDE12, GAMA15A, COSMOS, CDFS), covering a survey volume of $6.1 \\times 10^6$ Mpc$^3$ and a total of 174 LAE candidates.
The paper derives upper limits on the neutral fraction by comparing the observed evolution of the Lyman-alpha luminosity
density with three sets of reionization models: x_HI < 0.04 from Malhotra & Rhoads (2006), x_HI < 0.16 from the
analytical models of Dijkstra et al. (2007) and Furlanetto et al. (2006), and x_HI < 0.16, 0.33 and 0.11 from models I,
II and III of McQuinn et al. (2007). Reported here is the most conservative of the McQuinn et al. models (model II),
which is also the limit quoted in the abstract, x_HI < 0.33 at 1 sigma.
These are converted to lower limits on the ionized fraction, Q_HII = 1 - x_HI > 0.96, 0.84 and 0.67 respectively.
"""


data_structure         = "grid" #grid or points

extracted = False

ndim = 2

dimensions_descriptors = ['redshift', "IGM_model"]

axes = [[6.9], ["Malhotra & Rhoads (2006)", "Dijkstra et al. (2007) + Furlanetto et al. (2006)", "McQuinn et al. (2007)"]]

observational_constraints = [["T_IGM + Ly-alpha number density", "T_IGM", "cumulative Ly-alpha LF"]]

values         = [[0.96, 0.84, 0.67]]

err_up         = None

err_down       = None

upper_lim = False

lower_lim = True

confidence_level = 0.68
