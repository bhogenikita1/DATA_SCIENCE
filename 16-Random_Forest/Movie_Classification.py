
#### 24/10/2024  ####
#### RANDOM FOREST ALGORITHM  #####

import pandas as pd
df=pd.read_csv("C:/Decision_Tree/movies_classification.csv")
df.info()
#movies classsification data contain 2 columns which are objective hence convert to dummies
df=pd.get_dummies(df,columns=["3D_available","Genre"],drop_first=True)
df
#let us assign input and output variables

predictors=df.loc[:,df.columns!="start_Tech_Oscar"]
predictors
#Except Start_Tech_Oscar. rest all columns are assign as predictors

#predictor has got 20 columns
target=df["Start_Tech_Oscar"]
target
###################

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(predictors,target,test_size=0.2)

###################

#model selection
from sklearn.ensemble import RandomForestClassifier
rand_for=RandomForestClassifier(n_estimators=500,n_jobs=1,random_state=42)
#n_estamators=It is no. of trees in the forest always in range 500 to 1000
#n_jobs=1 means number of jobs running parallel=1 if it is -1 multiple random_state=controls randomness in bootstrapping
#Bootstrapping is getting sample replaced
rand_for.fit(X_train,y_train)
pred_X_train=rand_for.predict(X_train)
pred_X_test=rand_for.predict(X_test)

###

#let us check the performance of the model
from sklearn.metrics import accuracy_score,confusion_matrix
accuracy_score(pred_X_test,y_test)
confusion_matrix(pred_X_test,y_test)


###############

#for taining dataset
accuracy_score(pred_X_train,y_train)
confusion_matrix(pred_X_train,y_train)

#############
