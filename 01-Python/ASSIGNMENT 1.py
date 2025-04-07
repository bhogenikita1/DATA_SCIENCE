###  ASSIGNMENT 1 ###

#1. Write a program to check whether a number is positive or negative or zero

def check_number(num):
    if num > 0:
        return "Number is positive"
    elif num < 0:
        return "Number is negative"
    else:
        return "Number is zero"

# Taking user input
number = float(input("Enter a number: "))

# Checking the number and displaying the result
result = check_number(number)
print(result)



















