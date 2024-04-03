import random

# Exercise 1 (Lists):
"""
    Create a list of 100 random integers between 1 and 100.
    Write a Python program to multiply all the items in a list.
"""
# how to create a single random integrer between 1 and 100
random.randint(1,100)

# Exercise 2 (Aliasing):
"""
    Create an alias of the lists from exercise 1, and call it alias.
    Create a copy of the list from exercise 1, and call it not not_alias.
"""

# Exercise 3 (File IO):
"""
    Open the file "EXCITEMENT.txt", and print out the number of lines the file contains.
    Once the file has been completely read, open a new file called "NUMBER_LINES.txt"
    and write a statement that includes the number of lines the file contained.
"""

# Exercise 4 (with statements):
"""
    Complete exercise 3 using a with statement.
"""

with open('EXCITEMENT.txt', 'r') as file:
    num_lines = 0 
    for line in file:
        num_lines += 1

# Exercise 5 (Type Hints):
"""
    Add type hints to the below and completed function.
"""



def AverageThreeNumbers(num1, num2, num3):
    """
    function that takes in 3 numbers, and calculates the average
    """
    sum = num1 + num2 + num3
    return sum/3

AverageReturnedValue = AverageThreeNumbers(3,4.2,6)
print(AverageReturnedValue)

# Exercise 6 (Dictionaries):
"""
    Merge two dictionaries into one. You do not know how many key-value pairs
    are in either dictionary, just that they are named a and b.
"""
dictionary_a = {'bananas': 5}
dictionary_b = {'apples': 10}

for (k,v) in dictionary_b.items():
    if k not in dictionary_a:
        dictionary_a[k] = v

print(dictionary_a)


# Exercises to practice at home if you are struggling with these topics:
"""
LISTS
    1) Write a Python program to get the smallest number from a list.
    
    2) Write a Python program to find the second largest number in a list.
    
    3) Write a Python program to find common items in two lists.

    4) Write a Python program to select the odd items from a list, and add them to another list
    called OddList.
"""

"""
FILE READING & WRITING
    1) Write a Python program to read first n lines of a file.

    2) Write a Python program to read a file line by line and store it into a list, with each line being one item in the list.

    3) Write a Python program to copy the contents of a file to another file .
"""

"""
DICTIONARIES
    1) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
        Sample Dictionary ( n = 5) :
        Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    2) Write a Python program to multiply all the items in a dictionary.

    3) Write a Python program to create a dictionary from a string.
    Note: Track the count of the letters from the string.
        Sample string : 'w3resource'
        Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

    4) Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.
        Sample Output:
            Original lists:
            ['a', 'b', 'c', 'd', 'e', 'f']
            [1, 2, 3, 4, 5]
            Combine the values of the said two lists into a dictionary:
            {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
"""