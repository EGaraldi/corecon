import sys
sys.path.insert(1, '../../')
import ReCon
import matplotlib.pyplot as plt
import numpy as np


def plot_1d(param, xlab=None, ylab=None, xlog=False, ylog=False, legend_on_side=False, legend_ncol=1):
    
    print("plotting ", param)

    entries = getattr(ReCon, param)
    
    fig, ax = plt.subplots(1)

    for ik,k in enumerate(entries.keys()):
        print("  ", k)
            
        entries[k].values  [entries[k].values  ==None] = np.nan
        entries[k].err_up  [entries[k].err_up  ==None] = 0.0
        entries[k].err_down[entries[k].err_down==None] = 0.0

        if entries[k].ndim == 1:
            assert(entries[k].dimensions_descriptors[0] == 'redshift')

            pts = (~entries[k].upper_lim) & (~entries[k].lower_lim)
            ax.errorbar( entries[k].axes[pts], entries[k].values[pts], yerr=[ entries[k].err_up[pts], entries[k].err_down[pts] ], fmt='C%io'%(ik%10), label=k)
            
            ul = (entries[k].upper_lim)
            ax.errorbar( entries[k].axes[ul], entries[k].values[ul], yerr=[ entries[k].err_up[ul], entries[k].err_down[ul] ], fmt='C%io'%(ik%10), label=k, uplims=True)
            
            ll = (entries[k].lower_lim)
            ax.errorbar( entries[k].axes[ll], entries[k].values[ll], yerr=[ entries[k].err_up[ll], entries[k].err_down[ll] ], fmt='C%io'%(ik%10), label=k, lolims=True)
        
        elif entries[k].ndim == 2:     
            w = entries[k].dimensions_descriptors == 'redshift'
            if not any(w):
                print("ERROR: missing redshift dimension for entry %s in %s"%(k, param))
            zdim = np.where(w)[0][0]
        
            pts = (~entries[k].upper_lim) & (~entries[k].lower_lim)
            ax.errorbar( entries[k].axes[pts, zdim], entries[k].values[pts], yerr=[ entries[k].err_up[pts], entries[k].err_down[pts] ], fmt='C%io'%(ik%10), label=k)
            
            ul = (entries[k].upper_lim)
            ax.errorbar( entries[k].axes[ul, zdim], entries[k].values[ul], yerr=[ 0.1*np.ones_like(entries[k].values[ul]), 0.1*np.ones_like(entries[k].values[ul]) ], fmt='C%io'%(ik%10), label=k, uplims=True)
            
            ll = (entries[k].lower_lim)
            ax.errorbar( entries[k].axes[ll, zdim], entries[k].values[ll], yerr=[ 0.1*np.ones_like(entries[k].values[ll]), 0.1*np.ones_like(entries[k].values[ll])  ], fmt='C%io'%(ik%10), label=k, lolims=True)

    if xlab is not None:
        ax.set_xlabel(xlab)
    else:
        ax.set_xlabel("redshift")
    
    if ylab is not None:
        ax.set_ylabel(ylab)
    else:
        ax.set_ylabel(param)
    
    if xlog:
        ax.set_xscale('log')

    if ylog:
        ax.set_yscale('log')
   
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

    entries = getattr(ReCon, param)
    
    fig, ax = plt.subplots(1)

    for ik, k in enumerate(entries.keys()):
        
        print("  ", k)
                   
        entries[k].values  [entries[k].values  ==None] = np.nan
        entries[k].err_up  [entries[k].err_up  ==None] = 0.0
        entries[k].err_down[entries[k].err_down==None] = 0.0
        
        
        w = entries[k].dimensions_descriptors == 'redshift'
        if not any(w):
            print("ERROR: missing redshift dimension for entry %s in %s"%(k, param))
        zdim = np.where(w)[0][0]
        
        #dimension to plot on x axis
        pdim = 0 if zdim > 0 else 1
        
        pts = (~entries[k].upper_lim) & (~entries[k].lower_lim)
        ax.errorbar( entries[k].axes[pts, pdim], entries[k].values[pts], yerr=[ entries[k].err_up[pts], entries[k].err_down[pts] ], fmt='C%io'%(ik%10), label=k)
        
        ul = (entries[k].upper_lim)
        ax.errorbar( entries[k].axes[ul, pdim], entries[k].values[ul], yerr=[ 0.1*np.ones_like(entries[k].values[ul]), 0.1*np.ones_like(entries[k].values[ul]) ], fmt='C%io'%(ik%10), label=k, uplims=True)
        
        ll = (entries[k].lower_lim)
        ax.errorbar( entries[k].axes[ll, pdim], entries[k].values[ll], yerr=[ 0.1*np.ones_like(entries[k].values[ll]), 0.1*np.ones_like(entries[k].values[ll])  ], fmt='C%io'%(ik%10), label=k, lolims=True)
 
    if xlab is not None:
        ax.set_xlabel(xlab)
    
    if ylab is not None:
        ax.set_ylabel(ylab)
    else:
        ax.set_ylabel(param)
    
    if xlog:
        ax.set_xscale('log')

    if ylog:
        ax.set_yscale('log')

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
plot_2d("Lya_flux_ps", xlog=True, ylog=True)
plot_1d("mfp")
plot_1d("T0")
plot_1d("tau_eff_HI")
plot_1d("tau_eff_HeII")
plot_1d("eta")
plot_2d("qlf", legend_on_side=True)
