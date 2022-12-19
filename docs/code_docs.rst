.. _FunctionsDocs:

Functions Documentation
***********************

CoReCon
=======

These functions work on the whole module (e.g. filtering, etc.)

.. automodule:: corecon
   :members:


Field class
===========

This class represents all constraints available concerning a single physical quantity. It is derived from python's 
`dictionary` class, and provides additional field and data-manipulation functionalities.

.. autoclass:: corecon.Field
   :members:

DataEntry class
===============

This class represents a single constraint (or set of) coming from a single source (usually a scientific publication).

.. autoclass:: corecon.DataEntry
   :members:


