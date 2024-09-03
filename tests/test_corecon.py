import corecon as crc
import numpy as np

def test_get_fields():
    
    #We test that *at least* the following fields are returned. In this way, we do not have to update this test every time a 
    # new constraint field is added
    fields = ['HII_fraction', 'HeIII_fraction', 'Lya_flux_power_spectrum', 'mean_free_path', 'effective_optical_depth_HI_Lya',
              'effective_optical_depth_HeII_Lya', 'HeII_to_HI_column_density_ratio', 'quasar_luminosity_function',
              'UV_luminosity_function','IGM_temperature_mean_density','optical_depth_CMB','sfrd',
              'Lya_spike_galaxy_correlation','mass_stellar_metallicity_relation','mass_gas_metallicity_relation',
              'galaxy_main_sequence','UV_slope','ionizing_photons_production_efficiency','HI_photoionization_rate',
              'ionizing_photons_emission_rate','reionization_midpoint','UV_luminosity_density']


    crc_fields = crc.get_fields()
    
    assert len(set(fields).difference(crc_fields))==0, "Problem detected in CoReCon.get_fields"
    


def test_get_field_synonyms():
    #We test that *at least* the following synonyms are returned. In this way, we do not have to update this test every time a 
    # new one is added
    synonyms = ['ionized_fraction', 'x_HII', 'f_HII', 'x_ion', 'f_ion', 'ion_frac']

    crc_syn = crc.get_field_synonyms("HII_fraction")
    
    assert len(set(synonyms).difference(crc_syn))==0, "Problem detected in CoReCon.get_field_synonym"

