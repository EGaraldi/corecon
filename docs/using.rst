.. _UsingCoReCon:

Using CoReCon
^^^^^^^^^^^^^

Installation
""""""""""""
CoReCon is still in the beta-testing phase. If you want to try it out, 
it can be installed as a python module, using:

.. code-block:: bash

    pip install corecon

Tutorial
""""""""
For an introduction on how to use CoReCon, check :ref:`Tutorial`.


Known issues
""""""""""""

CoReCon hangs during import
---------------------------
Users using some internet providers have reported_ issues in connecting to github raw user contents, which is used by CoReCon to autonomously update available 
constraints when imported. For some users this results in the import statement hanging.

.. _reported: https://github.com/orgs/community/discussions/42655

In order to circumvent this, create an empty file named exactly ``skip_update`` in the filder where CoReCon is installed (i.e. where its ``__init__.py`` file is located). 
This will prevent CoReCon from trying to update the constraint at startup. Therefore, to update the available constraints you will have to manually download the `data directory`_ 
from the GitHub repository and replace the local data directory. 

.. _data directory: https://github.com/EGaraldi/corecon/tree/master/corecon/data

To restart automatic updates, simply remove the ``skip_update`` file. 


