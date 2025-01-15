# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:33:24 2024

@author: HP
"""

#EDA 
#EDA pre-processing

import pandas as pd
#let us import dataset
df=pd.read_csv("C:/5-Data_prep/ethnic diversity.csv.xls")
#let us check datatype of columns
df.dtypes

#salaries data type is float let us convert it into int
#df=df.salaries.astype(int)
df.Salaries=df.Salaries.astype(int)
df.dtypes
#now the dat type of salaries is int
#similarly age daya type must be float
#presently it is int
df.age=df.age.astype(float)
df.dtypes

##################

#identify the duplicates
df_new=pd.read_csv("C:/5-Data_prep/education.csv.xls")
duplicate=df_new.duplicated()
#output of this function is single column
#if there is duplicate records output-True
#if there is no duplicate records output-False
#series will be created
duplicate
sum(duplicate)
#output will be 0
#now let us import another dataset
df_new1=pd.read_csv("C:/5-Data_prep/mtcars_dup.csv.xls")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#there are 3 duplicate records
#row 17 is duplicate of row 2 like wise you can 3 duplicate records
#there is function callled drop_duplicates()
#which will drop all duplicates records
df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2)

######################


#outliers treatment
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/5-Data_prep/ethnic diversity.csv.xls")
#now let us find outliers in salaries
sns.boxplot(df.Salaries)
#there are outilers
#let us check outliers in age column
sns.boxplot(df.age)
#there are no outliers
#let us calculate IQR
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have observed IQR in variable explorer
#no,because IQR is in capital letters treated as constant
IQR









