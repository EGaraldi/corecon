.. _DataEntryTemplate:

Data Entry Template
===================

::

  dictionary_tag         = ""
  
  reference              = ""
          
  description            = \
  """
  """
  
  data_structure         = "grid" #grid or points
  
  ndim                   = 
  
  dimensions_descriptors = []
  
  axes                   = []
  
  values                 = []
  
  err_up                 = []
  
  err_down               = []
  
  err_up2                = []
  
  err_down2              = []
  
  upper_lim              = []
  
  lower_lim              = []


Fields description
^^^^^^^^^^^^^^^^^^

*dictionary_tag*: 
  a string which defines the name of the dictionary entry. Should correspond to a text 
  citation of the data paper, e.g. Garaldi et al. 2020.

*reference*: 
  a string containing the full reference to the data paper.
      
*description*: 
  a string containig a short description of the data contained in the file, and how they were obtained.

*data_structure*: 
  a string (either 'grid' of 'points') identifying the data layout in the file. See :ref:`InputDataLayout` 
  for more details.

*ndim*: 
  an integer containing the number of dimension each data point depends on (i.e. the number of independent variables). 

*dimensions_descriptors*: 
  a list of strings describing the independent variables.

*axes*: 
  the values of the independent variable(s). If ``data_structure=='grid'``, this should be a collection of ndim lists, 
  each containing the values of one independent variable. If ``data_structure=='points'``, this should be a list of ndim-long lists,
  each containing the values of the independent variable(s) for a specific datapoint.

*values*: 
  the values of the dependent variable. If ``data_structure=='grid'``, this should be a ndim-dimensional array such that
  ``values[i,j,k,..]`` corresponds to ``(axes[0][i], axes[1][j], axes[2][k], ...)``. If ``data_structure=='points'``, this should be a
  1-dimensional array of value, such that ``values[i]`` corresponds to ``axes[i]``.

*err_up*: 
  same as values, but containing the upper error. If ``None``, it will be expanded to the right shape.

*err_down*: 
  same as values, but containing the lower error. If ``None``, it will be expanded to the right shape.  

*err_up2*: 
  same as values, but containing a second (larger) upper error. If ``None``, it will be expanded to the right shape.    

*err_down2*: 
  same as values, but containing a second (larger) lower error. If ``None``, it will be expanded to the right shape.  

*upper_lim*: 
  same as values, but containing a boolean value that signals if a data point is an upper limit. If ``False`` or
  ``True``, it will be expanded to the right shape.  

*lower_lim*: 
  same as values, but containing a boolean value that signals if a data point is an lowe limit. If ``False`` or
  ``True``, it will be expanded to the right shape.


.. _InputDataLayout:

Input Data Layout
^^^^^^^^^^^^^^^^^

Currently there are two supported layout for data files, ``grid`` and ``points``. The layout can be different for each data entry file. 
CoReCon takes care of transforming the data into the ``points`` layout, which is the one exposed to the user.

The ``points`` layout is the most straightforward one, but also the most verbose. Each point is described by a unique combination of 
independent variables, and a single value for the dependent one. Hence, the ``axes`` array consist of a list of ndim-long tuples, i.e.
``shape(axes) = (Npts, ndim)`` and ``shape(values) = shape(err_up) = ... = Npts``.

The ``grid`` layout is suitable for data points organized in a ndim-dimensional grid. In this case, the ``axes`` variable descibres each
dimension using a list of grid points, i.e. ``shape(axes) = (ndim, ?)`` where the ``?`` indicates that each entry can have a different 
length (as it describes a different dimension in the ndim-dimensional grid. For this layout, the values, err_up, ... variables are in 
a ndim-dimensional grid, i.e. ``shape(values) = shape(err_up) = ... = (len(axes[0]), len(axes[1]), len(axes[2]), ...)``.
grid points along each dimension 

