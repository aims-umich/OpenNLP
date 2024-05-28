==========
Examples
==========

The following are some examples of solving classification problems with OpenNLP using different methods. 
 
---------------------------------------------------------------
Example 1: Sentiment Analysis with Classical Machine Learning
---------------------------------------------------------------

This is a binary classification problem of detecting the sentiment from texts collected from Twitter. The sentiment can be either positive or negative. The problem is solved using variety of classical machine learning classifiers. 

Summary
^^^^^^^^^^^^^^^^^^^^^^^^

- Input: Text from Twitter. 
- Output: Two labels of Positive (1) or Negative (0).
- Algorithm: Decision Tree, Random Forests, Gradient Boosting, Adaboost, Naive Bayes, Linear Support Vector
- Field: Sentiment Classification
 
Script
^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude :: ./examples/ex1_ml.py
   :language: python
   

---------------------------------------------------------------
Example 2: Sentiment Analysis with Neural Network Classifiers
---------------------------------------------------------------

This is a binary classification problem of detecting the sentiment from texts collected from Twitter. The sentiment can be either positive or negative. The problem is solved using neural network models such as long short-term memory (LSTM), convolutional neural network (CNN), and multilayer perceptron (MLP).  

Summary
^^^^^^^^^^^^^^^^^^^^^^^^

- Input: Text from Twitter. 
- Output: Two labels of Positive (1) or Negative (0).
- Algorithm: LSTM, CNN, MLP.
- Field: Sentiment Classification
 
Script
^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude :: ./examples/ex2_nn.py
   :language: python
   
---------------------------------------------------------------
Example 3: Sentiment Analysis with Large Language Models
---------------------------------------------------------------

This is a binary classification problem of detecting the sentiment from texts collected from Twitter. The sentiment can be either positive or negative. The problem is solved using large language models.  

Summary
^^^^^^^^^^^^^^^^^^^^^^^^

- Input: Text from Twitter. 
- Output: Two labels of Positive (1) or Negative (0).
- Algorithm: BERT, GPT-2, Llama2.
- Field: Sentiment Classification
 
Script
^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude :: ./examples/ex3_LLM.py
   :language: python