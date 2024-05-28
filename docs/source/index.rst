=================================================================
OpenNLP: Natural Language Processing for Classification Problems
=================================================================

OpenNLP is a natural language processing toolkit for classification problems developed by the `Artificial Intelligence and Multiphysics Simulations (AIMS) <https://github.com/aims-umich>`_ group at University of Michigan. This package provides various types of tools, including classical machine learning models, neural networks, and large language models. In our particular case, we used those tool for sentiment detection, but users can leverage this for any classification problem.

The models include classical machine learning models built using `scikit-learn <https://scikit-learn.org/stable/index.html>`_, neural network models built using `Keras <https://keras.io>`_, and large language models including BERT, GPT, and Llama2. Further models will continue to be added as the package evolves. OpenNLP supports the following classifiers:

- Bidirectional Encoder Representations from Transformers (BERT),
- Generative Pre-trained Transformer (GPT-2),
- Large Language Model Meta AI (LLaMA-2),
- Feedforward neural networks or Multilayer Perceptron (MLP),
- Long short-term memory (LSTM),
- Convolutional Neural Networks (CNN),
- Decision Trees,
- Random Forests,
- Gradient Boosting,
- Adaboosting,
- Multinomial Naive Bayes,
- Linear Support Vector Machines,

Additional development and support will be provided through the `OpenNLP repository <https://github.com/aims-umich/OpenNLP.git>`_. Refer to the sections below for more information, including installation, examples, and use. 

--------
Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   dev_guide
   release_notes
   models
   examples
   license

.. _data_refs:

---------------
References
---------------
.. bibliography:: data_refs.bib
   :all:

GitHub repository: https://github.com/aims-umich/OpenNLP.git 
