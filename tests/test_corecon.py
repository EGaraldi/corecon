import corecon as crc
import numpy as np
import os
import tempfile
import yaml

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



def test_get_constraint_set_from_yaml():
    yaml_content = {
        "HII_fraction": ["Fan et al. 2006", "Tilvi et al. 2014"],
        "HeIII_fraction": ["Makan et al. 2022", "Worseck et al. 2019"]
    }

    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.yaml') as temp_yaml:
        yaml.dump(yaml_content, temp_yaml)
        temp_yaml_path = temp_yaml.name

    try:
        result = crc.get_constraint_set_from_yaml(temp_yaml_path)

        # Add assertions based on the expected output of get_dataentry
        assert "HII_fraction" in result
        assert "HeIII_fraction" in result
        
        assert "Fan et al. 2006" in result["HII_fraction"]
        assert "Tilvi et al. 2014" in result["HII_fraction"]
    finally:
        os.remove(temp_yaml_path)



def test_get_constraint_set_from_dict():
    constraints_dict = {
        "HII_fraction": ["Fan et al. 2006", "Tilvi et al. 2014"],
        "HeIII_fraction": ["Makan et al. 2022", "Worseck et al. 2019"]
    }

    result = crc.get_constraint_set_from_dict(constraints_dict)

    # Add assertions based on the expected output of get_dataentry
    assert "HII_fraction" in result
    assert "HeIII_fraction" in result

    assert "Fan et al. 2006" in result["HII_fraction"]
    assert "Tilvi et al. 2014" in result["HII_fraction"]
    assert "Makan et al. 2022" in result["HeIII_fraction"]
    assert "Worseck et al. 2019" in result["HeIII_fraction"]

