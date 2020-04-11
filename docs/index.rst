ReCon: open collection of Reionization Constraints
==================================================

**ReCon** is an open collection of constraints on various physical
quantities linked to the *Epoch of Reionization (EoR)*.

It is built to be easily complemented by contribution from the scientific
community, thanks to a simple data form that supports two different ways of 
input data.

ReCon takes care of loading and interpreting the data, and presenting them 
in an organic wnd ready-to-use way. It also implement simple slicing capabilities,
which allow to perform simple data filtering.


Adding your constraint
^^^^^^^^^^^^^^^^^^^^^^
ReCon has been developed with in mind the contribution from the community. In order 
to add a constraint to the available one, we provide an empty :ref:`DataEntryTemplate`.


Available constraints
^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   sources/ionized_fraction.rst
   sources/T0.rst
   sources/tau_eff_HI.rst
   sources/tau_eff_HeII.rst
   sources/qlf.rst
   sources/mfp.rst
   sources/Lya_flux_ps.rst
   sources/eta.rst



Indices and tables
^^^^^^^^^^^^^^^^^^

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`