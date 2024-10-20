# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:42:00 2024

@author: HP
"""

###########  9/08/2024  ################

import pandas as pd
import matplotlib.pyplot as plt
#Now import file from data set and create a dataframe
Univ1=pd.read_excel("C:/DataSet/University_Clustering.xlsx")
Univ1
a=Univ1.describe() 
a
#we have coulmn state which will really not useful we will drop it
Univ=Univ1.drop(["State"],axis=1)
Univ
#we know that there is scale diff among the columns
#either by using normalization or stadardization
#whenever there is mixed data use normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now apply this normalization function to Univ data frame
#for all the rows and column from 1 until end
#since 0th column has university name hence skipped
df_norm=norm_func( Univ.iloc[:,1:])
b=df_norm.describe()
b

print(Univ.dtypes)              
#you can check df_norm dataframe which is scaled 
#between values from 0 to 1
#you can apply describe function o new dataframe
b=df_norm.describe()
b
#before you applying clustering you need to apply dendogram first
#now to create dendogram,we need to measure distance, we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage gives us hierarchical or aglomarative clustering
#ref the help for linkage
z=linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8))
plt.title("Hierarchical clustering dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")
#ref help of dendrogram
#sch.dendogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show() 

#applying agglomarative clustering choosing 5 as cluster from dendrogram
#whatever has been
from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',metric="euclidean").fit(df_norm)
#apply labels to the cluster
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#assign this series to Univ DataFrame are column and name the column
Univ['clust']=cluster_labels
#we want to realocate the column 7 to 0 th position
Univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]
#now check the Univ DataFrame

#from the output cluster 2 has got highest top 10

#############    13/08/2024    ##################

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler 
from matplotlib import pyplot as plt
df=pd.read_csv("C:/7-clustering/Income.csv")
df.head()
plt.scatter(df.Age,df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income($)')
km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['Age','Income($)']])
y_predicted
df['cluster']=y_predicted
df.head()
km.cluster_centers_

df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]

plt.scatter(df1.Age,df1['Income($)'],color='Green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.legend()
#we need to go for scaling

#preprocessing using min max scaler
scaler=MinMaxScaler()

scaler.fit(df[['Income($)']])
df['Income($)']=scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age']=scaler.transform(df[['Age']])

df.head()

plt.scatter(df.Age,df['Income($)'])

km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['Age','Income($)']])
y_predicted

df['cluster']=y_predicted
df.head()
km.cluster_centers_

df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]
plt.scatter(df1.Age,df1['Income($)'],color='Green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.legend()


###############   14/08/2024   ################

#WSS- within sum of square
#BSS- between sum of square

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

##let's understand first how k means works for dimentional data
#for that,generate random numbers of 1/50
X=np.random.uniform(0,1,50)
Y=np.random.uniform(0,1,50)

#create an empty  dataFrame with 0 row and 2 columns
df_xy=pd.DataFrame(columns=["X","Y"])
#assign the values of X and Y To these columns
df_xy.X=X
df_xy.Y=Y
df_xy.plot(x="X",y="Y",kind="scatter")
model1 = KMeans(n_clusters=3).fit(df_xy)

'''
Within data apply Kmeans model,generate scatter plot
eith scale/font=10 
cmap=plt.cm.coolwarm:cool color combination
'''
model1.labels_
df_xy.plot(x="X",y="Y",c=model1.labels_,kind="scatter",s=10,cmap=plt.cm.coolwarm)

#########################

Univ1=pd.read_excel("C:/7-clustering/University_Clustering.xlsx")
Univ1.describe()
Univ=Univ1.drop(["State"],axis=1)
#we know that there is scale diff among the columns  which we have either by using normalization /standardization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now apply this normalization funtion to Univ DataFrame for all the columns

df_norm=norm_func(Univ.iloc[:,1:])
df_norm
'''
what will be ideal cluster number,will it be 1,2 or 3
'''
TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    
    TWSS.append(kmeans.inertia_)#total within sum of square
    
    '''
    Kmeans inertia,also known as sum of square Errors(or SSE),
    calculates the sum of the distances of all
    points within cluster from the centroid of the point,
    It is the diff between the observed value and the predicted value
    '''
TWSS
#As k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters");
plt.ylabel("Total_within_SS")

'''
How to select value of k from elbow curve
when k changes from 2 to 3, then decrease in TWSS is higher than when k changes from 3 to 4.
when k value changes from 5 to 6 decreases 
'''
model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ
Univ.iloc[:,2:8].groupby(Univ.clust).mean()
Univ.to_csv("kmeans_university.csv",encoding="utf-8")

Univ.to_csv("kmeans_University.csv",encoding="utf-8")
import os
os.getcwd()
'''
    perform clustering for the crime data and identify the number of clusters
    formed and draw inferences.refer to crime_data.csv dataset.

1.Business Problem
1.1   what is the business objective
    In present scenario criminals are becoming technologically 
    
    
    
1.2 are there any constrints
'''







