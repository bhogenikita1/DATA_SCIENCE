# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:44:43 2024

@author: HP
"""

#############

#14/11/2024

import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')
#read csv file
loan_data=pd.read_csv("C:/DataSet/income2.csv")
loan_data.columns
loan_data.head()

#let us split the data in input and output
X=loan_data.iloc[:,0:6]
y=loan_data.iloc[:,6]

#split the datset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#create adaboost classifier
ada_model=AdaBoostClassifier(n_estimators=100,learning_rate=1)

#n_estimators = no. of weak learners
#learning rate, it contributes weights of weak learners, bydefault
#train the model

model=ada_model.fit(X_train,y_train)
#predict the results

y_pred=model.predict(X_test)
print("accuracy",metrics.accuracy_score(y_test,y_pred))
#accuracy 0.8335551233493704

#let us try for  another base model

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
#here base model is changed
Ada_model=AdaBoostClassifier(n_estimators=50, estimator=lr,learning_rate=1)

model=ada_model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print("accuracy",metrics.accuracy_score(y_test,y_pred))
#accuracy 0.8335551233493704

#both model have same accuracy









