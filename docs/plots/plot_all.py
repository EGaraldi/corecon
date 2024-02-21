import sys
sys.path.insert(1, '../../')
import corecon as crc
import matplotlib.pyplot as plt
import numpy as np


markers = ['o', '^', 's', 'v', '*']

def plot_0d(param, xlab=None, ylab=None, xlog=False, ylog=False, legend_on_side=False, legend_ncol=1):
    
    print("plotting ", param)

    entries = crc.get(param)
    
    fig, ax = plt.subplots(1)

    ymin, ymax = 1e100, -1e100

    lcounter = 0
    for ik,k in enumerate(entries.keys()):
        
        #if k=="description": continue

        print("  ", k)
            
        #entries[k].values  [entries[k].values  ==None] = np.nan
        #entries[k].err_up  [entries[k].err_up  ==None] = 0.0
        #entries[k].err_down[entries[k].err_down==None] = 0.0

        pts = (~entries[k].upper_lim) & (~entries[k].lower_lim)
        ax.errorbar( ik+0.1*np.arange(len(entries[k].values[pts])), entries[k].values[pts], yerr=[ entries[k].err_down[pts], entries[k].err_up[pts] ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k)
        if any(pts):
            ymin = min(ymin, entries[k].values[pts].min())
            ymax = max(ymax, entries[k].values[pts].max())
        
        ul = (entries[k].upper_lim)
        ax.errorbar( ik+0.1*np.arange(len(entries[k].values[ul])), entries[k].values[ul], yerr=[ 0.1*np.ones_like(entries[k].values[ul]), 0.1*np.ones_like(entries[k].values[ul]) ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k, uplims=True)
        if any(ul):
            ymin = min(ymin, entries[k].values[ul].min())
            ymax = max(ymax, entries[k].values[ul].max())
        
        ll = (entries[k].lower_lim)
        ax.errorbar( ik+0.1*np.arange(len(entries[k].values[ll])), entries[k].values[ll], yerr=[ 0.1*np.ones_like(entries[k].values[ll]), 0.1*np.ones_like(entries[k].values[ll])  ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k, lolims=True)
        if any(ll):
            ymin = min(ymin, entries[k].values[ll].min())
            ymax = max(ymax, entries[k].values[ll].max())
    
        lcounter += 1

    if xlab is not None:
        ax.set_xlabel(xlab, fontsize=15)
    
    if ylab is not None:
        ax.set_ylabel(ylab, fontsize=15)
    else:
        ax.set_ylabel(entries.field_symbol, fontsize=15)

    if xlog:
        ax.set_xscale('log')

    if ylog:
        ax.set_yscale('log')
   
    factor_low  = 0.9 if ymin>=0 else 1.1
    factor_high = 1.1 if ymax>=0 else 0.9
    ax.set_ylim([factor_low*ymin, factor_high*ymax])
    
    ax.tick_params(axis='both', labelsize=13)

    #legend woth no duplicates
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    if legend_on_side:
        ax.legend(by_label.values(), by_label.keys(), ncol=legend_ncol, bbox_to_anchor=(1.0, 1.0), bbox_transform=ax.transAxes, loc='upper left')
    else:
        ax.legend(by_label.values(), by_label.keys(), ncol=legend_ncol)

    fig.savefig( param+".png" , bbox_inches='tight')  
    plt.close(fig)


def plot_1d(param, xlab=None, ylab=None, xlog=False, ylog=False, legend_on_side=False, legend_ncol=1, x_descriptor="redshift"):
    
    print("plotting ", param)

    entries = crc.get(param)
    
    fig, ax = plt.subplots(1)

    ymin, ymax = 1e100, -1e100

    lcounter = 0
    for ik,k in enumerate(entries.keys()):
        
        #if k=="description": continue

        print("  ", k)
            
        #entries[k].values  [entries[k].values  ==None] = np.nan
        #entries[k].err_up  [entries[k].err_up  ==None] = 0.0
        #entries[k].err_down[entries[k].err_down==None] = 0.0

        entries[k].axes = np.expand_dims(entries[k].axes, axis=entries[k].ndim)
        
        w = entries[k].dimensions_descriptors == x_descriptor
        if not any(w):
            print("ERROR: missing %s dimension for entry %s in %s. I won't plot this."%(x_descriptor, k, param))
            return
        zdim = np.where(w)[0][0]
    
        pts = (~entries[k].upper_lim) & (~entries[k].lower_lim)
        ax.errorbar( entries[k].axes[pts, zdim], entries[k].values[pts], yerr=[ entries[k].err_down[pts], entries[k].err_up[pts] ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k)
        if any(pts):
            ymin = min(ymin, entries[k].values[pts].min())
            ymax = max(ymax, entries[k].values[pts].max())
        
        ul = (entries[k].upper_lim)
        ax.errorbar( entries[k].axes[ul, zdim], entries[k].values[ul], yerr=[ 0.1*np.ones_like(entries[k].values[ul]), 0.1*np.ones_like(entries[k].values[ul]) ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k, uplims=True)
        if any(ul):
            ymin = min(ymin, entries[k].values[ul].min())
            ymax = max(ymax, entries[k].values[ul].max())
        
        ll = (entries[k].lower_lim)
        ax.errorbar( entries[k].axes[ll, zdim], entries[k].values[ll], yerr=[ 0.1*np.ones_like(entries[k].values[ll]), 0.1*np.ones_like(entries[k].values[ll])  ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k, lolims=True)
        if any(ll):
            ymin = min(ymin, entries[k].values[ll].min())
            ymax = max(ymax, entries[k].values[ll].max())
    
        lcounter += 1

    if xlab is not None:
        ax.set_xlabel(xlab, fontsize=15)
    else:
        ax.set_xlabel("redshift", fontsize=15)
    
    if ylab is not None:
        ax.set_ylabel(ylab, fontsize=15)
    else:
        ax.set_ylabel(entries.field_symbol, fontsize=15)

    if xlog:
        ax.set_xscale('log')

    if ylog:
        ax.set_yscale('log')
   
    factor_low  = 0.9 if ymin>=0 else 1.1
    factor_high = 1.1 if ymax>=0 else 0.9
    ax.set_ylim([factor_low*ymin, factor_high*ymax])
    
    ax.tick_params(axis='both', labelsize=13)

    #legend woth no duplicates
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    if legend_on_side:
        ax.legend(by_label.values(), by_label.keys(), ncol=legend_ncol, bbox_to_anchor=(1.0, 1.0), bbox_transform=ax.transAxes, loc='upper left')
    else:
        ax.legend(by_label.values(), by_label.keys(), ncol=legend_ncol)

    fig.savefig( param+".png" , bbox_inches='tight')  
    plt.close(fig)


def plot_2d(param, xlab=None, ylab=None, xlog=False, ylog=False, legend_on_side=False, legend_ncol=1):
    
    print("plotting ", param)

    entries = crc.get(param)
    
    fig, ax = plt.subplots(1)

    ymin, ymax = 1e100, -1e100

    lcounter = 0
    for ik, k in enumerate(entries.keys()):
        
        #if k=="description": continue
        
        print("  ", k)
                   
        #entries[k].values  [entries[k].values  ==None] = np.nan
        #entries[k].err_up  [entries[k].err_up  ==None] = 0.0
        #entries[k].err_down[entries[k].err_down==None] = 0.0
        
        
        w = entries[k].dimensions_descriptors == 'redshift'
        if not any(w):
            print("ERROR: missing redshift dimension for entry %s in %s. I won't plot this."%(k, param))
            return
        zdim = np.where(w)[0][0]
        
        #dimension to plot on x axis
        pdim = 0 if zdim > 0 else 1
        
        pts = (~entries[k].upper_lim) & (~entries[k].lower_lim)
        ax.errorbar( entries[k].axes[pts, pdim], entries[k].values[pts], yerr=[ entries[k].err_down[pts], entries[k].err_up[pts] ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k)
        if any(pts):
            ymin = min(ymin, entries[k].values[pts].min())
            ymax = max(ymax, entries[k].values[pts].max())
        
        ul = (entries[k].upper_lim)
        ax.errorbar( entries[k].axes[ul, pdim], entries[k].values[ul], yerr=[ 0.1*np.ones_like(entries[k].values[ul]), 0.1*np.ones_like(entries[k].values[ul]) ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k, uplims=True)
        if any(ul):
            ymin = min(ymin, entries[k].values[ul].min())
            ymax = max(ymax, entries[k].values[ul].max())
        
        ll = (entries[k].lower_lim)
        ax.errorbar( entries[k].axes[ll, pdim], entries[k].values[ll], yerr=[ 0.1*np.ones_like(entries[k].values[ll]), 0.1*np.ones_like(entries[k].values[ll])  ], fmt='C%i%s'%(lcounter%10, markers[lcounter//10]), label=k, lolims=True)
        if any(ll):
            ymin = min(ymin, entries[k].values[ll].min())
            ymax = max(ymax, entries[k].values[ll].max())
    
        lcounter += 1
 
    if xlab is not None:
        ax.set_xlabel(xlab, fontsize=15)
    
    if ylab is not None:
        ax.set_ylabel(ylab, fontsize=15)
    else:
        ax.set_ylabel(entries.field_symbol, fontsize=15)
    
    if xlog:
        ax.set_xscale('log')

    if ylog:
        ax.set_yscale('log')
   
    factor_low  = 0.9 if ymin>=0 else 1.1
    factor_high = 1.1 if ymax>=0 else 0.9
    ax.set_ylim([factor_low*ymin, factor_high*ymax])
    
    ax.tick_params(axis='both', labelsize=13)

    #legend woth no duplicates
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    if legend_on_side:
        ax.legend(by_label.values(), by_label.keys(), ncol=legend_ncol, bbox_to_anchor=(1.0, 1.0), bbox_transform=ax.transAxes, loc='upper left')
    else:                                                             
        ax.legend(by_label.values(), by_label.keys(), ncol=legend_ncol)

    fig.savefig( param+".png" , bbox_inches='tight')  
    plt.close(fig)


plot_1d("ionized_fraction", legend_on_side=True, legend_ncol=2)
plot_2d("Lya_flux_power_spectrum", xlog=True, ylog=True, xlab="k [s/km]")
plot_1d("mean_free_path")
plot_1d("IGM_temperature_mean_density")
plot_1d("effective_optical_depth_HI_Lya")
plot_1d("effective_optical_depth_HeII_Lya")
plot_1d("HeII_to_HI_column_density_ratio")
plot_2d("quasar_luminosity_function", legend_on_side=True, xlab="M_UV")
plot_2d("UV_luminosity_function", legend_on_side=True, xlab="M_UV")
plot_0d("optical_depth_CMB")
plot_1d("sfrd")
plot_2d("Lya_spike_galaxy_correlation", xlab="proper distance [pMpc]")#, x_descriptor="proper distance [pMpc]")
plot_2d("mass_gas_metallicity_relation", legend_on_side=True, xlab="$\log(M_*/M_\odot)$")
plot_2d("mass_stellar_metallicity_relation", legend_on_side=True, xlab="$\log(M_*/M_\odot)$")
plot_2d("galaxy_main_sequence", legend_on_side=True, ylog=True, xlab="$\log(M_*/M_\odot)$")
plot_1d("UV_slope")
plot_1d("ionizing_photons_production_efficiency")
plot_1d("photoionization_rate")
plot_1d("ionizing_photons_emission_rate")
plot_0d("reionization_midpoint")
plot_1d("UV_luminosity_density")
