# ReCon

Collection of constraints on cosmic reionization

## Structure
recon
  |
  -- \<field1\>  (LF, xHI, ...)
  |
  -- \<field2\>
  |
  -- ...
  |
  -- get\_fields()

\<field\>
  |
  -- \<data1\>
  |
  -- \<data1\>
  |
  -- ...
  |
  -- get\_entries()


\<data\>
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



