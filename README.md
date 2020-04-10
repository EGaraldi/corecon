# ReCon

Collection of constraints on cosmic reionization

## Structure
ReCon
  |
  -- \<QuantityDict1\>  (LF, xHI, ...)
  |
  -- \<QuantityDict\>  (LF, xHI, ...)
  |
  -- ...
  |
  -- get\_fields()

\<QuantityDict\>
  |
  -- \<DataEntry1\>
  |
  -- \<DataEntry2\>
  |
  -- ...


\<DataEntry\>
  |
  -- dictionary\_tag
  |
  -- ndim
  |
  -- description
  |
  -- reference
  |
  -- dimensions\_descriptors[ndim]
  |
  -- axes[ndim]
  |
  -- values[ndim, ndata]
  |
  -- error\_up[ndim, ndata]
  |
  -- error\_down[ndim, ndata]
  |
  -- error\_up2[ndim, ndata]
  |
  -- error\_down2[ndim, ndata]
  |
  -- upper\_lim[ndim, ndata]
  |
  -- lower\_lim[ndim, ndata]



