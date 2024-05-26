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
#""

import warnings, os
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)

#import tensorflow as tf
#from tensorflow.python.util import deprecation
#tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
#if type(tf.contrib) != type(tf): tf.contrib._warning = None
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#deprecation._PRINT_DEPRECATION_WARNINGS = False

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
try:                    
    print(logo)
except:
    print(logo.encode('utf-8'))
    
    
#from opennlp.mining import api
#from opennlp.preprocessing import data
#from opennlp.custommodel import model
#from opennlp.trainer import trainer
#from opennlp.run import LLM,ml,nn
