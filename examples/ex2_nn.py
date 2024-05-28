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
lstm= _LSTM(data_path='../data/sample_sentiment.csv',   #sample dataset in opennlp
           input_col='tweets',            #the header of the input column (usually the text)
           output_col='labels',           #the header of the output column (the discrete label) 
           num_layers=5,                  #number of layers in the LSTM model 
           num_nodes=30,                  #number of nods in each layer 
           bs=32,                         #batch size
           user_split=False,              #if you are providing a seperate test set 
           num_epochs=3)                  #number of training epochs
# Run LSTM on sentiment dataset
lstm.run_LSTM()

# Create an instance from CNN class
cnn=CNN(data_path='../data/sample_sentiment.csv',     #sample dataset in opennlp
        input_col='tweets',         #the header of the input column (usually the text)
        output_col='labels',        #the header of the output column (the discrete label) 
        num_conv=4,                 #number of conv layers
        filter=16,                  #number of filters
        kernel=4,                   #kernel size
        num_layers=2,               #number of dense layers after the conv layers
        num_nodes=32,               #number of nodes in the dense layers        
        bs=8,                       #batch size
        num_epochs=3)               #number of training epochs
# Run CNN on sentiment dataset
cnn.run_CNN()

mlp=MLP(data_path='../data/sample_sentiment.csv',       #sample dataset in opennlp
        input_col='tweets',         #the header of the input column (usually the text)
        output_col='labels',        #the header of the output column (the discrete label) 
        bs=32,                         # batch size
        lr=1e-5,                       #learning rate
        user_split=False,              #if you are providing a seperate test set
        hidden_layer_sizes=(20,40,60), # 3 Layers, the layers 20,40,60 nodes
        max_iter=100)                  #similar to epochs

# Run MLP
mlp.run_MLP()

"""
Results of those models will be saved at './Results/<model name>_<parameters>'
"""

