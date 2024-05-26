#!/bin/bash

#cd ../neorl/ 
#rm -rf build/
#find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
#python3 setup.py sdist bdist_wheel
#twine check dist/*
#twine upload --username mradaideh --password miar1991 dist/*

mode=$1

source ~/miniconda3/etc/profile.d/conda.sh

if [ $mode == "install" ]; then
  conda create --name testnlp python=3.10 -y
  conda activate testnlp
  pip install .
else
  conda deactivate
  conda remove -n testnlp --all -y
fi

#