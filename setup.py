# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:08:52 2021

@author: majdi
"""

import os
import sys
import subprocess
from setuptools import setup, find_packages
from distutils.version import LooseVersion
from opennlp.version import version
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)

#check python version
if sys.version_info.major != 3:
    raise ValueError('--ERROR: This package is only compatible with Python 3, but you are running '
          'Python {}. The installation will likely fail.'.format(sys.version_info.major))
    
# The directory containing this file
HERE = os.getcwd()

# The text of the README file
with open(os.path.join(HERE , "README.md"), encoding='utf-8') as f:
    README = f.read()
    
    
long_description = r"""
# OpenNLP

The OpenNLP package is an extensive toolkit for natural language processing, 
specifically designed for classification tasks. It includes a variety of tools 
such as classical machine learning models, neural networks, and large 
language models. While our main focus of these tools is for sentiment 
analysis and classification, they can be applied to any classification 
problems by the users. The package is developed and maintained by the 
Artificial Intelligence and Multiphysics Simulation group (AIMS) at 
the University of Michigan. See our first application of OpenNLP on 
studying the United States public sentiment about nuclear power on social media.  

Repository:
https://github.com/aims-umich/OpenNLP

Main Paper:
https://doi.org/10.1016/j.rser.2024.114570

"""

# Read version from file
__version__ = version()
    
# Check tensorflow installation to avoid
# breaking pre-installed tf gpu ##(credit to @hill-a and stable-baselines)
def find_tf_dependency():
    install_tf, tf_gpu = False, False
    try:
        import tensorflow as tf
        if tf.__version__ < LooseVersion('2.10.1'):
            install_tf = True
            # check if a gpu version is needed
            tf_gpu = tf.test.is_gpu_available()
    except ImportError:
        install_tf = True
        # Check if a nvidia gpu is present
        for command in ['nvidia-smi', '/usr/bin/nvidia-smi', 'nvidia-smi.exe']:
            try:
                if subprocess.call([command]) == 0:
                    tf_gpu = True
                    break
            except IOError:  # command does not exist / is not executable
                pass
        if os.environ.get('USE_GPU') == 'True':  # force GPU even if not auto-detected
            tf_gpu = True

    tf_dependency = []
    if install_tf:
        tf_dependency = ['tensorflow>=2.10.1,<2.13.0'] if tf_gpu else ['tensorflow>=2.10.1,<2.13.0']
        if tf_gpu:
            print("A GPU was detected, tensorflow-gpu will be installed")

    return tf_dependency
    
# This call to setup() does all the work
setup(
    name="OpenNLP",
    packages=[package for package in find_packages() if package.startswith('opennlp')],
    include_package_data=True,
    package_data={'OpenNLP': ['requirements.txt', 'version.txt']},
    install_requires=['textblob==0.17.1',
                        'nltk==3.8.1',
                        'torch==2.1.0',
                        'requests==2.31.0',
                        'scikit-learn==1.3.1',
                        'pandas==2.1.1',
                        'transformers==4.33.2',
                        'matplotlib==3.8.0',
                        'peft==0.5.0',
                        'seaborn==0.13.0',
                        'torchmetrics==1.2.0',
                        'bitsandbytes==0.41.1',
                        'tensorflow==2.10.1',
                        'keras-preprocessing==1.1.2',
                        'keras==2.10.0'] + find_tf_dependency(),               
     extras_require={'dev': ['pytest', 
                             'pytest-cov', 
                             'pytest-env', 
                             'pytest-xdist', 
                             'pytype', 
                             'sphinx', 
                             'nbsphinx', 
                             'sphinx-autobuild', 
                             'sphinx-rtd-theme',
                             'sphinxcontrib.bibtex',
                             'docformatter']},   
    
    description="OpenNLP: A Natural Language Processing Package for Classification Problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aims-umich/OpenNLP.git",
    author="Artificial Intelligence and Multiphysics Simulations lab (AIMS) at University of Michigan",
    author_email="radaideh@umich.edu",
    entry_points={
        "console_scripts": [
            "opennlp=opennlp.scripts:main ",
        ]
    },
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"],
    version= __version__,
)
