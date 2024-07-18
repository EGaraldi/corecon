import sys
sys.path.insert(1, '../../')
import corecon as crc
import numpy as np
import plotly.graph_objs as go

def get_error(object, err_label):
    error = getattr(object, err_label, None)
    if error is None:
        error = np.zeros_like(object.values)
    else:
        error[np.isnan(error.astype(float))] = 0.0
    return error



def plot_0d(param, xlab=None, ylab=None, xlog=False, ylog=False):

    print("plotting ", param)
    
    f = go.Figure()
    markersize = 8

    entries = crc.get(param)

    xmin, xmax = np.inf, -np.inf
    ymin, ymax = np.inf, -np.inf

    lcounter = 0
    for ik,k in enumerate(sorted(entries.keys())):

        print("  ", k)
        entry = entries[k]

        #find min and max of x and y
        xmin = min(xmin, np.min(ik)) # - getattr(entry, 'err_left', 0.0)))
        ymin = min(ymin, np.min(entry.values)) # - entry.err_down))
        xmax = max(xmax, np.max(ik+0.1*(len(entry.values)-1))) # + getattr(entry, 'err_right', 0.0)))
        ymax = max(ymax, np.max(entry.values)) # + entry.err_up))

        #prepare symbols based on measurements (circles), lower limits (arrow up) and upper limits (arrow down)
        #  Note: for a bug, symbols with '-' in the name don't work -> use their numerical value
        symbols = np.array(['circle']*len(entry.values))
        symbols[entry.upper_lim] = 19
        symbols[entry.lower_lim] = 20
        
        trace =go.Scatter(x = ik+0.1*np.arange(len(entry.values)),
                          y = entry.values,
                          error_y = dict(array=entry.err_up, arrayminus=entry.err_down),
                          mode = "markers",
                          name = k, # <a href='https://wwwmpa.mpa-garching.mpg.de/~egaraldi/thesan/data.html'>[source]</a>",
                          marker = dict(symbol=symbols, size=markersize, line=dict(width=2, color='DarkSlateGrey')),
                          text= "",
                          # customdata=np.array([entry.redshift, entry.err_down, entry.err_up]).T,       
                          # hovertemplate='<br>'.join([
                          #     '(%{x:.2f}, %{y:.2f}',
                          #     'z = %{customdata[0]:.2f}',
                          #     'err_up = %{customdata[1]:.2f}',
                          #     'err_down = %{customdata[2]:.2f}',
                          # ])
                          #hoverinfo='none'
                         )
        f.add_trace(trace)
        lcounter += 1

    #fix range
    deltax = xmax-xmin
    deltay = ymax-ymin
    frac_to_extend = 0.05
    f.update_xaxes(range=[xmin-frac_to_extend*deltax, xmax+frac_to_extend*deltax])
    f.update_yaxes(range=[ymin-frac_to_extend*deltay, ymax+frac_to_extend*deltay])

    
    if xlab is not None:
        f.update_xaxes(title=xlab.replace("$",""))

    if ylab is not None:
        f.update_yaxes(title=ylab.replace("$",""))
    else:
        f.update_yaxes(title=entries.field_symbol)

    if xlog:
        f.update_xaxes(type='log')

    if ylog:
        f.update_yaxes(type='log')
    
    f.write_html(f"plots/{param}.html")#, full_html=False)



def plot_1d(param, xlab=None, ylab=None, xlog=False, ylog=False, x_descriptor="redshift"):

    print("plotting ", param)
    
    f = go.Figure()
    markersize = 8

    entries = crc.get(param)

    xmin, xmax = np.inf, -np.inf
    ymin, ymax = np.inf, -np.inf

    lcounter = 0
    for ik,k in enumerate(sorted(entries.keys())):

        print("  ", k)
        entry = entries[k]

        if entry.ndim==1:
            entry.axes = np.expand_dims(entry.axes, axis=entry.ndim)
        
        w = entry.dimensions_descriptors == x_descriptor
        if not any(w):
            print("ERROR: missing %s dimension for entry %s in %s. I won't plot this."%(x_descriptor, k, param))
            return
        zdim = np.where(w)[0][0]

        err_left = get_error(entry, 'err_left' )
        if err_left.ndim > 1: err_left = err_left[:,zdim]
        err_right = get_error(entry, 'err_right' )
        if err_right.ndim > 1: err_right = err_right[:,zdim]
        err_up   = get_error(entry, 'err_up' )
        err_down = get_error(entry, 'err_down' )

        #find min and max of x and y
        xmin = min(xmin, np.min(entry.axes[:, zdim] )) #- err_left ))
        ymin = min(ymin, np.min(entry.values        )) #- err_down ))
        xmax = max(xmax, np.max(entry.axes[:, zdim] )) #+ err_right))
        ymax = max(ymax, np.max(entry.values        )) #+ err_up   ))

        #prepare symbols based on measurements (circles), lower limits (arrow up) and upper limits (arrow down)
        #  Note: for a bug, symbols with '-' in the name don't work -> use their numerical value
        symbols = np.array(['circle']*len(entry.values))
        symbols[entry.upper_lim] = 19
        symbols[entry.lower_lim] = 20
        
        trace =go.Scatter(x = entry.axes[:, zdim],
                          y = entry.values,
                          error_x = dict(array=err_left, arrayminus=err_right),
                          error_y = dict(array=err_up, arrayminus=err_down),
                          mode = "markers",
                          name = k, # <a href='https://wwwmpa.mpa-garching.mpg.de/~egaraldi/thesan/data.html'>[source]</a>",
                          marker = dict(symbol=symbols, size=markersize, line=dict(width=2, color='DarkSlateGrey')),
                          text= "",
                          # customdata=np.array([entry.redshift, entry.err_down, entry.err_up]).T,       
                          # hovertemplate='<br>'.join([
                          #     '(%{x:.2f}, %{y:.2f}',
                          #     'z = %{customdata[0]:.2f}',
                          #     'err_up = %{customdata[1]:.2f}',
                          #     'err_down = %{customdata[2]:.2f}',
                          # ])
                          #hoverinfo='none'
                         )
        f.add_trace(trace)

        lcounter += 1

    #fix range
    deltax = xmax-xmin
    deltay = ymax-ymin
    frac_to_extend = 0.05
    f.update_xaxes(range=[xmin-frac_to_extend*deltax, xmax+frac_to_extend*deltax])
    f.update_yaxes(range=[ymin-frac_to_extend*deltay, ymax+frac_to_extend*deltay])

    
    if xlab is not None:
        f.update_xaxes(title=xlab.replace("$",""))
    else:
        f.update_xaxes(title='redshift')
        

    if ylab is not None:
        f.update_yaxes(title=ylab.replace("$",""))
    else:
        f.update_yaxes(title=entries.field_symbol)

    if xlog:
        f.update_xaxes(type='log')

    if ylog:
        f.update_yaxes(type='log')
    
    f.write_html(f"plots/{param}.html")#, full_html=False)


def plot_2d(param, xlab=None, ylab=None, xlog=False, ylog=False, x_descriptor="redshift"):

    print("plotting ", param)
    
    f = go.Figure()
    markersize = 8

    entries = crc.get(param)

    xmin, xmax = np.inf, -np.inf
    ymin, ymax = np.inf, -np.inf

    lcounter = 0
    for ik,k in enumerate(sorted(entries.keys())):

        print("  ", k)
        entry = entries[k]

        if entry.ndim==1:
            entry.axes = np.expand_dims(entry.axes, axis=entry.ndim)
        
        w = entry.dimensions_descriptors == x_descriptor
        if not any(w):
            print("ERROR: missing %s dimension for entry %s in %s. I won't plot this."%(x_descriptor, k, param))
            return
        zdim = np.where(w)[0][0]

        #dimension to plot on x axis
        pdim = 0 if zdim > 0 else 1

        err_left = get_error(entry, 'err_left' )
        if err_left.ndim > 1: err_left = err_left[:,zdim]
        err_right = get_error(entry, 'err_right' )
        if err_right.ndim > 1: err_right = err_right[:,zdim]
        err_up   = get_error(entry, 'err_up' )
        err_down = get_error(entry, 'err_down' )

        #find min and max of x and y
        xmin = min(xmin, np.min(entry.axes[:, pdim]))# - err_left ))
        ymin = min(ymin, np.min(entry.values       ))# - err_down ))
        xmax = max(xmax, np.max(entry.axes[:, pdim]))# + err_right))
        ymax = max(ymax, np.max(entry.values       ))# + err_up   ))


        #prepare symbols based on measurements (circles), lower limits (arrow up) and upper limits (arrow down)
        #  Note: for a bug, symbols with '-' in the name don't work -> use their numerical value
        symbols = np.array(['circle']*len(entry.values))
        symbols[entry.upper_lim] = 19
        symbols[entry.lower_lim] = 20
        
        trace =go.Scatter(x = entry.axes[:, pdim],
                          y = entry.values,
                          error_x = dict(array=err_left, arrayminus=err_right),
                          error_y = dict(array=err_up, arrayminus=err_down),
                          mode = "markers",
                          name = k, # <a href='https://wwwmpa.mpa-garching.mpg.de/~egaraldi/thesan/data.html'>[source]</a>",
                          marker = dict(symbol=symbols, size=markersize, line=dict(width=2, color='DarkSlateGrey')),
                          text= "",
                          customdata=entry.redshift, 
                          # hovertemplate='<br>'.join([
                          #     '(%{x:.2f} + %{error_x['array'], %{y:.2f}',
                          #     'z = %{customdata[0]:.2f}',
                          #     'err_up = %{customdata[1]:.2f}',
                          #     'err_down = %{customdata[2]:.2f}',
                          # ])
                          #hoverinfo='none'
                         )
        f.add_trace(trace)

        lcounter += 1

    #fix range
    deltax = xmax-xmin
    deltay = ymax-ymin
    frac_to_extend = 0.05
    f.update_xaxes(range=[xmin-frac_to_extend*deltax, xmax+frac_to_extend*deltax])
    f.update_yaxes(range=[ymin-frac_to_extend*deltay, ymax+frac_to_extend*deltay])

    
    if xlab is not None:
        f.update_xaxes(title=xlab.replace("$",""))
    else:
        f.update_xaxes(title='redshift')
        

    if ylab is not None:
        f.update_yaxes(title=ylab.replace("$",""))
    else:
        f.update_yaxes(title=entries.field_symbol)

    if xlog:
        f.update_xaxes(type='log')
        f.update_xaxes(range=[np.log10(np.maximum(0.95*xmin, xmin-frac_to_extend*deltax)), np.log10(xmax+frac_to_extend*deltax)])

    if ylog:
        f.update_yaxes(type='log')
        f.update_yaxes(range=[np.log10(np.maximum(0.95*ymin, ymin-frac_to_extend*deltay)), np.log10(ymax+frac_to_extend*deltay)])
    
    f.write_html(f"plots/{param}.html")#, full_html=False)


plot_1d("HII_fraction", ylab='x_HII')
plot_1d("HeIII_fraction", ylab='x_HeIII')
plot_2d("Lya_flux_power_spectrum", xlog=True, ylog=True, xlab="k [s/km]", ylab='P [km/s]')
plot_1d("mean_free_path", ylab='mfp [Mpc/h]')
plot_1d("IGM_temperature_mean_density", ylab='T_0 [K]')
plot_1d("effective_optical_depth_HI_Lya", ylab='tau_eff,HI')
plot_1d("effective_optical_depth_HeII_Lya", ylab='tau_eff,HeII')
plot_1d("HeII_to_HI_column_density_ratio", ylab='eta')
plot_2d("quasar_luminosity_function", xlab="M_UV", ylab='log(phi [Mpc^-3 dex^-1])')
plot_2d("UV_luminosity_function", xlab="M_UV", ylab='log(phi [Mpc^-3 dex^-1])')
plot_0d("optical_depth_CMB", ylab='tau_CMB')
plot_1d("sfrd", ylab='log(Psi [Msun yr^-1 Mpc^-3])')
plot_2d("Lya_spike_galaxy_correlation", xlab="proper distance [pMpc]", ylab='T(r)/<T>-1')#, x_descriptor="proper distance [pMpc]")
plot_2d("mass_gas_metallicity_relation", xlab="log(M_*/M_sun)", ylab='log(O/H)+12')
plot_2d("mass_stellar_metallicity_relation", xlab="log(M_*/M_sun)", ylab='log(O/H)+12')
plot_2d("galaxy_main_sequence", ylog=True, xlab="log(M_*/M_sun)", ylab='SFR [Msun/yr]')
plot_1d("UV_slope", ylab='beta')
plot_1d("ionizing_photons_production_efficiency", ylab='log(csi_ion [Hz erg^-1])')
plot_1d("HI_photoionization_rate", ylab='Gamma_HI [s^-1]')
plot_1d("ionizing_photons_emission_rate", ylab='Ndot_ion [s^-1 Mpc^-3]')
plot_0d("reionization_midpoint", ylab='z_mid')
plot_1d("UV_luminosity_density", ylab='log(rho_UV [erg s^-1 Hz^-1 Mpc^-3])')
