#    This file is part of OpenNLP.

#    Copyright (c) 2024 University of Michigan's 
#    AIMS (Artificial Intelligence and Multiphysics Simulation) Group
#    OpenNLP is free software: you can redistribute it and/or modify
#    it under the terms of the MIT LICENSE

#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.

#"""
#Created on Mon May 28 08:09:18 2024
#
#@author: Majdi Radaideh
#"""

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)
import os, sys
sys.path.insert(0, './opennlp/')
sys.path.insert(0, './opennlp/custommodel')
sys.path.insert(0, './opennlp/rl/labeling')
sys.path.insert(0, './opennlp/mining')
sys.path.insert(0, './opennlp/preprocessing')
sys.path.insert(0, './opennlp/run')
sys.path.insert(0, './opennlp/trainer')
import argparse
import opennlp
import pytest
from opennlp.version import version


    
simple_example="""
#***************************************************************************
# NEORL Simple Example
# Using DE to minimize the sphere function 
#***************************************************************************
from neorl import DE

#--Define the fitness function
def FIT(individual):
    #Sphere test objective function. 
    y=sum(x**2 for x in individual)
    return -y  #-1 is used to convert min to max

#--Define parameter space (d=5)
nx=5
BOUNDS={}
for i in range(1,nx+1):
    BOUNDS['x'+str(i)]=['float', -100, 100]

#--Differential Evolution
de=DE(bounds=BOUNDS, fit=FIT, npop=60, CR=0.7, F=0.5, ncores=1, seed=1)
x_best, y_best, de_hist=de.evolute(ngen=100, verbose=0)

#--Optimal Results
print('best x:', x_best)
print('best y:', y_best)
#***************************************************************************
"""
  
def main():
    
    logo="""
    
    \t\t\tOpenNLP: An Open Source NLP Package for Sentiment Classification
    \t\t\t ███████╗███████║███████╗███╗   ██╗███╗   ██╗██╗     ███████║                        
    \t\t\t ██║  ██║██   ██║██╔════╝████╗  ██║████╗  ██║██╗     ██   ██║                     
    \t\t\t ██║  ██║███████║██████╗ ██╔██╗ ██║██╔██╗ ██║██╗     ███████║                  
    \t\t\t ██║  ██║██╔════╝██╔═══╝ ██║╚██╗██║██║╚██╗██║██╗     ██╔════╝                      
    \t\t\t ███████║██║     ███████╗██║ ╚████║██║ ╚████║███████╗██║                      
    \t\t\t ═══════╝══╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝══╝                                                                 
    \t\t\t      Copyright © 2023 University of Michigan - Ann Arbor
    \t\t\t   Artificial Intelligence and Multiphysics Simulation Group
    
                           \n"""
    
    logo=logo.encode('utf-8')
                           
    __version__=version()
    path=os.path.dirname(opennlp.__file__)
    parser = argparse.ArgumentParser(description='OpenNLP command line API parser')
    #parser.add_argument('-i', '--input', required=False, help='Name of the input ASCII file, e.g. INPUT.inp, INPUT.dat (required arg)')
    #parser.add_argument('-c', '--check', help="check input file syntax and exit")
    parser.add_argument('-t', '--test', action='store_true', help="run OpenNLP units tests")
    parser.add_argument('-e', '--example', action='store_true', help='print a simple OpenNLP script and exit')
    parser.add_argument('-v', '--version', action='version', version='NEORL-'+__version__)
    args = parser.parse_args()
    
    if args.example:
        print(simple_example)
        sys.exit(0)
        
    if args.test:
        pytest.main(["-x", path, "-v", "--continue-on-collection-errors", "--maxfail=10"])
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(0)
    
    print("--debug: All modules are imported sucessfully")
    print ("--------------------------------------------------------------- ")