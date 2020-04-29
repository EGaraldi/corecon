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

If you have already installe CoReCon and wish to upgrade it to the latest version, use:

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



