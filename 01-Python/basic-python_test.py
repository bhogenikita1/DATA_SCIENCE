# -*- coding: utf-8 -*-
'''Write a python program to print all even numbers from a given list of
numbers in the same order and stop printing any after 237 in the sequence.
Sample numbers list:
numbers = [ 
 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 
950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 
843, 831, 445, 742, 717, 958,743, 527]
'''
#==>
list=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 
328, 615, 953, 345, 
 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 
950, 626, 949, 687, 217, 
 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 
843, 831, 445, 742, 717, 958,743, 527]
for list in list:
    if list==237:
        break
    if list%2==0:
        print(list)
    



'''Q2. Write a python program to find a list of integers with exactly two 
occurrences of nineteen and at least three occurrences of five. Return True 
otherwise False.
e.g. Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
'''
list=[19,19,15,5,3,5,5,2]
if list.count(19)==2:
   print(True)
else:
    print(False)


'''Q3. Write a python program to find numbers that are greater than 10 and have 
odd first and last digits.
e.g: Input:
[1, 3, 79, 10, 4, 1, 39, 62]
Output:
[79, 39]
Input:
[11, 31, 77, 93, 48, 1, 57]
Output:
[11, 31, 77, 93, 57
'''
list=[1,3,79,10,4,1,39,62]
for num in list:
    if num>10:
        print(num)
        
     
    
'''
Q4. Write a python program to find the largest negative and smallest positive 
numbers (or 0 if none).
e.g. Input: 
[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
Output:
[-6, 2]
'''     
list1=[-12,-6,300,-40,2,2,3,57,-50,-22,12,40,9,11,18]
list1
list1.sort()
for i in range (len(list1)):
    if(list1[i+1]>0):
        print(list1[i])
        print(list1[i+1]) 
        break;

''' 5. Write a Python program that matches a string that has an a followed by 
zero or more b's
'''
str=["abcd0","qutetuwe","fhiegfwkq","wjhfiuef0","hbegbfiyb"]
for str in str:
    if "0" in str or "b" in str:
        print(str)
print(str)    





