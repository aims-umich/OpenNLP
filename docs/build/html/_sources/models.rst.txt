.. _models:

==========================
Model Dictionary Templates
==========================

This page includes templates for defining NLP models supported by the OpenNLP. The parameters of the dictionaries are set to their defaults.

--------------------------
Neural Network Templates
--------------------------

**LSTM**

.. code-block:: python

	_LSTM(data_path='/path/to/data.csv',
	           user_split=False,
	           input_col='tweets',
	           output_col='labels',
	           num_epochs=10,
	           num_nodes=30,
	           num_layers=5,
	           bs=32)

**CNN**

.. code-block:: python

	CNN(data_path='/path/to/data.csv',
	           num_conv=4,
	           filter=16,
	           kernel=4,
	           num_nodes=32,
	           num_layers=2,
	           bs=8,
	           user_split=False,
	           input_col='tweets',
	           output_col='labels',
	           num_epochs=10)

**MLP**

.. code-block:: python

	MLP(data_path='/path/to/data.csv',
	        input_col='tweets',output_col='labels',
	        bs=32,
	        lr=1e-5,
	        user_split=False,
	        hidden_layer_sizes=(20,40,60),
	        max_iter=1000)

-------------------------------
Large Language Model Templates
-------------------------------

**BERT**

.. code-block:: python

	BERT(data_path='/path/to/data.csv',
	          input_col='tweets', 
	          output_col='labels',
	          user_split=False,
	          num_class=2)

**GPT**

.. code-block:: python

	GPT(data_path='/path/to/data.csv',
	          input_col='tweets', 
	          output_col='labels',
	          user_split=False,
	          num_class=2)

**Llama**

.. code-block:: python

	Llama(data_path='/path/to/data.csv',
	          input_col='tweets', 
	          output_col='labels',
	          user_split=False,
	          num_class=2)
	          
--------------------------
Classical ML Templates
--------------------------

.. code-block:: python

	classical_ml=ClassicalML(data_path='/path/to/data.csv', 
	                         input_col='tweets', 
	                         output_col='labels',
	                         seed=42)

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