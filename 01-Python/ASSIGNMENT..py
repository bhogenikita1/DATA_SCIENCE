# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:18:13 2024

@author: HP
"""

#.Write a Python function that takes two lists and returns True 
#if they have at least one common member

a=[1,3,5,4]
b=[10,3,5,7]
def dup(a,b):
    for i in a:
        for j in b:
            if (i==j):
                return True
    return False
print(dup(a,b))

list1=[1,2,3,4,5]
list2=[6,7,8,9,2]
#def to_check():
if (list1==list2):
    print("list are exactly same")
elif(list1!=list2):
    print("TRUE")
else:
    print("")    

#2.Use list comprehension to construct a new list but add 6 to each item.
list=[]
for num in range(0,20):
    list.append(num+6)
print(list)    


#3..Write a Python program to reverse a string. 

a=input("enter the string: ")
print(a[::-1])


#4. Write a Python program to iterate over dictionaries using for loops.

dict={"name":"nikita","year":"sy","division":"A"}
for key,values in dict.items():
    print("%s-%s"%(key,values))

#5. Using dict comprehension and a conditional argument create a dictionary from the current dictionary 
#where only the key:value pairs with value above 2000 are taken to the new dictionary. 

dict={"a":1000,"b":2000,"c":3000,"d":4000,}
di={k: v for k, v in dict.items() if v > 2000}
print(di)


#6. Open the file data.txt using file operations.    
import pandas as pd
a=pd.read_csv("C:/1-python/a.txt")
a

#7. Define a array ,data = array([11, 22, 33, 44, 55]) find 0 th index 4 th index data

data=([11,22,33,44,55])
data[0]
data[4]

#8. Write a Python program to filter a list of integers using Lambda.  
#Original list of integers: 
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
#Even numbers from the said list: 
#[2, 4, 6, 8, 10] 
#Odd numbers from the said list: 
#[1, 3, 5, 7, 9]

list1=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,list1))
print(even)
odd=list(filter(lambda x:x%2!=0,list1))
print(odd)

#9. Write a Pandas program to create the specified columns and rows from a given data frame.
#'name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh'] 
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19] 
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1] 
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] 
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
import pandas as pd
import numpy as np
tech={'name': ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'] ,
      'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] }
row_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
df=pd.DataFrame(tech,index=row_labels)
df

#10. Define a array data = array([11, 22, 33, 44, 55]) and slice it from 1 to 4
array=([11,22,33,44,55])
array[0:4]

#11.1 Write a NumPy program to test if any of the elements of a given array are non-zero. 
import numpy as np
a=np.array([0,0,0,0,0,1])
result=np.any(a)
print(result)


#11.2 Write a Python program to plot two or more lines and set the line markers.
import matplotlib.pyplot as plt
x=[1,4,5,6,7]
y=[2,6,3,6,3]
plt.plot(x,y,color='red',linewidth=3,linestyle='dashdot',marker='o',markerfacecolor='blue',markersize=12)
plt.xlim(1,8)
plt.ylim(1,8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Line with marker")
plt.legend()
plt.show()

#12 Write a Python programming to display a bar chart of the popularity of programming Languages.  
#Sample data:  
#Programming languages: Java, Python, PHP, JavaScript, C#, C++ 
#Popularity: 22.2, 23.7, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt
Programming_languages=["Java","Python","PHP","JavaScript","C#","C++"]
Popularity=[22.2,23.7,8.8,8,7.7,6.7]
plt.bar(Programming_languages,Popularity)
plt.xlabel('Programming_languages')
plt.ylabel('popularity')
plt.title('Popularity of programming languages')
plt.show()

import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 8, 27, 64]

plt.plot(x, y1, marker='o', label='y = x^2')
plt.plot(x, y2, marker='s', label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^2 and y = x^3')
plt.legend()
plt.show()


list=[1,2,-4,-5,3,4,5,6]
if all(list):
    print("there is not a zero")#O/P
else:
    print("zeros are there")
    
list=[1,2,3,0,5,0,6]
if all(list):
    print("there is not a zero")
else:
    print("zeros are there")#O/P
    
#use of any(),if any one non zero values
list=[0,0,0,-1,0,0,1]
if any(list):
    print("there are some nonzero values")
else:
    print("all are zeros")
