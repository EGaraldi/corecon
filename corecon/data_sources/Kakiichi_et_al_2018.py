dictionary_tag                = 'Kakiichi et al. 2018'

reference                     = 'Kakiichi, Ellis, Laporte, Zitrin, Eilers, et al.; MNRAS 479, 43 (2018)'

url                           = 'https://academic.oup.com/mnras/article/479/1/43/4999925'

extracted                     = 'True'

description                   = \
'''
Measurements from a Keck DEIMOS spectroscopic survey centered on a Keck ESI QSO sightline. The constraints come from seven colour-selected LBGs in the range 
5.3 < z < 6.4 and the Ly-a/Ly-b transmission fluctuations in the QSO sightline.
NOTE: We have derived the correlation from the original data (i.e. the transmitted flux) by taking the most-distant point as a measure of the average transmitted 
      flux at that redshift. The original data and errors are stored in the flux, err_up_flux, and err_down_flux arrays.
NOTE: The three points between 3 and 5 pMpc are biased high by the presence of a nearby QSO.
'''

redshift                      = [ 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0 ]
redshift_err_up               = [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25 ]
redshift_err_down             = [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25 ]
redshift_upper_lim            = False
redshift_lower_lim            = False

proper_distance_pMpc          = [ 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0 ]
proper_distance_pMpc_err_up   = [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25 ]
proper_distance_pMpc_err_down = [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25 ]
proper_distance_pMpc_upper_lim= False
proper_distance_pMpc_lower_lim= False

Lya_spike_galaxy_correlation  = [ 2.22076336, 0.71755725, 0.63572519, 0.40458015, 2.52793893, 1.63419847, 3.49435115, -0.21496183, -0.33038168, 0.0 ]
Lya_spike_galaxy_correlation_err_up= [ 2.78149211, 0.75185978, 0.62679114, 0.46659183, 1.96928336, 1.47762254, 3.87712682, -0.17919231, -0.31903575, 0.0 ]
Lya_spike_galaxy_correlation_err_down= [ 2.78149211, 0.75185978, 0.62679114, 0.46659183, 1.96928336, 1.47762254, 3.87712682, -0.17919231, -0.31903575, 0.0 ]
Lya_spike_galaxy_correlation_upper_lim= [ False, False, False, False, False, False, False, False, False, False ]
Lya_spike_galaxy_correlation_lower_lim= [ False, False, False, False, False, False, False, False, False, False ]

flux                          = [ 0.010548, 0.005625, 0.005357, 0.0046, 0.011554, 0.008627, 0.014719, 0.002571, 0.002193, 0.003275 ]
flux_err_up                   = [ 0.006277, 0.002196, 0.00176, 0.002281, 0.001405, 0.002129, 0.006655, 0.000453, 0.000676, 0.002153 ]
flux_err_down                 = [ 0.006277, 0.002196, 0.00176, 0.002281, 0.001405, 0.002129, 0.006655, 0.000453, 0.000676, 0.002153 ]
flux_upper_lim                = [ False, False, False, False, False, False, False, False, False, False ]
flux_lower_lim                = [ False, False, False, False, False, False, False, False, False, False ]

