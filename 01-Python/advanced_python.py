##############   ADVANCED PYTHON   ################

#### List Comprehension ####

# Basic list generation using a for loop
basic_list = []
for num in range(0, 20):
    basic_list.append(num)
print(basic_list)

# Using list comprehension for the same task
comprehension_list = [num for num in range(0, 20)]
print(comprehension_list)

# Capitalizing names in a list using list comprehension
names = ["dada", "mama", "kaka"]
capitalized_names = [name.capitalize() for name in names]
print(capitalized_names)

# List comprehension with if statement (filtering even numbers)
def is_even(num):
    return num % 2 == 0

even_list = [num for num in range(21) if is_even(num)]
print(even_list)

# List comprehension with nested for loops
nested_list = [f"{x}{y}" for x in range(3) for y in range(3)]
print(nested_list)

#### Dictionary Comprehension ####

# Creating a dictionary where keys are numbers and values are their squares
squares_dict = {x: x*x for x in range(3)}
print(squares_dict)

#### Generators ####

# Simple generator for numbers using the 'yield' keyword
def range_even(end):
    for num in range(0, end, 2):
        yield num

# Accessing generator values with 'next()'
even_gen = range_even(6)
print(next(even_gen))  # 0
print(next(even_gen))  # 2
print(next(even_gen))  # 4

# Generator for creating hidden password
def lengths(itr):
    for ele in itr:
        yield len(ele)

def hide(itr):
    for ele in itr:
        yield ele * "*"

passwords = ["not good", "give m-pass"]
for hidden in hide(lengths(passwords)):
    print(hidden)

#### Create and Hide Password from User Input ####

adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
number = input("Enter a number: ")
sc = input("Enter a special character: ")
user_password = adj + noun + str(number) + sc
print(f"Your password is: {user_password}")

# Hiding the generated password
hidden_password = hide(lengths(user_password))
for hidden_char in hidden_password:
    print(hidden_char, end="")

#### Enumerators and Zipping ####

# Printing list with index using a for loop
fruits = ["Apple", "Mango", "Watermelon"]
for index in range(len(fruits)):
    print(f"{index+1} - {fruits[index]}")

# Using enumerate to simplify the above task
for index, fruit in enumerate(fruits, start=1):
    print(f"{fruit} - {index}")

# Using zip function to combine two lists
names = ["Dada", "Mama", "Kaka"]
mobiles = ["9975", "8648", "9327"]
for name, mobile in zip(mobiles, names):
    print(f"{mobile} - {name}")

# Using zip_longest to handle mismatched lists
from itertools import zip_longest
for name, mobile in zip_longest(mobiles, names, fillvalue="Unknown"):
    print(f"{mobile} - {name}")

#### Useful Functions: all(), any(), count(), cycle() ####

# all() example: returns True if all values are non-zero
values = [2, 3, 4, 1, -2, 0, -4]
if all(values):
    print("All values are true")
else:
    print("There are zero values")

# any() example: returns True if at least one value is non-zero
if any(values):
    print("There are some non-zero values")
else:
    print("All values are zero")

# count(): generates an infinite sequence starting from 0 or a given number
from itertools import count
counter = count(start=1)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# cycle(): repeats an iterable infinitely
from itertools import cycle
tasks = ["eat", "code", "sleep", "repeat"]
for task in cycle(tasks):
    print(task)

# repeat(): repeats a single value for a specified number of times
from itertools import repeat
for msg in repeat("Keep patience", times=3):
    print(msg)

#### Combinations and Permutations ####

# Combinations: select items without regard to order
from itertools import combinations
players = ["Virat", "Dhoni", "Rohit", "Sachin"]
for combo in combinations(players, 2):
    print(combo)

# Permutations: select items with regard to order
from itertools import permutations
for perm in permutations(players, 3):
    print(perm)

#### Shallow and Deep Copying ####

# Assignment operation (shallow copy)
list_a = [1, 2, 3, 4]
list_b = list_a  # Both point to the same memory location
list_a[0] = -10
print(list_a)  # [-10, 2, 3, 4]
print(list_b)  # [-10, 2, 3, 4] (same as list_a)

# Shallow copy using list slicing
import copy
list_c = copy.copy(list_a)
list_c[0] = 100
print(list_c)  # [100, 2, 3, 4] (independent from list_a)

# Deep copy (creates an independent copy)
nested_list = [[1, 2], [3, 4]]
deep_copy_list = copy.deepcopy(nested_list)
nested_list[0][0] = 99
print(nested_list)  # [[99, 2], [3, 4]]
print(deep_copy_list)  # [[1, 2], [3, 4]] (independent from nested_list)
