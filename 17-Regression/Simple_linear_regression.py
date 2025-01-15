# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:44:00 2025

@author: HP
"""

import pandas as pd
import numpy as np
import seaborn as sns
wcat=pd.read_csv("C:/DataSet/wc-at.csv")
wcat
#EDA
wcat.info()
wcat.describe()
#Avg waist is 91.90 and min is 63.50 and max is 121
#avg AT is 101.89 and min 11.44 and max is 253

import matplotlib.pyplot as plt
plt.bar(height=wcat.AT, x=np.arange(1,110,1))
sns.distplot(wcat.AT)
#Data is normal but right skewed
plt.bar(height=wcat.Waist,x=np.arange(1,110,1))
sns. distplot(wcat.Waist)
#Data is normal bimodal
plt.boxplot(wcat.Waist)
#No outliers but right skewed

plt.bar(height=wcat.Waist,x=np.arange(1,110,1))
sns. distplot(wcat.Waist)
#Data is normal bimodal


#Bivariant analysis
plt.scatter(x=wcat.Waist,y=wcat.AT)
#Data is linearly scatterd, direction positive, strength:poor
#Now let us checl the correlation coeficient
np.corrcoef(np.log(wcat.Waist).wcat.AT)

#the correlation coefficient is 0.8185<085 hence the correlation is moderate
#let us check the direction of correlation
cov_output=np.cov(wcat.Waist,wcat.AT)[0,1]
cov_output

#635.91, it is positive means correlation will be positive

######################

#let us apply to various models and check feasibility

import statsmodels.formula.api as smf
#First simple linear model
model=smf.ols('AT~Waist',data=wcat).fit()
#Y is AT  and X is waist
model.summary()

#R-squared=0.67<0.85, there is scope of improvement
#p=00<0.05,hence acceptable
#bita-0=215.98
#bita-1=3.45
pred1=model.predict(pd.DataFrame(wcat.Waist))
pred1

#Regression line
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred1,'r')
plt.legend(['Predicted Line','Observed data'])
plt.show()

###########
res1=wcat.AT-pred1
np.mean(res1)
res_sqr1=res1*res1
mse1=np.mean(res_sqr1)
rmse=np.sqrt(mse1)
rmse
#Out[63]: 32.760177495755144

#let us try another model
#x=log(Waist)
plt.scatter(x=np.log(wcat.Waist),y=wcat.AT)
#Data is linearly scatterd,direction positive , strenght:poor
#now let us check the correlation coefficient

np.corrcoef(np.log(wcat.Waist),wcat.AT)

model2=smf.ols('AT~np.log(Waist)',data=wcat).fit()
#Y is AT  and X is waist
model2.summary()

#R-squared=0.675<0.85, there is scope of improvement
#p=00<0.05,hence acceptable
#bita-0=1328.3420
#bita-1=np.log(Waist) 317.1356
pred2=model2.predict(pd.DataFrame(wcat.Waist))
pred2

#Regression line
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred2,'r')
plt.legend(['Predicted Line','Observed data_model2'])
plt.show()

res2=wcat.AT-pred2
np.mean(res2)
res_sqr2=res2*res2
mse2=np.mean(res_sqr2)
rmse=np.sqrt(mse2)
rmse

#32.49








import pandas as pd
import numpy as np
import seaborn as sns
wcat=pd.read_csv("C:/DataSet/wc-at.csv")
# EDA
wcat.info()
wcat.describe()
#Average waist is 91.90 and min is 63.50 and max is 121
# Average AT is 101.89 and min is 11.44 and max is 253
import matplotlib.pyplot as plt
plt.bar(height=wcat.AT,x=np.arange(1,110,1))
sns.distplot(wcat.AT)
# Data is normal but right skewed
plt.boxplot(wcat.AT)

plt.boxplot(wcat.AT)
# no outliers but right skewsd
plt.bar(height=wcat.Waist,x=np.arange(1,110,1))
sns.distplot(wcat.AT)

# data is normal binomial
plt.boxplot(wcat.AT)
plt.bar(height=wcat.Waist,x=np.arrange(1,110,1))
sns.distplot(wcat.Waist)
# data is bidonomial
############################
# bivariant analysis
plt.scatter(x=wcat.Waist,y=wcat.AT)
# data is linearly scatterd,direction postive,strength:poor
# now let us check dirction of correletion
np.corrcoef(wcat.Waist,wcat.AT)
# the corrlection coefficienyt is 0.8185<0.85 hence
# the correlction is moderate
# let us check the direction of correlction
cov_output=np.cov(wcat.Waist,wcat.AT)[0,1]
cov_output
#635.91,it is postive means correlation will postive
#################################################
# let us apply to various model and check the feasiblity
import statsmodels.formula.api as smf
# first simple linear model
model=smf.ols('AT~Waist',data=wcat).fit()
#  Y is AT and x is waist
model.summary()
# r-squarred-0.67<0.85,there is scope of imporvement
# p=0<0.05 hence acceptable
# bita-0=-215.98
# bitA -1=3.45
pred1=model.predict(pd.DataFrame(wcat.Waist))
pred1
##############################
# Regression line
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred1,'r')
plt.legend(['Predicted line','Observed data'])
plt.show()
####################
## error calculations
res1=wcat.AT-pred1
np.mean(res1)
res_sqr1=res1*res1
mse1=np.mean(res_sqr1)
rmse1=np.sqrt(mse1)
rmse1
#32.76
#######################
# let us try another model
# x=log(waist)
plt.scatter(x=np.log(wcat.Waist),y=wcat.AT)
# data  is linerlay scatterd,direction postively,streghth:poor
# now let us check the correlation coefficient
np.corrcoef(np.log(wcat.Waist),wcat.AT)
# the correlation coefficent is 0.8185
#
model2=smf.ols('AT~np.log(Waist)',data=wcat).fit()
#
model2.summary()
#
#
#
#
pred2=model.predict(pd.DataFrame(wcat.Waist))
pred2
##########################




###### 03/01/2025 ######
import matplotlib.pyplot as plt
# Now let us try another model

# Now let us make Y=log(AT) and X=Waist, X*X=Waist.Waist
# polynomial model
# Here r cannot be calculated
model4 = smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
# Y is log(AT) and X=Waist

model4.summary()

# R-sqarred = 0.779<0.85, there is scope of improvement
# p  =0.000<0.05 hence acceptable
# bita-0 = -7.8241
# bita-1 = 0.2289

pred4 = model4.predict(pd.DataFrame(wcat.Waist))
pred4
pred4_at = np.exp(pred4)
pred4_at
###############################
# Regression line
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist,pred4,'r')
plt.legend(['Predicted line','Observed data_model3'])
plt.show()
##############################

# error calculations
res4 = wcat.AT-pred4_at
res_sqr4 = res4*res4
mse4 = np.mean(res_sqr4)
rmse4 = np.sqrt(mse4)
rmse4
#32.24


#we have to generalize the best model

from sklearn.model_selection import train_test_split

train,test=train_test_split(wcat,test_size=0.2)
plt.scatter(train.Waist,np.log(train.AT))
plt.scatter(test.Waist,np.log(test.AT))
final_model=smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
#Y is log(AT) and X=Waist
final_model.summary()

# R-sqarred = 0.779<0.85, there is scope of improvement
# p  =0.000<0.05 hence acceptable
# bita-0 = -7.8241
# bita-1 = 0.2289


test_pred=final_model.predict(pd.DataFrame(test))
test_pred_at=np.exp(test_pred)
test_pred_at

################

train_pred=final_model.predict(pd.DataFrame(train))
train_pred_at=np.exp(train_pred)
train_pred_at

################

#Evaluation on test data
test_res=test.AT-test_pred_at
test_sqr=test_res*test_res
test_mse=np.mean(test_sqr)
test_rmse=np.sqrt(test_mse)
test_rmse

#26.882118

#Evaluation on train data
train_res=train.AT-train_pred_at
train_sqr=train_res*train_res
train_mse=np.mean(train_sqr)
train_rmse=np.sqrt(train_mse)
train_rmse

#33.464601

#test_rmse>train_rmse





