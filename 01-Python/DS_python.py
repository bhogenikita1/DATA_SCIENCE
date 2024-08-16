# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:16:37 2024

@author: HP
"""

##############2/04/2024###################

print("nikita")
#python for data science
#pandas-[series]
#numpy 
#matpylib 
#pandas series like a column in a table
#a series is used to model one dimentional array holding data of any type
#similar to list in python
#the series object also has a few more bits of data, including an
#index(it is in the form of string, dates shouldn't in float) and a name
import pandas as pd
songs2=pd.Series([150,145,35,90],name='counts')
#it is easy to inspect the index of a series(or data)
songs2.index
songs2
songs3=pd.Series([150,145,35,90],name='counts',index=['nikita','anisha','ishwari','aaditi'])
songs3.index
songs3

import pandas as pd
f1=pd.read_csv('age (1).csv')
f1
df=pd.read_excel("C:/1-python/Bahaman.xlsx")
df

import numpy as np
numpy_ser=np.array([150,145,35,90])
songs3[1]
numpy_ser[1]
songs3.mean()
numpy_ser.mean()

################################

george=pd.Series([10,7,1,22],index=['1968','1969','1970','1971'])
george
#reading or select the data from the series
george['1968']
george['1969']
george['1970']
george['1971']
for item in george:
    print(item)

###################03/04/2024######################

#DELETION
#THE DELETTION STATEMENT APPEARS TO HAVE PROBLEMS WITH DUPLICATE INDEX

import pandas as pd
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s
 
 #CONVERT TYPES
 #String use.astype(str)
 #numeric use pd.to_numeric
 #integer use.astype(int),

 #import pandas as pd
songs_66=pd.Series([3,None,11,9],index=['george','ringo','john','paul'],name='Counts')
songs_66.dtypes
songs_66
#dtypes('float64')

pd.to_numeric(songs_66.apply(str))
#there will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
#if we pass errors='coerce' we can see it support to many formats
songs_66.dtypes 

################################

#dealing with none
#the .fillna method will replace them with a given values

import pandas as pd
songs_66=pd.Series([3,None,11,9],index=['george','ringo','john','paul'],name='Counts')
songs_66.dtypes
songs_66=songs_66.fillna(-1)
#pd.to_numeric(songs_66.fillna(str))
#songs_66=songs_66.apply(str)
songs_66=songs_66.astype(int)
songs_66.dtypes
songs_66

#the nan values can be droped from 
#the series using .dropna
songs_66=pd.Series([3,None,11,9],index=['george','ringo','john','paul'],name='Counts')
songs_66=songs_66.dropna()
songs_66

#Append,combining and joining the two series
songs_69=pd.Series([7,16,21,39],index=['nikita','akshata','anisha','aaditi'],name='Counts')
#to concatenate two series together, simply use the .append()
songs=pd.concat([songs_66,songs_69])
songs

#search on google
#songs=songs_66.append(songs_69)
#songs

#ploting series
import pandas as pd 
import matplotlib.pyplot as plt
songs_69=pd.Series([7,16,21,39],index=['nikita','akshata','anisha','aaditi'],name='Counts')
#instead of writing matplotlib.pyplot we can access by using plt
#there is pyplot block inside matplot package
fig=plt.figure()
songs_69.plot()
plt.legend()


songs_66=pd.Series([3,None,11,9],index=['george','ringo','john','paul'],name='Counts')
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()


#import pandas as pd
import numpy as np
data=pd.Series(np.random.randn(500),name='500_random')
fig=plt.figure()
ax=fig.add_subplot(111)
#search it on google->subplot(111)
data.hist()
#hist means histograph


##################04/04/2024#########################

#pandas dataframe is a two data structure
#Data frame features
#it supports named rows and columns
#step 1-go to the anaconda navigator
#step-2 select environmenatl tab
#step-3by default it will be base terminal
#step-4on base terminal-pip install pandas
#or conda install pandas
####
#upgrade pandas to latest or specific version on base terminal

#to check the version of pandas
import pandas as pd
pd.__version__

#create using constructor
#create pandas dataframe using list
import pandas as pd
technologies=[["Spark",20000,"30days"],["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)

##############################

#since we have not given names to coumn and indexes, 
#DataFramese by default assign
#incremenatl sequence numbers as labels
#to both rows and columns, these are called index
#add column & row labels to DataFrames
column_names=["Cources","fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

####
df.dtypes
####
#you can also custom data types to columns
#seet custom types to dataframes
import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
df
print(df.dtypes)


#convert all types to best possible types
#object->string
df2=df.convert_dtypes()
print(df2.dtypes)
#change all column to same type
#string->object
df=df.astype(str)
print(df2.dtypes)


#change type for one or multiple columns
df=df.astype({"fee":int,"Discount":float})
print(df2.dtypes)


#covert data type for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=['fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes


#ignore errors
df=df.astype({"Courses":int},errors="ignore")
df.dtypes

#Generates error
df=df.astype({"Courses":int},errors="raise")
df.dtypes

#converts feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df["Discount"]=pd.to_numeric(df["Discount"])
df.dtypes

##############
#create dataframe from dictionary
import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df=pd.DataFrame(technologies)
df
#convert DataFrame to csv
df.to_csv("data_file.csv")
#############

#create DataFrame from csv file
import pandas as pd
df=pd.read_csv("data_file.csv")
#############
#pandas DataFrame _basic operations
#create DataFrame with None/Null to work with examples

import pandas as pd
import numpy as np
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

##################05/04/2024######################

#DataFrame properties
import pandas as pd 
import numpy as np
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
##############
df.shape
#(7,4)
df.size
#(28)
df.columns
df.columns.values
df.index
df.dtypes
df.info

#understanding buissness
#data dictionary
#exploronary data analysis(EDA)
#data processing
#model
#performance evaluation
#deploy
#monitoring and maintaining


################
#Accessing one columns contents
df['fee']
#Accessing two columns contents
#method 1
cols=['fee','Duration']
df[cols]
#method 2
df[['fee','Duration']]
#select certain rows and assign it to another DataFrame
df2=df[6:]
df2
#
#df[rows,columns]
df[3:4]
#
df2=df[:2]
df2
df2=df[ :7]
df2
#rows from 0 to 5
df2=df[:6]
df2
#6th row
df2=df[6:]
df2
#all rows
df[:]
df['Duration'][0]
df['Discount'][5]
#substracting specific value
df['fee']=df['fee']-500
df['fee']
df['Discount']=df['Discount']+5
df['Discount']
df[:]
#pandas to manipulate to DataFrame
#Describe DataFrame
#Describe DataFrame for all numeric columns
df.describe()
#it will show 5 number summary

#########################
#rename()-Renames pandas DataFrames to columnms
df=pd.DataFrame(technologies,index=row_labels)
df
df.columns=['A','B','C','D']
df

##################
import pandas as pd
df=pd.DataFrame(technologies,index=row_labels)
df.columns=('A','B','C','D')
#FOR ROWS AXIS=0,,,,FOR COLUMNS AXIS=1
df2=df.rename({'A':'C1','B':'C2'},axis=1)
df2
df2=df.rename({'C':'C3','D':'C4'},axis=1)
df2
df2=df.rename(columns={'A':'C1','B':'C2'})
df2



####################
import pandas as pd
df=pd.DataFrame(technologies,index=row_labels)
df.columns=('A','B','C','D')
#FOR ROWS AXIS=0,,,,FOR COLUMNS AXIS=1
df2=df.rename({'r0':'C1','r1':'C2'},axis=0)
df2
df2=df.rename({'r3':'C3','r4':'C4'},axis='rows')
df2
df2=df.rename(columns={'r0':'C1','r2':'C2'})
df2

################
#drop rows by labels
df1=df.drop(['r1','r2'])
df1
#delete rows by posion/index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1
#delete rows by index range
df1=df.drop(df.index[2:])
df1
df1=df.drop(df.index[:2])
df1
#when you have defualt indexs for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0)#it will delete rows 0 and row3
df1
df1=df.drop(range(0,2))#it will delete 0 and 1
df1
#mean->
#median->
#std deviation->


#####10/04/2024#####



#to check version of pandas
import pandas as pd
pd.__version__

import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
print(df)

#explicitely using parameteer name labels
import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df2=df.drop(labels=["fee"],axis=1)
df2
#alternatively u can also use columns instead of labels
df2=df.drop(columns=['fee'],axis=1)
df2
#drop column by index
print(df.drop(df.columns[0],axis=1))
df=pd.DataFrame(technologies)
df
#using inplace=true
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

##########################################
#DROP two or more columns by label name
df2=df.drop(["Courses","fee"],axis=1)
print(df2)

##########################################
#Drop two or more columns by index
df=pd.DataFrame(technologies)
df
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)

############################
#drop columns from list of columns
df=pd.DataFrame(technologies)
print(df.columns)
liscol=['Courses','fee']
df2=df.drop(liscol,axis=1)
print(df2)

#########################
#remove columns from DataFrame inplace
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df

#############################
#pandas select rows by index (position/label)
#accesing rows/columns using INDEX=>iloc is used
#accessing columns using name=>loc

import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

df=pd.DataFrame(technologies,index=row_labels)
#below are quick exampels
#df.iloc[startrow:endrow,startcolumn:endcolumn]
df2=df.iloc[:,0:2]
df2
df3=df.iloc[:,0:1]
df3 

#this line uses the slicing operator to get dataframe items by index
#the first slice operator[:]indicates to return all rows
#the second slice operator specifies that only columns between 0and 2(excluding 2)should be returned

df2=df.iloc[0:2,:]
df2
#in this case, the first slice is[0:2]
#requesting only rows 0 through 1 of the dataframe.
#the second slice[:]indicates that all columns are required

#slicing specifies rows and columns using iloc attribute
df3=df.iloc[1:2,1:3]
df3
#another example
df3=df.iloc[:,1:3]
df3
#the second operator [1:3] yeilds 1 and 3 only
#select rows by integer index
df2=df.iloc[2] #select Row by index
df2

###########12/04/24###############

import pandas as pd
import numpy as np
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
df2=df.iloc[[2,3,6]]#select rows by index list
df2
df2=df.iloc[1:5]#select rows by index integer range
df2
df2=df.iloc[:1]#select first row
df2
df2=df.iloc[:3]#select first 3 rows
df2
df2=df.iloc[-1:]#select last row
df2
df2=df.iloc[-3:]#select last 3 row
df2
df2=df.iloc[::2]#selects alternate rows
df2

#select rows by index labels
df2=df.loc[['r2']]#select row by label
df2
df2=df.loc[['r2','r3','r6']] #select rows by index labels
df2
df2=df.loc['r1':'r5']
df2
df2=df.loc['r1':'r5']   #select rows by label index range
df2
df2=df.loc['r1':'r5':2]#select alternate rows
df2

#####################
#using loc[]to take column slices
#loc[]syntax to slice columns
#df.loc[:,start:stop:step]
#select multiple columns
df2=df.loc[:,['Courses','fee','Duration']]
df2
#select random columns
df2=df.loc[:,['Courses','fee','Discount']]
df2
#select column between two columns
df2=df.loc[:,['fee','Discount']]
df2
df2=df.loc[:,'Discount']
df2
#select columns by range
df2=df.loc[:,'Duration']
df2
#select columns by range
#all the columns upto Duration
df2=df.loc[:,:'Duration']
df2
#select every alternate columns
df2=df.loc[:,::2]
df2

################################
#pandas DataFrame.query()by example
#query all rows with courses equals 'spark'

df2=df.query("Courses=='spark'")
print(df2)
#not equals condition
df2=df.query("Courses!='spark'")
df2

###############################
#pandas add coulmn to DataFrame
#add new column to DataFrame
import pandas as pd
import numpy as np
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
print(df)
tutors=['ram','sham','ghansham','ganesh','ramesh','raj','aaditi']
df2=df.assign(TutorsAssigned=tutors)
df2
 
#############################
MNCCompanies=['TATA','HCL','Infosys','Google','Amazon','Virtusa','Zomato']
df2=df.assign(MNC=MNCCompanies,tutors=tutors)
df2

############################
#derive new column from eisting column
df=pd.DataFrame(technologies)
df2=df.assign(discount_percent=lambda x:x.fee*x.Discount/100)
print(df2)
  
############################
#append column to existing pandas DataFrame
#add new coulumn to the existing DataFrame
df=pd.DataFrame(technologies)
df['MNCCompanies']=MNCCompanies
print (df)

###########################
#ADD NEW COLUMN AT THE SPECIFIC POSITION
df=pd.DataFrame(technologies)
df.insert(0, 'Tutors', tutors)
print(df)

##########################
import pandas as pd
import numpy as np
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
print(df.columns)
df.columns
#pandas rename coulmn name
#rename a single column
df2=df.rename(columns={'Courses':'Courses_list'})
df2.columns
#alternatively we can also write like
df2=df.rename({'Courses':'Courses_list'},axis=1)
df2
df2=df.rename({'Courses':'Courses_list'},axis='columns')
df2
######################################
#inorder to change columns on existing DataFrame
#without copying to new dataframe
#you have to use inplace=true
df.rename({'Courses':'courses_list'},axis=1,inplace=True)
df
#########################################
#rename coulmns with a list
column_names=['Courses','fee','Duration']
df.columns=column_names

###########15/04/2024#################

import pandas as pd
import numpy as np
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
df
#Quick examples of get the rows in dataframe
#count no. of rows in DataFrame

rows_count=len(df.index)  
rows_count
rows_count=len(df.axes[0])
rows_count

#count no. of columns in DataFrame
column_count=len(df.axes[1])
column_count

#######################################
df=pd.DataFrame(technologies)
df
row_count=df.shape[0] #returns no. of rows
row_count
col_count=df.shape[1] #returns no. of columns
print(row_count)
print(col_count)

######################################

#below are quick examples
#using DataFrame.apply()to apply function add column
import pandas as pd
#import numpy as np
data={"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}
df=pd.DataFrame(data)
print(df)
def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
    
############################
#using apply function to single column
def add_4(x):
    return x+4          #adding 4 in that column
df["B"]=df["B"].apply(add_4)
df["B"]
df
############################
#apply to multiple columns
df[['A','B']]=df[['A','B']].apply(add_4)     #adding 4 in both the column
df
#############################
#apply a lambda function to each column
df2=df.apply(lambda x:x+10)
df2
df['A']=df['A'].apply(lambda x:x-2)
df
###########################
#using pandas.DataFrame.transform() to apply function column
#using DataFrame.transform()
def add_2(x):
   return x+2 
df=df.transform(add_2)
print(df)

df['B']=df['B'].transform(lambda x:x/2)
df
##########################

#using pandas.DaraFrame.map() to single column
import pandas as pd
import numpy as np
data={"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}
df=pd.DataFrame(data)
print(df)
df['A']=df['A'].map(lambda A:A/2)
print(df)
 
#########################
#using numpy function on single column
#using DtaFrame.apply & [] operator
import pandas as pd
import numpy as np
data={"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}
df=pd.DataFrame(data)
print(df)
#using numpy function on single column
df['A']=df['A'].apply(np.square)
print(df)

#using numpy function on multiple columns
df[['A','B']]=df[['A','B']].apply(np.square)
df

#######################

#using numpy.square() method on single column
#using numpy.square()and [] operator
df['A']=np.square(df['A'])
print(df)
#numpy function on each column
df=np.square(df)
df
#############################

#pandas groupby() with examples
import pandas as pd
import numpy as np
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","hadoop","spark","pyspark","python"],
              'fee':[20000,25000,26000,22000,24000,21000,22000,35000,45000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days","25days","20days"],
              'Discount':[1000,2000,3000,4000,5000,1200,1300,1400,0]
              }
df=pd.DataFrame(technologies)
df
#use groupby()to compute the sum
df2=df.groupby(['Courses']).sum()
print(df2)
df3=df.groupby(['fee']).sum()
print(df3)

############################

#groupby() for multiple columns
df2=df.groupby(['Courses','Duration']).sum()  #similar data get added
print(df2)

###########################

#add index to the grouped data
#add row index to the grouped by result
df2=df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)

###########################

df.columns
#get the list of all columns names from headers
column_headers=list(df.columns.values)
print("The column header: ",column_headers)

###########################

#using list(df) to get the column headers as a list
column_headers=list(df.columns)
print(column_headers)


###########16/04/2024#############

#pandas shuffle DataFrame rows
import pandas as pd
technologies={'Courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'Duration':["30days","40days","35days","40days","60days","50days","55days"],
              'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
              }
df=pd.DataFrame(technologies)
print(df)
#pandas shuffle DataFrame rows
#shuffle the DataFrame rows return all rows
df1=df.sample(frac=1)
print(df1)
######################
#create new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)
########################
#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)
########################
import pandas as pd
technologies={'Courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,26000,22000],
              'Duration':["30days","40days","35days","50days"],
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies, index=index_labels)
df1

technologies2={'Courses':["spark","java","python","go"],
              'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
df2
#pandas join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

###############
#pandas inner join DataFrames
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)

###############
#pandas left join DataFrame
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)

###############
#pandas right join DataFrame
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)

###############
import pandas as pd
technologies={'Courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,26000,22000],
              'Duration':["30days","40days","35days","50days"],
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies, index=index_labels)
df1

technologies2={'Courses':["spark","java","python","go"],
              'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
df2
#using pandas.merge()
df3=pd.merge(df1,df2)
df3
#using DataFrame.merge()
df3=df1.merge(df2)
df3

###############
#use pandas concat()to concat two DataFrames in vertical manner
import pandas as pd
df=pd.DataFrame({'Courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,24000],
              'Duration':["30days","40days","35days","50days"],
              })
df1=pd.DataFrame({'Courses':["pandas","hadoop","hyperion","java"],
               'Discount':[25000,25200,245000,249000]
               })
 #using pandas.concat()to concat two DataFrame
data=[df,df1]
df2=pd.concat(data)
df2
df2=pd.concat([df,df1])
df2
##################
#concatenate multiple DataFrames Using pandas.concat()
import pandas as pd
df=pd.DataFrame({'Courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,24000],
              })
df1=pd.DataFrame({'Courses':["unix","hadoop","hyperion","java"],
               'fee':[25000,25200,245000,249000]
               })
df2=pd.DataFrame({'Duration':["30days","40days","35days","50days"],
                  'Discount':[25000,25200,245000,249000]
                  })
df3=pd.concat([df,df1,df2])
print(df3)

############18/04/2024##################

import pandas as pd
#read excel file
df=pd.read_excel('C:/1-python/Bahaman.xlsx')
print(df)
#######################

df=pd.DataFrame({'Courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,24000],
              })
df
#using series.values.tolist() 
col_list=df.Courses.values
print(col_list)
col_list=df.Courses.values.tolist()
print(col_list)

#using series.values to list
col_list=df["Courses"].values.tolist()
print(col_list)

#using list function
col_list= list (df["Courses"])
print(col_list)

import pandas as pd
#convert to numpy array
col_list=df['Courses'].to_numpy()
print(col_list)

########################

#what is numpy?
#it is open source python library
import pandas as pd
pd.__pandas__version
#array-can store homogeneous element
#list-can store heterogeneous element
#arrays in numpy
#create ndarray
import numpy as np
arr=np.array([10,20,30])
print(arr)      #in arrray there is no colon between 2 elements
#o/p:
#[10 20 30]
    
################

#create multidimentional array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
#o/p:
#[[10 20 30]
 #[40 50 60]]
 
#represent the minimum dimension
#use ndmin parameter to specify how many minimum dimensions you wanted
#to create an array with minimum dimension
arr=np.array([10,20,30,40],ndmin=4)
print(arr)
#o/p:
#[[[10 20 30 40]]]

##################

#change the data type
#dtype parameter
arr=np.array([10,20,30],dtype=complex)
print(arr)

arr=np.array([10,20,30],dtype=float)
print(arr)

###################

#get the dimensions of the array
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)

###################

#finding the size of each item in array
arr=np.array([10,20,30])
print("Each item contain in bytes:",arr.itemsize)
print(arr)

arr=np.array([[10,20,30,40],[60,70,80,90]])
print("ARRAY SIZE IS:",arr.size)#8
print("ARRAY SHAPE IS:",arr.shape)#(2,4)

#craete numpy array in list
#creation of arrays
arr=np.array([10,20,30])
print("ARRAY:",arr)

###############

#creating  array from list with type float
import numpy as np
arr=np.array([[10,20,40],[30,40,50]],dtype='float')
print("ARRAY CREATETD BY USING LIST:\n",arr)

##################

#create a sequence of integers using arange()
#create a sequence of integers
#from 0 to 20 with steps of 3
arr=np.arange(0,20,3)
print("A sequence array with steps of 3:\n",arr)

###################

#array index in numpy
#accesss single element using index
arr=np.arange(11)
print(arr)
#[ 0  1  2  3  4  5  6  7  8  9 10]  
print(arr[2])
#2
###################
print(arr[-2])#9
print(arr[-5])#6
###################


#indexing with multidimentional array
arr=np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)
print(arr.shape)
print(arr[1,1])#30
print(arr[0,4])#50
print(arr[1,-1])
print(arr[1,-5])

#acces array element using slicing
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]
print(x)
y=arr[0:3]
print(y)
x=arr[-2:10]
print(x)

##############
import numpy as np
multi_arr=np.array([[10,20,10,40],[40,50,70,90],[60,10,70,80],[30,90,40,30]])
multi_arr
#slicing array
#for multidimentional numpy array
#you can access the elements as below
multi_arr[1,2]
multi_arr[1,:]
multi_arr[:,1]
x=multi_arr[:3,::2]
#o/p-[[10 10]
 #[40 70]
 #[60 70]]
   #columns from 0 to 3,
print(x)



###########19/04/24###############


#x=3=>scalar
#x=[10 20 30]=>vector(one dimentional)
#x=[[10 20 30],[15,30,45]]=>matrix(two dimentional)
#x=[[[]]]=>tensor(more that two dimentional)

#integer array indexing
arr=np.arange(14).reshape(2,7)
print(arr)

#boolean array indexing
#when object is of boolean type
import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)
rows=np.array([False,True,True])
rows
wanted_rows=arr[rows, :]
print(wanted_rows)

import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)
rows=np.array([True,False,True])
rows
wanted_rows=arr[rows, :]
print(wanted_rows)


import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)
rows=np.array([False,False,False])
rows
wanted_rows=arr[rows, :]
print(wanted_rows)


####################
list=[20,30,40]
#convert array
array=np.array(list)
print("array:",array)#o/p-array: [20 30 40]
#numpy array properties
#1)ndarray.shape
#ndarray.ndim
#3)ndarray.itemsize
#4)ndarray.size
#5)ndarray.dtype


#1)ndarray.shape=>to get shape of a python numpy array 
#shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)#o/p-(2, 3)


#resize the array
array=np.array([[10,20,30],[40,50,60]])
array
array.shape=(3,2)
print(array)
#o/p-[[10 20]
 #[30 40]
 #[50 60]]
#Reshape
#array=np.array([[10,20,30,40],[50,60,70,80]])


#arithmetic operations on array
arr1=np.arange(16).reshape(4,4)
arr1
arr2=np.array([1,3,2,4])
arr2
#add()
add_arr=np.add(arr1,arr2)
print(f"Adding two arrays:\n{add_arr}")
 
sub_arr=np.subtract(arr1,arr2)
print(f"subtracting two arrays:\n{sub_arr}")


#multiply()
mul_arr=np.multiply(arr1,arr2)
print(f"multiplying two arrays:\n{mul_arr}")

###############

#division()
div_arr=np.divide(arr1,arr2)
print(f"dividing two arrays:\n{div_arr}")

######################

#numpy.resiprocal()
#returns the resiprocal  of arguments by element wise 
#for a element with absolute values larger than 1, 
#the result is always 0

#to perform reciprocal operation
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(f"After reciprocal functions to array:\n{rep_arr1}")

######################
#numpy.power()
#this numpy power (function treats element in the first input array)
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(f"After applying power function to arrray:\n{pow_arr1}")
#[ 27 1000 125]

arr2=np.array([3,2,1])
print("my second array:\n",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"After applying power function to array:\n{pow_arr2}")
########################

#to perform mod function on numpy array
arr1=np.array([7,10,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype
#mod()
mod_arr=np.mod(arr1,arr2)
print(f"After applying mod function to array:\n{mod_arr}")

#########################
#create an empty array
from numpy import empty
a=empty([3,3])
print(a)

###########
#create zero array
from numpy import zeros
a=zeros([3,5])
print(a)
###########
import numpy as np 
np.__version__
############
#create one array
from numpy import ones
a=ones([5])
print(a)

#################

#create array with vstack
from numpy import array
from numpy import vstack
#create first array
a1=array([1,2,3])
print(a1)
#create second array
a2=array([4,5,6])
print(a2)
#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)
#[[1 2 3]
 #[4 5 6]]

####################

#create array with hstack
from numpy import array
from numpy import hstack
#create first array
a1=array([1,2,3])
print(a1)
#create second array
a2=array([4,5,6])
print(a2)

#vertical stack
a3=hstack((a1,a2))#o/p-[1 2 3 4 5 6]
print(a3)
print(a3.shape)

###################  23/04/2024  #####################

#split input and output data
data=array([
    [11,22,33],
    [44,55,66],
    [77,88,99],
    [76,43,67]])
x,y=data[:,:-1],data[:,-1]
x
y

###############

#broadcast scalar to one D array
a=array([11,22,33,44,55,66,77,88])
print(a)
#define scalar
b=2
print(b)
#broadcast
c=a+b
print(c)

################
'''
vector l1 norm
the  l1 norm is calculated as the sum of the absolute vectors values,
where the absolute value of the scalar uses the notation |a|
in effect, the norm is a collection of the Manhattan distance from the
origin of vector space
||v||=|a1|+|a2|+|a3|
'''
from numpy import array
from numpy.linalg import norm
a=array([1,2,3,4,5,6,7,8,9])
#calculate norm
l1=norm(a,1)  #45.0
l1

'''
vector l2 norm
the notation for l2 norm of a vector x is ||x|| power of 2
to calculate the l2 norm of a vector, take the square root of the
sum of the sum of squared vector values 
also called as euclidean distance
this is often used for calculating error in ML models
'''
from numpy import array
from numpy.linalg import norm
a=array([1,2,3])
#calculate norm
l2=norm(a)
l2  # 3.7416573867739413

########################

from numpy import array
from numpy import tril
from numpy import triu
#dfine square matrix
a=array([
        [1,2,3],
        [6,7,8],
        [4,5,10]
        ])
print(a)
#lower triangular matrix
lower=tril(a)
#upper triangular matrix
upper=triu(a)
lower
upper
##################

#diagonal matrix
from numpy import array
from numpy import diag
a=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(a)
d=diag(a)
print(d)

########################

#identity matrix
from numpy import identity
i=identity(5)
print(i)

#########################

#orthognal matrix
'''
the matrix is said to be orthogonal matrix
if the product of a matrix and its transpose give an identity matrix
'''
from numpy import array 
from numpy.linalg import  inv
a=array([
    [1,2],
    [3,4]])
print(a)
V=inv(a)
print(V.T)
I=a.dot(a.T)
print(I)


########### 24/04/2024 ##########


#calculate transpose
from numpy import array
#define matrix
A=array([[1,2],[3,4],[5,6]])
print(A)
#calculate transpose
C=A.T
print(C)

#########################

#INVERSE MATRIX
from numpy import array
from numpy.linalg import inv
A=array([[1.0,2.0],[3.0,4.0]])
print(A)
#inverse matrix
B=inv(A)
print(B)

#multiply A and B
I=A.dot(B)
print(I)

########################

#sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
#create dense matrix
A=array([[1,0,0,1,0,0],
         [0,0,2,0,0,1],
         [0,0,0,2,0,0]])
print(A)
#convert to sparse matrix (CSR method)
S=csr_matrix(A)
print(S)
#reconstruct dense matrix
B=S.todense()
print(B)
###########

#write a python program to draw a line with suitable label
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value*3 for value in X]
print("value of X:")
print(*range(1,50))
'''This is similar to 
i in range(1,50):
    print(i,end='')
'''
print("values of Y(thrice of X):")
print(Y)
#plot lines and /or markers to the Axes
plt.plot(X,Y)
#set the x axis label of the current axis
plt.xlabel('x - axis')
#set the y axis label of the current axis
plt.ylabel('y - axis')
#set the title
plt.title('sample graph!')
#display a graph
plt.show()

##############

#w.a.p. to plot  two or more lines
#on same plot with suitable legendes of each line 
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#plotting the line 1 points
plt.plot(x1,y1,label="line 1")
#plotting the line 2 points
plt.plot(x2,y2,label="line 2")
plt.xlabel('x - axis')
##set the x axis label of the current axis
plt.ylabel('y - axis')

#set the y axis label of the current axis
plt.title('two or more lines on same plot with suitable legend')
#show a legend on the plot
plt.legend()
#display a graph
plt.show
#################
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#plotting the line 1 points
plt.plot(x1,y1,label="line 1")
#plotting the line 2 points
plt.plot(x2,y2,label="line 2")
plt.xlabel('x - axis')
##set the x axis label of the current axis
plt.ylabel('y - axis')
#set the y axis label of the current axis
plt.title('two or more lines on same plot with suitable legend')
#display the figure
plt.plot(x1,y1,color='blue',linewidth=3,label='line1-width-3')
plt.plot(x2,y2,color='red',linewidth=5,label='line1-width-5')

#show a legend on the plot
plt.legend()
#display a graph
plt.show

#############################


import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#plotting the line 1 points
plt.plot(x1,y1,label="line 1")
#plotting the line 2 points
plt.plot(x2,y2,label="line 2")
plt.xlabel('x - axis')
##set the x axis label of the current axis
plt.ylabel('y - axis')
#set the y axis label of the current axis
plt.title('two or more lines on same plot with suitable legend')
#display the figure
plt.plot(x1,y1,color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2,color='yellow',linewidth=5,label='line1-dashed',linestyle='dashed')

#show a legend on the plot
plt.legend()
#display a graph
plt.show



###########25/04/24###########


#EDA-explotary data analysis
#w.a.p. to plot two or more lines
#set the line markers

import matplotlib.pyplot as plt
#x-axis values
x=[1,4,5,6,7]
#y-axis values
y=[2,6,3,6,3]
#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
#set the y limit to the current axis
plt.ylim(1,8)
#set the x limit to the currrent axis
plt.xlim(2,8)
#naming the x-axis
plt.xlabel('x - axis')
plt.ylabel('y -axis')
plt.title('display marker')
plt.show()

###############

#w.a.p to display a bar chart of the popularity of programming language
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,7.7,6.7,8.6]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color='black')
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("Popularity of programming language\n"+"Worldwide, oct 2017 compared to yesr ago")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='white')
plt.show()
 
####################

import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,7.7,6.7,8.6]
x_pos=[i for i, _ in enumerate(x)]
plt.barh(x_pos,popularity,color='pink')
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("Popularity of programming language\n"+"Worldwide, oct 2017 compared to yesr ago")
plt.yticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.show()

######################
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,7.7,6.7,8.6]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color=['black','blue','orange','green','red','purple'])
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("Popularity of programming language\n"+"Worldwide, oct 2017 compared to yesr ago")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='white')
plt.show()

######################
#HISTOGRAM
import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar,rwidth=0.8)#by default number of bins are set to 10
plt.hist(blood_sugar,rwidth=0.5,bins=4)

#####################

'''
histogram showing normal,predaibetic and diabetic patients disr
80-100:normal
100-125:prediabetic
125 onwards:diabetic
'''
plt.xlabel("Sugar level")
plt.ylabel("Number of Patients")
plt.title("Blood Sugar Chart")
plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,color='g')

###################

import matplotlib.pyplot as plt
import numpy as np
#creating dataset
np.random.seed(10)
data=np.random.normal(100,20,200)
fig=plt.figure(figsize=(10,7))
#creating plot
plt.boxplot(data)
#show plot
plt.show()

#########################

import matplotlib.pyplot as plt
import numpy as np
#creating dataset
np.random.seed(10)
data_1=np.random.normal(100,10,200)
data_2=np.random.normal(90,20,100)
data_3=np.random.normal(80,30,200)
data_4=np.random.normal(70,40,200)
data=[data_1,data_2,data_3,data_4]
fig=plt.figure(figsize=(10,7))
#creating axes instance
ax=fig.add_axes([0,0,1,1])
#creating plot
bp=ax.boxplot(data)
#show plot
plt.show()


#############29/04/2024############
import seaborn as sns
import pandas as pd
sales=pd.read_excel("C:/1-python/1-python/Cars.csv")
sales
sales.head()
sales.columns

cars=pd.read_csv("C:/1-python/1-python/Cars.csv")
cars.columns
sns.relplot(x='HP',y='MPG',data=cars)
sns.relplot(x='HP',y='MPG',data=cars,kind='line')

sns.relplot('Sales','Profit',data=sales)
sns.relplot=('Sales','Profit',data=sales,hue='Order')
sns.relplot('Order Date','Sales',data=sales,kind='line')
sns.catplot(x='HP',y='MPG',data=cars,kind='box')

##############################
import pandas as pd
import numpy as np
import seaborn as sns
cars.describe()
###############
#exploratory data analysis
#
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.distplot(cars.HP)
#data is right skewed
plt.boxplot(cars.HP)
#there is no attribute
sns.distplot(cars.MPG)
plt.boxplot(cars.MPG)
#there is no attribute
sns.distplot(cars.MPG)

plt.boxplot(cars.VOL)
#data is slightly left distributed
sns.distplot(cars.SP)
#data is slightly right distributed
sns.distplot(cars.WT)
plt.boxplot(cars.WT)

import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars['MPG'])
#now let us count plot
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])
#count plot shows how many times the each value occured
#92 HP value occured 7 times






















