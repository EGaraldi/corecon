.. _CoReCon:

CoReCon: open Collection of Reionization Constraints
====================================================

**CoReCon** is an open collection of constraints on various physical
quantities linked to the *Epoch of Reionization (EoR)*.

It is built to be easily complemented by contribution from the scientific
community, thanks to a simple data form that supports two different ways of 
input data.

CoReCon takes care of loading and interpreting the data, and presenting them 
in an organic and ready-to-use way. It also implement simple slicing capabilities,
which allow to perform simple data filtering.


.. _AddYourConstraint:

Adding your constraint
^^^^^^^^^^^^^^^^^^^^^^
CoReCon has been developed with in mind the contribution from the community. In order 
to add a constraint to the available one, we provide an empty :ref:`DataEntryTemplate`.


.. _AvailableCoinstraints:

Available constraints
^^^^^^^^^^^^^^^^^^^^^
Click to see more details.

- :ref:`ionized_fraction`
- :ref:`T0`
- :ref:`tau_eff_HI`
- :ref:`tau_eff_HeII`
- :ref:`glf`
- :ref:`qlf`
- :ref:`mfp`
- :ref:`Lya_flux_ps`
- :ref:`eta`
- :ref:`tau_cmb`

.. _UsingCoReCon:

Using CoReCon
^^^^^^^^^^^^^
CoReCon is still in the beta-testing phase. If you want to try it out, 
it can be installed as a python module, using:

.. code-block:: bash

    pip install -i https://test.pypi.org/simple/ corecon

For an introduction on how to use CoReCon, check :ref:`Tutorial`.


.. _FunctionDocs:

Function Docs
^^^^^^^^^^^^^
The documentation for CoReCon public functions can be found at :ref:`Docs`.


.. _Author:

Author
^^^^^^
Enrico Garaldi
 |  Post-doctoral fellow, 
 |  Max-Planck-Insitut fur Astrophysik
 |  Garching bei Munchen, Germany
 |  email: egaraldi ~at~ mpa-garching ~dot~mpg ~dot~ de
 

.. toctree::
  :hidden:
  :maxdepth: 3

  index

