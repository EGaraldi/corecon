dictionary_tag = "Wold et al. 2022"

reference = "Wold, I. G. B., Malhotra, S., Rhoads, J., Wang, J., Hu, W., Perez, L. A., et al., ApJ, 927, 36 (2022)"

url = "https://iopscience.iop.org/article/10.3847/1538-4357/ac4997"

description = "Constraints from the $Ly\\alpha$ luminosity function at redshift $z = 6.9$ derived from four LAGER survey fields (WIDE12, GAMA15A, COSMOS, CDFS), covering a survey volume of $6.1 \\times 10^6$ Mpc$^3$ and a total of 174 LAE candidates. NOTE: values represent a range, not uncertainties."


data_structure         = "grid" #grid or points

extracted = False

ndim = 2

dimensions_descriptors = ['redshift', "IGM_model"]

axes = [[6.9], ["Malhotra & Rhoads (2006)", "Dijkstra et al. (2007) + Furlanetto et al. (2006)", "McQuinn et al. (2007)"]]

observational_constraints = [["T_IGM + Ly-alpha number density", "T_IGM", "cumulative Ly-alpha LF"]]

values         = [[0.98, 0.92, 0.835]]

err_up         = [[0.02, 0.08, 0.165]]

err_down       = [[0.02, 0.08, 0.165]]

upper_lim = False

lower_lim = False