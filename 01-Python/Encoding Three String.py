
#Afternoon
############  Encoding Three String  #############
'''
Anand was assigned the task of coming up wiht
an encoding mechanism for any given three strings.
He has come up with the following plan.
'''
'''
Step 1: Splitting each string into Three Parts
Given three input strings, break each string
into threee parts: Front,Middle,End.

Rules for splitting:
If the string length is a multiple of 3, divide it into equal three parts.
If the string length is not a multiple of 3:
If one extra character is present, assign it to the middle part.
If two extra character
'''

'''
Step 2: Concatenation of parts
After splitting , concatenation the corresponding
'''
##########################################################################
#Method 2
s1="John"
s2="Johny"
s3="Janardhan"
lst=[s1,s2,s3]
char_list=[list(word) for word in lst]
for char in char_list:
    n=len(char)
    
    if n%3 == 1:   #1 extra character goes to the middle
          first=char[:1]
          middle=char[1:n-1]   #take all except first
          end=char[n-1:]
          
    elif n%3 == 2:      #1 extra character to first and
        first=char[:2]
        middle=char[2:n-2]    #Middle should take only
        end=char[n-2:]
        
    else: #If n is exactly divisible by 3
        first=char[0:3]
        middle=char[3:6]
        end=char[6:9]        
    print(f"First: {''.join(first)},Middle: {''.join(middle)},End: {''.join(end)}")
##########################################################################
#Method 2
s1 = "John"
s2 = "Johny"
s3 = "Janardhan"
lst = [s1, s2, s3]

# To store the parts of each string
first_parts = []
middle_parts = []
end_parts = []

for word in lst:
    n = len(word)

    if n % 3 == 1:  # 1 extra character goes to the middle
        first = word[:1]
        middle = word[1:n-1]  # Take all except first and last
        end = word[n-1:]

    elif n % 3 == 2:  # 1 extra character to first
        first = word[:2]
        middle = word[2:n-2]  # Take middle part
        end = word[n-2:]

    else:  # If n is exactly divisible by 3
        first = word[:3]
        middle = word[3:6]
        end = word[6:]

    # Append to lists
    first_parts.append(first)
    middle_parts.append(middle)
    end_parts.append(end)

# Concatenating the extracted parts
output1 = ''.join(first_parts)
output2 = ''.join(middle_parts)
output3 = ''.join(end_parts).swapcase()  # Convert case

# Print final outputs
print(output1)
print(output2)
print(output3)
#####################################################################3
    
###########   27/03/2025    ##########

'''
Addition using string : Write a function thhat takes two numbers in string 
format and forms a string containngthe sum (addition) of these two numbers

if input string are '1234' and '56', the output string should be '1290'
if input strings are '56' and '1234',the output string should be '1290'

If input are '123456732128989543219' and '9876126


'''

def add_of_string(num1,num2):
    sum=str(int(num1)+int(num2))
    return sum
add_of_string(1234, 56)

'''

Example 1-

If the series of input numbers are[1237,262,666,140]
we notice that,
0 occurs 1 time
1 occurs 2 
2 occurs
3 occurs
4 occurs
5 occurs
6 occurs
7 occurs 
8 occurs
9 occurs


6 is the digit that occurs 4 times
Thus the most frequent occuring digit in this series is


'''
from collections import Counter

def most_frequent_digit(numbers):
    digit_count=Counter()
    
    #Count occurences of each digit
    for num in numbers:
        digit_count.update(str(num))
        
    #Find the most frequent digits(s)
    max_frequency = max(digit_count.values()) 
    most_frequent = [int(digit) for digit, count in digit_count.items()if count==max_frequency]
   
    return most_frequent, max_frequency
#Example usage
numbers=[1237,262,666,140]
most_frequent,frequency=most_frequent_digit(numbers)

print(f"Most frequent Occuring Digits(s):{most_frequent}")

#___________________________________________________________

def find_digit_to_remove(input1):
    str_num=str(input1)  #Convert number  to string
    
    #Chcek if the number is already palindrome
    if str_num == str_num[::-1]:
        return -1 #No digit needs to be removed
    
    #try removing each digit one by one
    for i in range(len(str_num)):
        new_num=str_num[:i] + str_num[i+1:]
        #Remove digit at index i
        if new_num == new_num[::-1]:
        #check if the new number is the palindrome
            return  int(str_num[i]) #Return the removed digit
    return -1  #If no single digit is removal makes it a palindrome

#Test Cases
print(find_digit_to_remove(12332))

'''   
Given an array with  'N ' elements , you are expected to find the sum of 
the values that are present in non-prime indices of the array

Note: The array index starts with 0, meaning
the position (index) of the first array element is 0
the position of next  array element is 1
And so on....

'''        

def sum_non_prime(input1,input2):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5) +1):
            if num%i==0:
                return False
        return True
    total=0
    for i in range(input2):
        if not is_prime(i):
            total+=input1[i]
    return total
input1=[10,20,30,40,50,60,70,80,90,100]
input2=10
sum_non_prime(input1, input2)       
        
#-----------------------------------------------

def longest_odd(input1,input2):
    current_length=0
    current_sum=0
    max_length=0
    longest_sum=[]
    for num in input1:
        if num%2!=0:
            current_length+=1
            current_sum+=num
            
        else:
            current_length>0
            max_length=current_length
            longest_sum=[current_sum]
        elif current_length>0:
                
            
    
