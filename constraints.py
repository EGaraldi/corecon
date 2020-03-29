import numpy
from math import pi as PI
from scipy.interpolate import interp1d



########################
# Flux Power Spectrum  #
########################
Fdata = numpy.genfromtxt('dat/FluxPS.dat')
FluxPS = {}
FluxPS['Croft et al. 2002'] = {
    2.13: Fdata[ 0: 20].T,
    2.47: Fdata[20: 40].T,
    2.74: Fdata[40: 60].T,
    3.03: Fdata[60: 80].T,
    3.51: Fdata[80:100].T
}
FluxPS['McDonald et al. 2006'] = {
    2.2: Fdata[100:112].T,
    2.4: Fdata[112:124].T,
    2.6: Fdata[124:136].T,
    2.8: Fdata[136:148].T,
    3.0: Fdata[148:160].T,
    3.2: Fdata[160:172].T,
    3.4: Fdata[172:184].T,
    3.6: Fdata[184:196].T,
    3.8: Fdata[196:208].T,
    4.0: Fdata[208:220].T,
    4.2: Fdata[220:232].T
}
FluxPS["D'Aloisio et al. 2016"] = {
    5.2: Fdata[232:244].T,
    5.4: Fdata[244:256].T,
    5.6: Fdata[256:268].T
}
FluxPS['Palanque-Delabrouille et al. 2013'] = {
    4.4: Fdata[268:286].T,
    4.0: Fdata[286:318].T,
    3.6: Fdata[318:350].T
}



###############################
# Temperature at mean density #
###############################
# [z,T,dT+,dT-]
Tdata = numpy.genfromtxt('dat/T0.dat')
T0={}
T0['Becker et al. 2011']   = Tdata[ 0: 8]
T0['Boera et al. 2014']    = Tdata[ 8:15]
T0['Bolton et al. 2014']   = Tdata[15,None]
T0['Garzilli et al. 2012'] = Tdata[16:19]
T0['Lidz et al. 2010']     = Tdata[19:24]
T0['Schaye et al. 2000']   = Tdata[24:40]
T0['Lidz et al. 2014']     = Tdata[40:45]
T0['Bolton et al. 2010']   = Tdata[45,None]
T0['Boera et al. 2010']    = Tdata[46:49]
T0['Hiss et al. 2018']     = Tdata[49:57]
T0['Walther et al. 2018']  = Tdata[57:73]
T0['Rorai et al. 2018']    = Tdata[73,None]
T0['Bolton et al. 2012']   = Tdata[74,None]




######################
#  Tau effective HI  #
######################
tauHIdata = numpy.genfromtxt('dat/taueff_HI.dat')
taueffHI={'points':{}, 'ranges':{}, 'lowlim':{}}
taueffHI['points']['Becker et al. 2015'] = tauHIdata[  0: 91,0:2]
taueffHI['points']['Fan et al. 2006']    = tauHIdata[ 96:205,0:2]

taueffHI['lowlim']['Becker et al. 2015'] = tauHIdata[ 91: 96,0:2]
taueffHI['lowlim']['Fan et al. 2006']    = tauHIdata[206:209,0:2]

taueffHI['ranges']['Fan et al. 2006']    = tauHIdata[209:212]




########################
#  Tau effective HeII  #
########################
#z taueff err+ err-
tauHeIIdata = numpy.genfromtxt('dat/taueff_HeII.dat')
taueffHeII={'points':{}, 'lowlim':{}}
taueffHeII['points']['Worseck et al. 2016'] = tauHeIIdata[ 0: 87]

taueffHeII['lowlim']['Worseck et al. 2016'] = tauHeIIdata[87:103,0:2]
