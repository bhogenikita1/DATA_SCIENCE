# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:42:13 2024

@author: HP
"""

####  10/09/2024   #####

#Data Aquisition==> Text extraction & cleanup==> Preprocessing==> 
#Featues Engineering==> Model Building==> Evaluation=>Deployment==> Monitor & Update

# Word to vector=> Establish relation between two words


#pip install gensim
#pip install python-Levenshtein
import gensim
import pandas as pd
df=pd.read_json("C:/8-textmining/textmining/Cell_Phones_and_Accessories_5.json",lines=True)
df
df.shape
#simple Preprocessing & Tokenization
review_text=df.reviewText.apply(gensim.utils.simple_preprocess)
review_text

#let us check first word of each review
review_text.loc[0]

#let's check first row of DataFrame
df.reviewText.loc[0]

#training the word2vec model
model=gensim.models.Word2Vec(
       window=10,
       min_count=2,
       workers=4,
) 
model
'''Where window is how many words you are going to consider
as sliding window you can choose any count
min_count-there must min 2 words in each sentence
workers:no.of threads
'''

#build vocabulary
model.build_vocab(review_text,progress_per=1000)
#progress per: after 1000 words it shows progress Train the word2vec model it will take time have patience
model.train(review_text,total_examples=model.corpus_count,epochs=model.epochs)
#save the model
model.save("C:/8-textmining/textmining/word2vec-amezon-cell-accessories- reviws-short.model")

#finding similar words and similarity between words
model.wv.most_similar("bad")
model.wv.similarity(w1="cheap",w2="inexpensive")
model.wv.similarity(w1="great",w2="good")












