dictionary_tag = "Umeda et al. 2025"

reference = "Umeda, H., Ouchi, M., Kikuta, S., Harikane, Y., Ono, Y., Shibuya, T., et al., \\textit{ApJS}, \\textbf{277}, 37 (2025)"

url = "https://iopscience.iop.org/article/10.3847/1538-4365/adb1c0"

description = "Constraints derived from luminosity functions (LFs) and angular correlation functions (ACFs) of 18,960 Lyman-alpha emitters (LAEs) at z = 5.7--7.3. Observations were conducted using Subaru/HSC narrowband data from the HSC-SSP and CHORUS surveys over ~24 deg^2. The analysis utilizes 21CMFAST simulations."

data_structure         = "grid" #grid or points

extracted = False

ndim = 2

dimensions_descriptors = ['redshift', 'method']

axes = [[5.7, 6.6, 7.0, 7.3], ["LF", "ACF"]]

values = [[0.05, 0.06], [0.15, 0.21], [0.18, None], [0.75, None]]

err_up = [[0.0, 0.12], [0.10, 0.19], [0.14, None], [0.09, None]]

err_down = [[0.0, 0.03], [0.08, 0.14], [0.12, None], [0.13, None]]

upper_lim = [[True, False], [False, False], [False, False], [False, False]]

lower_lim = [[False, False], [False, False], [False, False], [False, False]]
    