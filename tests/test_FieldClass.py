import corecon as crc
import numpy as np


def test_get_all_references():
    uvlf = crc.get("UVLF")
    
    #We test that *at least* the following references are returned. In this way, we do not have to update this test every time a 
    # new constraint is added (or a temporary one updated)
    references = ['Ishigaki, Kawamata, Ouchi, Oguri, Shimasaku, Ono; ApJ. 854, 73 (2018)',
                  'McLeod, Donnan, McLure, Dunlop, Magee, Begley, Carnall, et al.; MNRAS 527, 5004 (2024)',
                  'Atek, Richard, Kneib, Schaerer; MNRAS 479, 5184 (2018)',
                  'Oesch, Bouwens, Illingworth, Labbe, Smit, Franx, et al.; ApJ. 786, 108 (2014)',
                  'Morishita, Trenti, Stiavelli, Bradley, Coe, et al.; ApJ. 867, 150 (2018)',
                  'Perez-Gonzalez, Costantin, Langeroodi, Rinaldi, Annunziatella, et al.; ApJL 951, L1 (2023)',
                  'Bouwens, Oesch, Labbe, Illingworth, Fazio, et al.; ApJ. 830, 67 (2016)',
                  'Livermore, Finkelstein, Lotz; ApJ. 835, 113 (2017)',
                  'Harikane, Ouchi, Oguri, Ono, Nakajima, Isobe, Umeda, Mawatari, Zhang; ApJS 265, 5 (2023)',
                  'Atek, Richard, Kneib, Jauzac, Schaerer, Clement, et al.; ApJ 800, 18 (2015)',
                  'Bouwens, Illingworth, Oesch, Naidu, van Leeuwen, Magee, MNRAS 523, 1009 (2023)',
                  'McLeod, McLure, Dunlop; MNRAS 459, 3812 (2016)',
                  'Donnan, McLeod, McLure, Dunlop, Carnall, Cullen, Magee; MNRAS 520, 4554 (2023)',
                  'Finkelstein, Ryan, Papovich, Dickinson, Song, et al.; ApJ. 810, 71 (2015)',
                  'Stefanon, Labbe, Bouwens, Oesch, Ashby, Caputi, et al.; ApJ. 883, 99 (2019)',
                  'Bouwens, Illingworth, Oesch, Trenti, Labbe, et al.; ApJ. 803, 34 (2015)',
                  'Rojas-Ruiz S., Finkelstein S. L., Bagley M. B., Stevans M., Finkelstein K. D.,  et al., 2020, ApJ, 891, 146',
                  'McLure, Dunlop, Bowler, Curtis-Lake, Schenker, et al.; MNRAS 432, 2696 (2013)',
                  'Bouwens, Oesch, Illingworth, Ellis, Stefanon; ApJ. 843, 129 (2017)',
                  'Bowler, Jarvis, Dunlop, McLure, McLeod, et al.; MNRAS 493, 2059 (2020)',
                  'Leung, Bagley, Finkelstein, Ferguson, Koekemoer, Perez-Gonzalez, et al.; ApJL 954, L46 (2023)',
                  'Donnan, McLeod, Dunlop, McLure, Carnall, Begley, Cullen, et al.; MNRAS 518, 6011 (2023)',
                  'Bouwens, Stefanon, Brammer, Oesch, Herard-Demanche, Illingworth, et al., MNRAS 523, 1936 (2023)',
                  'Castellano, Dayal, Pentericci, Fontana, Hutter, et al.; ApJL. 818, L3 (2016)',
                  'Oesch, Bouwens, Illingworth, Labbe, Stefanon; ApJ. 855, 105 (2018)',
                  'Bouwens, Illingworth, Ellis, Oesch, Stefanon; ApJ 940, 55 (2022)',
                  'Bowler, Dunlop, McLure, McCracken, Milvang-Jensen, et al.; MNRAS 452, 1817 (2015)'
                  ]

    uvlf_ref = uvlf.get_all_references()

    assert len(set(references).difference(uvlf_ref))==0, "Problem detected in Field.get_all_references"





def test_get_all_urls():
    uvlf = crc.get("UVLF")
    
    #We test that *at least* the following URLs are returned. In this way, we do not have to update this test every time a 
    # new constraint is added (or a temporary one updated)
    urls = ['https://iopscience.iop.org/article/10.3847/1538-4357/aaa544',
            'https://academic.oup.com/mnras/article/527/3/5004/7408621',
            'https://academic.oup.com/mnras/article/479/4/5184/5050078',
            'https://iopscience.iop.org/article/10.1088/0004-637X/786/2/108',
            'https://iopscience.iop.org/article/10.3847/1538-4357/aae68c',
            'https://iopscience.iop.org/article/10.3847/2041-8213/acd9d0/pdf',
            'https://iopscience.iop.org/article/10.3847/0004-637X/830/2/67',
            'https://iopscience.iop.org/article/10.3847/1538-4357/835/2/113',
            'https://iopscience.iop.org/article/10.3847/1538-4365/acaaa9',
            'https://ui.adsabs.harvard.edu/abs/2015ApJ...800...18A/abstract',
            'https://ui.adsabs.harvard.edu/abs/2023MNRAS.523.1009B/',
            'https://academic.oup.com/mnras/article/459/4/3812/2624050',
            'https://ui.adsabs.harvard.edu/abs/2023MNRAS.520.4554D/abstract',
            'https://iopscience.iop.org/article/10.1088/0004-637X/810/1/71',
            'https://iopscience.iop.org/article/10.3847/1538-4357/ab3792',
            'https://iopscience.iop.org/article/10.1088/0004-637X/803/1/34',
            'https://iopscience.iop.org/article/10.3847/1538-4357/ab7659',
            'https://academic.oup.com/mnras/article/432/4/2696/2907730',
            'https://iopscience.iop.org/article/10.3847/1538-4357/aa70a4',
            'https://academic.oup.com/mnras/article/493/2/2059/5721544',
            'https://iopscience.iop.org/article/10.3847/2041-8213/acf365/pdf',
            'https://academic.oup.com/mnras/article/518/4/6011/6849970',
            'https://ui.adsabs.harvard.edu/abs/2023MNRAS.523.1036B/abstract',
            'https://iopscience.iop.org/article/10.3847/2041-8205/818/1/L3',
            'https://iopscience.iop.org/article/10.3847/1538-4357/aab03f',
            'https://iopscience.iop.org/article/10.3847/1538-4357/ac86d1',
            'https://academic.oup.com/mnras/article/452/2/1817/1068199']

    uvlf_urls = uvlf.get_all_urls()
    
    assert len(set(urls).difference(uvlf_urls))==0, "Problem detected in Field.get_all_urls"





def test_filter_by_redshift_range():
    uvlf = crc.get("UVLF")
    
    #We test that *at least* the following entries are returned. In this way, we do not have to update this test every time a 
    # new constraint is added (or a temporary one updated)
    entries = ['Ishigaki et al. 2018', 'McLeod et al. 2024', 'Oesch et al. 2014',
               'Morishita et al. 2018', 'Perez-Gonzalez et al. 2023',
               'Bouwens et al. 2016', 'Harikane et al. 2023',
               'Bouwens et al. 2023a', 'McLeod et al. 2016',
               'Donnan et al. 2023b', 'Stefanon et al. 2019',
               'Bouwens et al. 2015', 'Rojas-Ruiz et al. 2020',
               'Bowler et al. 2020', 'Leung et al. 2023', 'Donnan et al. 2023a',
               'Bouwens et al. 2023b', 'Oesch et al. 2018', 'Bouwens et al. 2022']

    uvlf_zrange = uvlf.filter_by_redshift_range(9,13)

    assert len(set(entries).difference(uvlf_zrange))==0, "Problem detected in Field.filter_by_redshift_range (not all entries are returned)"
    
    #then test the slicing is correct
    assert np.all(uvlf_zrange['Ishigaki et al. 2018'].redshift == [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]), \
           "Problem detected in Field.filter_by_redshift_range (slicing of constraints is wrong)"





def test_filter_by_extracted():

    uvlf = crc.get("UVLF")
    
    #We test that *at least* the following entries are returned. In this way, we do not have to update this test every time a 
    # new constraint is added (or a temporary one updated)
    entries = ['Ishigaki et al. 2018',  'Atek et al. 2018', 'Atek et al. 2015', 'McLeod et al. 2016',  'Castellano et al. 2015']
    
    uvlf_ex = uvlf.filter_by_extracted(True)

    assert len(set(entries).difference(uvlf_ex))==0, "Problem detected in Field.filter_by_extracted (not all entries are returned)"
    
    for e in entries:
        assert uvlf_ex[e].extracted == True, "Problem detected in Field.filter_by_extracted (returned wrong entry/slice)"




def test_get_upper_limits():
    xHII = crc.get("x_HII")

    #We test that *at least* the following entries are returned. In this way, we do not have to update this test every time a 
    # new constraint is added (or a temporary one updated)
    entries = ['Schenker et al. 2014','Sobacchi & Mesinger 2015', 'Schroeder et al. 2013', 'Mortlock et al. 2011', 'Mesinger et al. 2015', 'Mason et al. 2019', 
            'Tilvi et al. 2014', 'Pentericci et al. 2014', 'Bosman et al. 2022', 'Yang et al. 2020b', 'Robertson et al. 2013', 'Hoag et al. 2019']

    xHII_ul = xHII.get_upper_limits()

    assert len(set(entries).difference(xHII_ul))==0, "Problem detected in Field.get_upper_limits (not all entries are returned)"

    for e in entries:
        assert np.all(xHII_ul[e].upper_lim), "Problem detected in Field.get_upper_limits (returned wrong entry/slice)"




def test_get_lower_limits():
    xHII = crc.get("x_HII")

    #We test that *at least* the following entries are returned. In this way, we do not have to update this test every time a 
    # new constraint is added (or a temporary one updated)
    entries = ['Zhu et al. 2022', 'Ouchi et al. 2010', 'Chornock et al. 2013', 'Totani et al. 2006', 'Nakane et al. 2024',
               'Lu et al. 2020', 'McGreer et al. 2011','McGreer et al. 2015']

    xHII_ll = xHII.get_lower_limits()

    assert len(set(entries).difference(xHII_ll))==0, "Problem detected in Field.get_lower_limits (not all entries are returned)"

    for e in entries:
        assert np.all(xHII_ll[e].lower_lim), "Problem detected in Field.get_lower_limits (returned wrong entry/slice)"

