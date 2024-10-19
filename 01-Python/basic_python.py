# ---------------------------------
# Basic Python Operations
# ---------------------------------

# Print statement and variable types
print("Hello World")
x = 1
print(x)  # Output variable value
print(type(x))  # Check variable type (int)

x = 10000.0
print(x)  # Output updated variable value
print(type(x))  # Check variable type (float)

# Input statements and type conversion
age = input("Enter your age: ")
print(type(age))  # By default, input is of type string
print(age)

age1 = input("Enter another age: ")
print(type(age1))  # Still string type
print(age + age1)  # String concatenation of input values

# Converting input to integer type
age2 = int(input("Enter your age again: "))
print(type(age2))  # Now it's an integer
print(age2)

# Basic arithmetic operations
h = 5
a = 20
print(a + h)  # Addition
print(a - h)  # Subtraction
print(a * h)  # Multiplication
print(a / h)  # Division (float result)

# Integer division operator
print(100 // 20)  # Output: 5 (integer division)
# Modulus operator
print("Modulo division 100%13:", 100 % 13)
print("Modulo division 3%2:", 3 % 2)

# Exponentiation
print(5 ** 3)  # 5 raised to the power of 3

# Assignment and comparison operators
x = 0
x += 1  # Equivalent to x = x + 1
print(x)

# None operator
winner = None
print(winner is None)  # Check if variable is None

# If-else conditions
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")

# Loops
# While loop
count = 1
while count <= 10:
    print(count)
    count += 1

# For loop
print("Values in range:")
for i in range(2, 10):
    print(i)

# Nested loops example
colors = ["red", "yellow", "blue"]
fruits = ["apple", "banana", "cherry"]
for color in colors:
    for fruit in fruits:
        print(color, fruit)

# ---------------------------------
# Strings and String Operations
# ---------------------------------

# Basic string operations
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # String concatenation

# String slicing
x = "This is Python. It is powerful."
print(x[2:8])  # Output: 'is is '
print(x[:3])   # Slicing from the start
print(x[4:])   # Slicing to the end
print(x[-5:-2])  # Negative indexing

# String manipulation
x = "  This is Python  "
print(x.strip())  # Remove white spaces
print(x.replace("Python", "Programming"))  # Replace substrings

# String methods
print(x.upper())  # Convert to uppercase
print(x.lower())  # Convert to lowercase

# ---------------------------------
# Lists and List Operations
# ---------------------------------

# List creation and access
fruits = ["apple", "mango", "cherry"]
print(fruits[0])  # Access first item

# List methods
fruits.append("banana")  # Add item to the list
print(fruits)

fruits.remove("apple")  # Remove item
print(fruits)

fruits.reverse()  # Reverse the list
print(fruits)

fruits.sort()  # Sort list in alphabetical order
print(fruits)

# ---------------------------------
# Dictionaries and Dictionary Operations
# ---------------------------------

# Dictionary creation
car = {"Brand": "Ford", "Model": "Mustang", "Year": 2020}
print(car["Model"])  # Access dictionary value

# Add a new key-value pair
car["Color"] = "White"
print(car)

# Iterate over dictionary keys and values
for key, value in car.items():
    print(f"{key} == {value}")

# Copy dictionary
car_copy = car.copy()
print(car_copy)

# Nested dictionaries
family = {
    "child1": {"name": "Ram", "age": 10},
    "child2": {"name": "Shyam", "age": 8}
}
print(family)

# ---------------------------------
# Functions
# ---------------------------------

# Basic function
def greet():
    print("Hello from the function!")

greet()

# Function with parameters
def greet_with_name(name):
    print(f"Hello, {name}!")

greet_with_name("Nikita")

# Function with multiple arguments
def greet_with_fullname(first, last):
    print(f"Hello, {first} {last}!")

greet_with_fullname("Nikita", "Bhoge")

# Return values
def multiply(x, y):
    return x * y

result = multiply(5, 10)
print(f"Multiplication result: {result}")

# Lambda function example
add = lambda a, b: a + b
print(add(10, 5))  # Output: 15

# ---------------------------------
# Use Case Examples
# ---------------------------------

# Rollercoaster ticketing system
def rollercoaster():
    print("Welcome to the roller coaster")
    height = int(input("Enter your height in cm: "))
    if height >= 120:
        age = int(input("Enter your age: "))
        if age < 12:
            bill = 5
            print("Child ticket: $5")
        elif 12 <= age <= 21:
            bill = 20
            print("Teen ticket: $20")
        else:
            bill = 50
            print("Adult ticket: $50")

        wants_popcorn = input("Do you want popcorn (Y/N)? ")
        if wants_popcorn == "Y":
            bill += 3

        wants_photo = input("Do you want a photo (Y/N)? ")
        if wants_photo == "Y":
            bill += 4

        print(f"Your total bill is ${bill}")
    else:
        print("Sorry, you're not tall enough to ride.")

rollercoaster()

# BMI Calculator
def bmi_calculator():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        print(f"Underweight (BMI: {bmi})")
    elif 18.5 <= bmi < 25:
        print(f"Normal weight (BMI: {bmi})")
    elif 25 <= bmi < 30:
        print(f"Overweight (BMI: {bmi})")
    elif 30 <= bmi < 35:
        print(f"Obese (BMI: {bmi})")
    else:
        print(f"Clinically obese (BMI: {bmi})")

bmi_calculator()

# Find duplicates in a list
def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

lst = [1, 2, 3, 4, 4, 5, 6, 6]
print(f"Duplicates: {find_duplicates(lst)}")

