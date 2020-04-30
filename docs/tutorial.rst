.. _Tutorial:

Using CoReCon: tutorial
=======================

0. Installation
^^^^^^^^^^^^^^^
*WARNING: CoReCon is still in the beta-testing phase.*

CoReCon can be installed as a python module, using:

.. code-block:: bash

    pip install -i https://test.pypi.org/simple/ corecon

and then loaded e.g. using:

.. code-block:: python

    import corecon as crc

If you have already installed CoReCon and wish to upgrade it to the latest version, use:

.. code-block:: bash

    pip install -U -i https://test.pypi.org/simple/ corecon

1. Data organization and retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoReCon stores data in an individual DataEntry class for each data source. The available fields are described
in :ref:`DataEntryTemplate`, while the available utility functions are described below.

DataEntry classes are stored in dictionaries, sorted based on the physical quantity they describe, whose keys are
the source paper short citation. Available quantities are listed in the section :ref:`AvailableCoinstraints`, 
and can also be retrieved from python using:

.. code-block:: python

    available_fields = crc.fields()

This returns a tuple containing all available field names (as strings). These strings are used to specify the data to 
load, using (for e.g. the quasar luminosity function, shorthanded to qlf):

.. code-block:: python

   qlf = crc.get("qlf")
   
   for k in qlf.keys():
       print(k)

   > description
   > Kulkarni et al. 2019
   > Giallongo et al. 2015
   > McGreer et al. 2013
   > Yang et al. 2016
   > Willott et al. 2010
   > Jiang et al. 2016
   > Kashikawa et al. 2015
   > Glikman et al. 2011
   > Giallongo et al. 2019
   > Ross et al. 2013

All keys are string. The first one (description) contains a string with a breif description (using matplotlib's Math Text) of
the quantity used in values, err_up, err_down, err_up2, err_down2, including their units (if present). 

It is also possible to retrieve all available dictionaries, using:

.. code-block:: python

   all_dicts = crc.get_all_dicts()

which returns a dictionary, whose keys are the available field. Retrieving a key produces the same result as using crc.get() with
the same key.

In case you want to add your own dataset, this can be done simply adding a properly-formatted file into one of the data/ subdirectories.
You can find more information on the format in :ref:`DataEntryTemplate`. For convenience, such template can be retrieved directly from
CoReCon using:

.. code-block:: python

   template_string = crc.get_data_entry_template()

which returns the template as a string.


2. Utility functions
^^^^^^^^^^^^^^^^^^^^
CoReCon provides also some basic utilities functions. 

Available constraints within a redshift range can be retrieved with:

.. code-block:: python

   qlf_zrange = crc.get_redshift_range("qlf", 5.0, 6.0)

Similarly, the data available can be filtered to return only upper or lower limits, using:

.. code-block:: python

   qlf_ll = crc.get_lower_limits("qlf")
   qlf_ul = crc.get_upper_limits("qlf")

In each DataEntry, upper and lower limits can be swapped (e.g. to be used in derived quantity, for instance 1-ionised_fraction) 
using:

.. code-block:: python

   qlf['Kulkarni et al. 2019'].swap_limits()

CoReCon uses python's None to indicate missing data entries. In case they need to be replaced (e.g. for plotting or operation
on data), CoReCon provides the following utilities:

.. code-block:: python

   qlf['Kulkarni et al. 2019'].none_to_value(0.0)
   qlf['Kulkarni et al. 2019'].none_to_nan()

where the second is equivalent to passing np.nan to the first as parameter.

Finally, CoReCon provides a function that replaces all the entries in err_up, err_down, err_up2, err_down2 corresponding
to upper or lower limits with a user defined value v, which can be specified as a fraction of the correspondent value entries.
It can be used with:

.. code-block:: python

   qlf['Kulkarni et al. 2019'].set_lim_errors(0.1, frac_of_values=True)


2. Complete example
^^^^^^^^^^^^^^^^^^^

Finally, we provide here a simple head-to-tail example of usage, namely to create a plot of the ionized fraction evolution with redshift.

.. code-block:: python

   import corecon as crc
   import matplotlib.pyplot as plt
   import numpy as np

   #get IGM temperature at mean density
   ionfr = crc.get("T0")

   #create figure, ax, and markers cycle
   fig, ax = plt.subplots(1) 
   markers = ['o', 's', 'D'] 
   
   #loop over available datasets
   for ik,k in enumerate(ionfr.keys()):

       if k=="description": 
           continue 
       
       #find redshift dimension 
       zdim = np.where(ionfr[k].dimensions_descriptors == "redshift")[0][0] 

       #get format
       fmt = "%s%Ci"%(markers[ik//10], ik%10)

       #transform to neutral fraction
       ionfr[k].values = 1-ionfr[k].values 
       # ...need to swap limits
       ionfr[k].swap_limits()
       #transform None's (in errors) into values to set arrow length
       ionfr[k].none_to_value(0.1)

       #plot 
       ax.errorbar(ionfr[k].axes[:,zdim], ionfr[k].values, 
                   yerr=[ionfr[k].err_down, ionfr[k].err_up], 
                   lolims=ionfr[k].lower_lim, uplims=ionfr[k].upper_lim, 
                   fmt=fmt, label=k) 
   
   #move legend to side
   ax.legend(bbox_to_anchor=(1.0, 1.0), bbox_transform=ax.transAxes, loc='upper left') 
   
   #save figure and close
   fig.savefig( "neutral_fraction_evolution.png" , bbox_inches='tight')
   plt.close(fig)

The above script produce the following plot:

.. image:: neutral_fraction_evolution.png
  :width: 800

