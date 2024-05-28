""" 
            Ex 3. Fine Tuning Large Language Models using OpenNLP(Single GPU)

OpenNLP provides handy fine tuning tools for 3 LLMs.  
1. BERT - Lightest
2. GPT - Moderate
3. Llama - Massive
Runtime of the model will be proportional to the number of parameters.
"""

from opennlp.run.LLM import BERT,GPT,Llama

#Loading Llama using Token from Mohammed's (malradai) hugging face
from huggingface_hub import login
login(token='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')

# user inputs
data_path='../data/sample_sentiment.csv'    #sample dataset in opennlp
input_col='tweets'                          #the header of the input column (usually the text)
output_col='labels'                         #the header of the output column (the discrete label) 
epochs=1                    #number of epochs, increase to 5 for better performance
bs=32                       #batch size
lr=1e-5                     #learning rate

# Create instances from the classes.
bert=BERT(data_path=data_path,
          input_col=input_col, 
          output_col=output_col,
          user_split=False,   #if you are providing a seperate test set 
          num_class=2)        #positive (1) and negative (0) 

gpt=GPT(data_path=data_path,
          input_col=input_col, 
          output_col=output_col,
          num_class=2)        #positive (1) and negative (0) 

llama=Llama(data_path=data_path,
          input_col=input_col, 
          output_col=output_col,
          num_class=2)        #positive (1) and negative (0) 

bert.run_BERT(epochs=epochs,
              bs=bs,
              lr=lr,
              save_every=1)

gpt.run_GPT(epochs=epochs,
              bs=bs,
              lr=lr,
              save_every=1)      #save the model weights every epoch(s)

#Llama is a bit expensive, uncomment this if you have a very good GPU

#llama.run_LLAMA(epochs=epochs,
#              bs=8,
#              lr=lr,
#              save_every=1)
