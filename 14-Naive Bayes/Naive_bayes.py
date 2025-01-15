# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:29:05 2024

@author: HP
"""

#Independent and Dependent Event

#Conditional probability


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
#Loading the dataset
email_data=pd.read_csv("sms_raw_NB.csv",encoding="ISO-8859-1")
#These are in test form,open the data frame there are ham or spam
#Cleaning the data
#The function tokenize the text and removes words with fewer than 4 characters
import re
def cleaning_text(i):
    i=re.sub("[^A-Z a-z""]+","",i).lower()
    w=[]
    #every thing else A to Z and a to z is going to space andabs
    #we will take each row and tokenize
    for word in i.split(""):
        if len(word)>3:
            w.append(word)
    return("",join(w))
    #Testing above function with sample text
    cleaning_text("Hope you are having a good week. Just checking in")
    cleaning_text("hope i can understand your felling12321.123.hi how are you")
    cleaning_text("Hi how are you")
#Note the ddataframe size is 5559,2 now removing spaces
#Removing empty rows
email_data=email_data.loc[email_data.text!="",:]
email_data.shape
#You can use count count vectorizer which directly converts a colection of document
#First we will split the data
from sklearn.model_selection import train_test_split
email_train,email_test=train_test_split(email_data,test_size=0.2)
#Splits each email into a list of words.
#Creating matrix of token count for entire dataframe
def split_into_words(i):
    return[word for word in i.split(" ")]
#defining the preparation of email text into word count matrix  format
#CountVectorizer: converts the emails into a matrix of token counts
#.fit():learns the vocabulary from the text ddata
#.transform():converts the text data to token count matrix
email_bow = CountVectorizer(analyzer=split_into_words).fit(email_data.text)
#Defining bow 
all_emails_matrix = email_bow.transform(email_data.text)
train_email_matrix = email_bow.transform(email_train.text)

#For testing messages
test_email_matrix = email_bow.transform(email_test.text)

#learning term weighting and normalizing entire emails
tfidf_transformer = TfidfTransformer().fit(all_emails_matrix)

#Preparing TFIDF for train mails
train_tfidf = tfidf_transformer.transform(train_email_matrix)
train_tfidf.shape

test_tfidf = tfidf_transformer.transform(test_email_matrix)
test_tfidf.shape

###Now apply to Naive Bayes 
from sklearn.naive_bayes import  MultinomialNB as MB
classifier_mb=MB()
classifier_mb.fit(train_tfidf,email_train.type)
# email_train.type : this is the column in training dataset
# (email_train ) that contains the target labels
# which specify wheather each message is spam or ham (non - spam).
#The .type attibute refers to that specific column in the email_train datframe
# training data prepared in term of tfidf and labels of corresponding training data
#Evaluation on test data
test_pred_m=classifier_mb.predict(test_tfidf)
#Calculate accuracy
accuracy_test_m=np.mean(test_pred_m==email_test.type)
accuracy_test_m
#Evaluation on test data accuracy matrix
from sklearn.metrics import accuracy_score
accuracy_score(test_pred_m,email_test.type)
pd.crosstab(test_pred_m,email_test.type)
#Training data accuracy
train_test_m=classifier_mb.predict(train_tfidf)

# calculate accuracy 
accuracy_train_m = np.mean(test_pred_m == email_train.type)
accuracy_train_m
#Accuracy after tuning
from sklearn, metrics import accuracy_score
accuracy_score(test_pred_lap,email_test.type)
pd.crosstab(test_pred_lap,email_test.type)

accuracy_score

# test data( with Laplace Smoothing ): This accuracy is
# computed after applying Laplace smoothing (with alph = 3)
# to the Naive Bayes model.

# Interpretation : smoothing helps avoid issues when encountering 
# words in the text data that were not seen in the training data 
# (zero -frequncy problem)

classifier_mb_lab = MB(alpha= 3)
classifier_mb_lab.fit(train_tfidf, email_train.type)

# accuracy after tunning 

test_pred_lab = classifier_mb_lab.predict(test_tfidf)
accuracy_test_lab = np.mean(test_pred_lab == email_test.type)
accuracy_test_lab
accuracy_score(test_pred_lab, email_test.type)
from sklearn.metrics import accuracy_score
accuracy_score(test_pred_lab, email_test.type)
pd.crosstab(test_pred_lab, email_test.type)
#Training data accuracy
train_pred_lap=classifier_mb_lap.predict(train_tfidf)
accuracy_train_lap=np.mean(train_pred_lap==email_train.type)
accuracy_train_lap

###############  18/10/2024  ################  

'''
Problem statement:-
This Dataset contains information of users in a social network has sevaral business
 clients which can post ads on it.
 One of the client has car company which has jjust Launched a luxury SUV for a ridiculos price.
 Build a Bernoulli Naive Bayes model using this DataSet and classify which of the users of the social network are going to purchase the Luxury SUV.
 1.Implies that there was a purchase and 0 implies there wasn't a purchase

1.Business Problem
1.1.What is the business Objective?
    1.1.1. This will help you to bring those audiences to your website who are intrested in cars.
    And, there will be manyb of those who are planning to buy a car in the near future
    1.1.2. Communicating with your target audiences over social media is always a great way to build a good market reputation.
    Try responding to people's automobile related to queries on Twitter And Facebook pages quickly to be their first choice when it comes to buying a car
1.2.Are thre any constraints?
    Not having a clear marketing or social media strategy may result in reduced benefits for your business
    Additional resources may be needed to manage your online presence

    Social media is immediate and needs daily monitoring
    
    If you don't actively manage your social media presence,you may not see any real benefits
    There is a risk of wantted or inappropriate behavior on your  site including bullying and harassment
    
    Greater exposure online has the potential to  attract risks.
    Risks can include negative feedback information, Leaks or hacking
''' 
'''
#DATA DICTINARY
2.Work on each feature of the dataset to create a data dictinary 
user ID :Integer type which is not contributory
Gender: Object Type need to be label encoding
Age: Integer
EstimatedSalary:Integer
Purchased: Integer Type
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

# Load dataset
car = pd.read_csv("C:/Users/HP/Downloads/NB_Car_Ad.csv")
car

# EDA
print(car.describe())
car.isna().sum()

car.drop(['User ID'], axis=1, inplace=True)

plt.hist(car.Age)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.hist(car.EstimatedSalary)
plt.title('Estimated Salary Distribution')
plt.xlabel('Estimated Salary')
plt.ylabel('Frequency')
plt.show()

# Data Preprocessing
label_encoder = preprocessing.LabelEncoder()
car['Gender'] = label_encoder.fit_transform(car['Gender'])

# Separate the target variable (assuming 'Purchased' is the target column)
target_column = 'Purchased'
X = car.drop(columns=[target_column])  # Input features (Age, EstimatedSalary, Gender)
y = car[target_column]  # Target variable (Purchased)

# Normalize the input features (excluding target)
def norm_func(i):
    return (i - i.min()) / (i.max() - i.min())

X_norm = norm_func(X)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)

# Naive Bayes Model (BernoulliNB)
classifier_bb = BernoulliNB()
classifier_bb.fit(X_train, y_train)

# Predictions
y_pred_b = classifier_bb.predict(X_test)

# Accuracy
accuracy_test_b = np.mean(y_pred_b == y_test)
print("Accuracy:", accuracy_test_b)


#let us now check confusion matrix
 
























































                                                                                                                                         