"""
            EX 2. Running Neural Network models using OpenNLP

This is an tutorial for Neural Network for NLP.
OpenNLP includes LSTM and MLP. 
1. LSTM 
2. MLP
3. CNN
"""

# Import dependencies 
from opennlp.run.nn import _LSTM, MLP, CNN


# Create an instance from LSTM class
lstm=_LSTM(data_path='../data/sample_sentiment.csv',
           user_split=False,
           input_col='tweets',output_col='labels',
           num_epochs=1,num_nodes=30,num_layers=5,bs=32)
# Run LSTM on sentiment dataset
lstm.run_LSTM()

# Create an instance from CNN class
cnn=CNN(data_path='../data/sample_sentiment.csv',
           num_conv=4,
           filter=16,
           kernel=4,
           num_nodes=32,
           num_layers=2,
           bs=8,
           user_split=False,
           input_col='tweets',output_col='labels',
           num_epochs=1)
# Run CNN on sentiment dataset
cnn.run_CNN()

mlp=MLP(data_path='../data/sample_sentiment.csv',
        input_col='tweets',output_col='labels',
        bs=32,
        lr=1e-5,
        user_split=False,
        hidden_layer_sizes=(20,40,60), # 3 Layers, Each layer has 20,40,60 nodes
        max_iter=1000) # Note that MLP does not have epochs, max iteration number will control the training

# Run MLP
mlp.run_MLP()

"""
Results of those models will be saved at './Results/<model name>_<parameters>'
For example, if you run Random forest model with 200 estimators,
Results will be saved in ./Results/LSTM_10layers_30nodes
Results include runtime,confusion matrix,clcassification report and training and validation loss.
"""

