# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:17:38 2024

@author: ADMIN
"""
#####################################################
import numpy as np
from numpy import array
from scipy.linalg import svd
A=array([[1,0,0,0,2],[0,0,3,0,0],[0,0,0,0,0],[0,4,0,0,0]])
print(A)

#SVD
U,d,Vt=svd(A)
print(U)
print(d)
print(Vt)
print(np.diag(d))

#SVD Applying to a dataset
import pandas as pd
data=pd.read_excel("C:/Data Set/University_Clustering.xlsx")
data.head()
data=data.iloc[:,2:]#removes non numeric data
data

from sklearn.decomposition import TruncatedSVD
svd=TruncatedSVD(n_components=3)
svd.fit(data)
result=pd.DataFrame(svd.transform(data))
result.head()
result.columns="pc0","pc1","pc2"
result.head()
#scatter diagram
import matplotlib.pyplot as plt
plt.scatter(x=result.pc0,y=result.pc1)#Here higher value of pc0 and lower value of pc1.

#########################################################

import pandas as pd
import numpy as np
Univ1=pd.read_excel("C:/Data Set/University_Clustering.xlsx")
Univ1.describe()#Generates descriptive statistics like count, mean, std, etc., for numerical columns.
Univ1.info()#Provides a concise summary of the DataFrame, including data types, non-null counts, and memory usage.
Univ=Univ1.drop(["State"],axis=1)#Drops the "State" column from the DataFrame.
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
Univ.data=Univ.iloc[:,1:]
#normilizing numerical data
uni_normal=scale(Univ.data)
uni_normal


