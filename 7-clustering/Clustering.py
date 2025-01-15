# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:38:37 2024

@author: HP
"""
'''
Statistics
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:/DataSet/crime_data.csv")
df.head()
df.describe()
df.columns
set(df['Murder'])
#continous data
set(df['Assault'])
#continous data
set(df['UrbanPop'])
#continous data
df.iloc[:5,:4]  #include all columns and rows
df.iloc[:5,3:] #include columns 3,4 with all rows

df=pd.read_csv("C:/DataSet/crime_data.csv",names=["Murder","Assault"],skiprows=[0])
df
df.Murder.quantile(0)
df.Murder.quantile(0.25)
df.Murder.quantile(0.75)
df.Murder.quantile(1)

percentile_99=df.Murder.quantile(0.99)
percentile_99

df_no_outlier=df[df.Murder<=percentile_99]
df_no_outlier

df.Murder[3]=np.NAN
df

df.Murder.mean()
# 65.85714285714286

df_new=df.fillna(df.Murder.mean())
df_new

'''                            Murder  Assault
Alabama        13.2 236  58.000000     21.2
Alaska         10.0 263  48.000000     44.5
Arizona        8.1  294  80.000000     31.0
Arkansas       8.8  190  65.857143     19.5
California     9.0  276  91.000000     40.6
Colorado       7.9  204  78.000000     38.7
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df['Assault'].plot(kind='hist',color='pink',bins=20)

df['Murder'].plot(kind='kde')   #density curve
#data is normally distributed according to density curve

df['Murder'].skew()
#-0.2738303530441143==> near about 0 #data is normally distributed

df['Murder'].plot(kind='box')
#as there is no outlier so data is Balancesd 


###########  AGGLOMERATIVE CLUSTERING  ############

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

df=pd.read_csv("C:/DataSet/crime_data.csv")
df

def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_func(df.iloc[:,1:])
df_norm

z=linkage(df_norm,method='complete',metric='euclidean')
#The method used is 'complete' linkage, which considers the 
#maximum distance between points in clusters. 
#The distance metric is Euclidean, which is the straight-line distance between points.
#z=This will contain the linkage matrix, which is used to generate the dendrogram.z

plt.figure(figsize=(15,8))
plt.title=('Heirarchical clustering dendogram')
plt.xlabel=('Index')
plt.ylabel=('Distance')

sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

from sklearn.cluster import AgglomerativeClustering
a=AgglomerativeClustering(n_clusters=3,linkage='complete',metric='euclidean').fit(df_norm)

a.labels_
cluster_label=pd.Series(a.labels_)
df['clust']=cluster_label
df1=df.iloc[:,[5,1,2,3,4]]
df1

############ KMEANS CLUSTERRING ############

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv("C:/DataSet/crime_data.csv")
df

# Step 1: Apply K-Means Clustering
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Murder', 'Assault']])

# Step 2: Add the cluster labels to the DataFrame
df['cluster'] = y_predicted
y_predicted
# Step 3: Visualize the clusters
# Separate the data based on cluster labels
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

# Plot the clusters
plt.scatter(df1.Murder, df1['Assault'], color='orange',label='Cluster 0')
plt.scatter(df2.Murder, df2['Assault'], color='blue', label='Cluster 1')
plt.scatter(df3.Murder, df3['Assault'], color='green',label='Cluster 2')


# Plot the centroids
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], 
            color='purple', marker='*', s=200, label='Centroid')

# Set plot title and labels
plt.title('K-Means Clustering')
plt.xlabel('Murder')
plt.ylabel('Assault')
plt.legend()
plt.show()

#  preprocessing

scaler=MinMaxScaler()
scaler.fit(df[['Murder']])
df['Murder']=scaler.transform(df[['Murder']])

scaler.fit(df[['Assault']])
df['Assault']=scaler.transform(df[['Assault']])

df.head()

plt.scatter(df.Murder,df['Assault'])

# Step 1: Apply K-Means Clustering
km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Murder', 'Assault']])

# Step 2: Add the cluster labels to the DataFrame
df['cluster'] = y_predicted
y_predicted
# Step 3: Visualize the clusters
# Separate the data based on cluster labels
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]


# Plot the clusters
plt.scatter(df1.Murder, df1['Assault'], color='orange',label='Cluster 0')
plt.scatter(df2.Murder, df2['Assault'], color='blue', label='Cluster 1')
plt.scatter(df3.Murder, df3['Assault'], color='green',label='Cluster 2')


plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], 
            color='purple', marker='*', s=200, label='Centroid')

# Set plot title and labels
#plt.title('K-Means Clustering')
plt.title('K-Means Clustering')
plt.xlabel('Murder')
plt.ylabel('Assault')
plt.legend()
plt.show()













