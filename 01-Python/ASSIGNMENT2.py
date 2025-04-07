####   ASSIGNMENT 2   ####

#1  Write a program to reverse the order of list

list1=["Nikita","xyz",20,True]
list2=list1[::-1]
list2

#_____________________________


#2 Write a program to check number of occurences of specified elements in the list

list1=["Nikita","Sakshi","Indrayani","Nikita"]
count1=list1.count("Nikita")
count1

#____________________________


#3  Write a program to append  the list1 with list2 in the front


list1=[12,20,23,54,"Nikita"]
list2=[43,65,21,87,"XYZ"]
list1.append(list2)
list1


#__________________________


#4  Write a program to insert new item before the second element

list1=[12,20,23,54,"Nikita"]
list1.insert(0, "xyz")
list1


#__________________________
'''
5  Write a program to remove first occurence of specified elements in the list, 
first you check which number is repeated and then remove it
'''

list1=[12,"Nikita",20,23,54,"Nikita"]
list1.remove("Nikita")
list1



#__________________________

#6 Write a program to check whether an element exist in a tuple or not

tuple1=("Nikita","Sakshi","Indrayani","Chaitali",20)
"abcd" in tuple1    #False
"Nikita" in tuple1   #True
20 in tuple1    #True


#___________________________


#7. Write a program to replace last value of each tuple in list to 100


data = [(1,2,3),(4,5,6),(7,8,9)]
updated_data = [t[:-1] + (100,) for t in data]
print(updated_data)

#_____________________________

#8. Write a program  to add a key and value in the dictionary

dict1={"A":"Apple","B":"Ball","C":"Cat"}
dict1["D"]="Dog"
dict1

#_____________________________

#9. Write a program to concatenate dictionary

dict1={"A":"Apple","B":"Ball","C":"Cat"}
dict2={"D":"Dog","E":"Elephant","F":"Fish"}

dict3={}
for d in (dict1,dict2):
    dict3.update(d)
print("\nConcatenated Dictionary: \n\n" ,dict3)    


# Function to concatenate dictionaries
def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Concatenating dictionaries
concatenated_dict = concatenate_dicts(dict1, dict2, dict3)

# Display the result
print("Concatenated Dictionary:", concatenated_dict)

#_______________________________________

#10. Write a program to create dictionary where the keys are 
    #from 1 to 15 and values from square of the numbers

def dictionary():
    dict1={}
    for i in range(1,16):
        dict1[i]=i**2
    return dict1    
            
dictionary=dictionary()   
dictionary

#without using fubctions 
squared_dict={num: num**2 for num in range(1,16)}
print("Dictionary With Squares: ",squared_dict)

#_____________________________________________


#11. write a program to sum of all values in the dictionary

def dictionary():
    dict1 = {}
    for i in range(1,16):
        dict1[i]=i**2
    return dict1    

def sum_of_values(dictionary):
    return sum(dictionary.values())

squared_dict=dictionary()
total_sum=sum_of_values(squared_dict)

print("Dictionary with squares ",squared_dict)
print("Summ of all values: ",total_sum)




