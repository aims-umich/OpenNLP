##############
 Installation
##############

.. _prerequisites:

***************
 Prerequisites
***************

OpenNLP currently supports Python 3.9 and 3.10. Below are the required
dependencies for OpenNLP with the version combination that yields most stable performance. There is no need to install these yourself as
OpenNLP will also install all needed dependencies. They are listed here for your reference only.

.. admonition:: Required
   :class: error
   
   -  textblob==0.17.1
   -  nltk==3.8.1
   -  torch==2.1.0
   -  scikit-learn==1.3.1
   -  pandas==2.1.1
   -  transformers==4.33.2
   -  tensorflow==2.10.1
   -  keras-preprocessing==1.1.2
   -  keras==2.10.0
   -  matplotlib==3.8.0
   -  peft==0.5.0
   -  requests==2.31.0
   -  seaborn==0.13.0
   -  torchmetrics==1.2.0
   -  bitsandbytes==0.41.1

..
	.. admonition:: Optional
	   :class: note
	
	   -  `Jupyter <https://jupyter.org/>`_
	   -  `OpenCV <https://opencv.org/>`_
	   -  `SciPy <https://scipy.org/>`_

*****
 Pip
*****

Installation via pip is coming soon after we make our first stable release on pypi. For now, use the installation from source. 

..
	Install through Pip by running:
	
	.. code:: sh
	
	   pip install pyMAISE
	
	To install a specific version of pyMAISE, run:
	
	.. code:: sh
	
	   pip install pyMAISE==<version>
	
	Released versions and a discussion of the changes are listed in the
	:ref:`versions`. Only stable versions are listed on PyPI. For other
	versions or the latest features, install pyMAISE from the source. 

*************
 From Source
*************

For the latest features in development, install
OpenNLP from source. Clone the repository using ``git`` and running:

.. code:: sh

   git clone https://github.com/aims-umich/OpenNLP
   cd OpenNLP/

For a specific version, then checkout the branch based on the command below. If you want to use the latest version on Github, skip the next command. 

.. code:: sh

   git checkout <version>

Then install OpenNLP through pip:

.. code:: sh

   pip install .


For OpenNLP developers, we recommend using the ``-e`` option and installing
the ``dev`` extension:

.. code:: sh

   pip install -e ".[dev]"
