""" 
            Ex 1. Running Classical ML Models using OpenNLP

OpenNLP provides variety of classical machine learning tools. In this example, we use: 
1. Decision Trees
2. Random Forests 
3. Multinomial Bayesian classification model
4. Gradient Boosting 
5. Adaboost 
6. Linear SVC
"""

# Import denpendencies 
from opennlp.run.ml import ClassicalML

# Create an instance from the class
# Test size is set as 0.2 (Default), user can change it. 
classical_ml=ClassicalML(data_path='../data/sample_sentiment.csv',  #sample dataset in opennlp
                         input_col='tweets',   #the header of the input column (usually the text)
                         output_col='labels', #the header of the output column (the discrete label)
                         seed=42) # Your random seed

# Run Decision Tree
classical_ml.run_DecisionTree()

# Run random forest
classical_ml.run_RandomForest(n_estimators=10)

# Run MNB
classical_ml.run_MNB(alpha=1.0)

# Run Gradboost
classical_ml.run_GradBoost(n_estimators=10)

# Run Adaboost
classical_ml.run_AdaBoost(n_estimators=10)

# Run SVC
classical_ml.run_SVC()

"""
Results of those models will be saved at './Results/<model name>_<parameters>'
For example, if you run Random forest model with 200 estimators,
Results will be saved in ./Results/RandomForest_estimator200
Results include runtime,confusion matrix and clcassification report.
"""