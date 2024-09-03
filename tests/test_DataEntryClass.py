import corecon as crc
import numpy as np


def test_swap_limits():
    uvlf = crc.get("UVLF")
    h23 = uvlf["Harikane et al. 2023"]
    
    h23.swap_limits()
    assert np.all( h23.lower_lim == [True, True, False, False, False, False, True, True, False, False, False, False, True, False]),\
           "Problem detected in DataEntry.swap_limit"

def test_swap_errors():
    uvlf = crc.get("UVLF")
    b17 = uvlf["Bouwens et al. 2017"]
    
    b17.swap_errors()
    assert np.all(b17.err_down == [0.30103   , 0.15970084, 0.19629465, 0.12493874, 0.09691001, 0.07918125, 0.28546222, 0.03817964, 
                                   0.29459589, 0.34325599, 0.26787824, 0.35483287, 0.09089366, 0.78861996, 1.14378603, 1.58134989, 2.10047281] ), \
           "Problem detected in DataEntry.swap_errors"

def test_nan_to_values_all_fields():
    uvlf = crc.get("UVLF")
    k22 = uvlf["Kauffmann et al. 2022"]
    
    k22.nan_to_values("all", 1e-10)
    assert np.all(k22.err_down == [1.0000000e-10, 3.5139073e-01, 3.4584234e-01, 4.0866387e-01, 5.4104580e-01, 1.0000000e+02]),\
           "Problem detected in DataEntry.nan_to_vals using 'all' as first argument"
    assert np.all(k22.err_up == [1.0000000e-10, 1.9165904e-01, 1.9005692e-01, 2.0676008e-01, 2.3357745e-01, 3.4987856e-01]),\
           "Problem detected in DataEntry.nan_to_vals using 'all' as first argument"

def test_nan_to_values_one_field():
    uvlf = crc.get("UVLF")
    k22 = uvlf["Kauffmann et al. 2022"]
    
    k22.nan_to_values("err_down", 1e-10)
    assert np.all(k22.err_down == [1.0000000e-10, 3.5139073e-01, 3.4584234e-01, 4.0866387e-01, 5.4104580e-01, 1.0000000e+02]),\
           "Problem detected in DataEntry.nan_to_vals using a single field as first argument"

def test_nan_to_values_list_fields():
    uvlf = crc.get("UVLF")
    k22 = uvlf["Kauffmann et al. 2022"]
    
    k22.nan_to_values(["err_down", "err_up"], 1e-10)
    assert np.all(k22.err_down == [1.0000000e-10, 3.5139073e-01, 3.4584234e-01, 4.0866387e-01, 5.4104580e-01, 1.0000000e+02]),\
           "Problem detected in DataEntry.nan_to_vals using a list of fields as first argument"
    assert np.all(k22.err_up == [1.0000000e-10, 1.9165904e-01, 1.9005692e-01, 2.0676008e-01, 2.3357745e-01, 3.4987856e-01]),\
           "Problem detected in DataEntry.nan_to_vals using a list of fields as first argument"

def test_set_lim_errors():
    uvlf = crc.get("UVLF")
    h23 = uvlf["Harikane et al. 2023"]

    h23.set_lim_errors(5, frac_of_values=False)
    assert np.all(h23.err_up == [5.0000000e+00, 5.0000000e+00, 5.2569252e-01, 5.2542593e-01, 3.4821760e-02, 3.9757000e-03, 
                                 5.0000000e+00, 5.0000000e+00, 5.2009033e-01, 3.6845013e-01, 2.9921665e-01, 3.7791135e-01, 
                                 5.0000000e+00, 3.6835150e-01]),\
           "Problem detected in DataEntry.set_lim_errors using frac_of_values=False"

def test_set_lim_errors_frac():
    uvlf = crc.get("UVLF")
    h23 = uvlf["Harikane et al. 2023"]

    h23.set_lim_errors(0.5, frac_of_values=True)
    assert np.all(h23.err_up == [-2.0790076 , -2.05760232,  0.52569252,  0.52542593,  0.03482176, 0.0039757 , -2.616422065, 
                                 -2.596910015,  0.52009033,  0.36845013, 0.29921665,  0.37791135, -2.808092315,  0.3683515 ]),\
           "Problem detected in DataEntry.set_lim_errors using frac_of_values=True"

def test_list_attributes():
    uvlf = crc.get("UVLF")
    h23 = uvlf["Harikane et al. 2023"]

    assert np.all(h23.list_attributes() == ['ndim', 'description','reference','parent_field','url','dimensions_descriptors',
                                            'extracted','axes','values','err_up','err_down','upper_lim','lower_lim','extra_data',
                                            'err_right','err_left','UV_luminosity_function', 'dimensions_descriptors_internal','redshift','M_UV']),\
            "Problem detected in DataEntry.list_attributes"
