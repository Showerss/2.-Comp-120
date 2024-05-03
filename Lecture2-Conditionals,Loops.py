# Exercise 1 (Conditionals):
"""
    Have the user input a number. If the user inputs your favorite number, print 
    out a special celebratory message for them. Otherwise, print out the difference 
    between the number they inputted and your favorite number, along with a message.   
"""
myFavoriteNumber = 7
userNumber = input("Enter a number: ")
if userNumber == myFavoriteNumber:
    print(f"Congratulations! You entered my favorite number!{myFavoriteNumber}")
else:
    numberDifference = abs(myFavoriteNumber - int(userNumber))
    print(f"Wow what a lame number to choose, my number is {numberDifference} away from {userNumber}")




# Exercise 2 (Loops):
"""
    Write a Python program to print those numbers which are divisible by 7 and multiples of 5, 
    between 1500 and 2700 (both included).


    for loop, while loops are both great
        for needs to be some sort of iterable sequence
    while loops execute infinitely until bool condition is met
        3 components: start, stop, increment(accumulator) of that beginning variable


    range will NEVER hit the stop value, always one before.
        start will always be the true start value

    accumulator loop will increase the loop by a certain number
"""

for nums in range(1500, 2701, 5):
    if nums % 7 == 0:
        print(nums)


# Exercise 3 (Strings):
"""
    Write a Python program to add 'ing' at the end of a given string (length should be 
    at least 3). If the given string already ends with 'ing', add 'ly' instead. 
    If the string length of the given string is less than 3, leave it unchanged.
        Sample String : 'abc'
        Expected Result : 'abcing'
        Sample String : 'string'
        Expected Result : 'stringly'

    concatenation +
    slicing : works just like range that it never includes the final part of that slice
    split, strip, join, etc

    by item: 
    for ch in "CS Rules!"

    by index
    for i in range(len(text))
"""

userString = input("Give me a string more than 3 characters!")
if len(userString) > 3:
    if userString [-3:] == 'ing':
        userString += 'ly'
    else:
        userString += "ing"
else:
    print(userString)



# Exercise 4 (f-string): 
"""
    SAME AS EXERCISE 1: Have the user input a number. If the user inputs your favorite number, print 
    out a special celebratory message for them. Otherwise, print out the difference 
    between the number they inputted and your favorite number, along with a message. 
    Use f-strings to format both print statements.    
"""
myFavoriteNumber = 7
userNumber = input("Enter a number: ")
if userNumber == myFavoriteNumber:
    print(f"Congratulations! You entered my favorite number!{myFavoriteNumber}")
else:
    numberDifference = abs(myFavoriteNumber - int(userNumber))
    print(f"Wow what a lame number to choose, my number is {numberDifference} away from {userNumber}")




# Exercises to practice at home if you are struggling with these topics:
"""
Strings:
    1) Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
    Sample String : 'w3resource'
    Expected Result : 'w3ce'
    Sample String : 'w3'
    Expected Result : 'w3w3'
    Sample String : ' w'
    Expected Result : Empty String

    2) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
    Sample String : 'restart'
    Expected Result : 'resta$t'

    3) Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
"""
newString = input("Give me an example string")
if len(newString) > 3:
    newString = newString[:1] + newString[-2:]
elif len(newString) :



"""
Conditionals:
    1) Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
        Expected Output : 0 1 2 4 5
    
    2) Write a Python program to check whether an alphabet is a vowel or consonant.
        Expected Output:
            Input a letter of the alphabet: k                                       
            k is a consonant.
    
    3) Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.

    4) Write a Python program to display the astrological sign for a given date of birth.
        Expected Output:
            Input birthday: 15                                                      
            Input month of birth (e.g. march, july etc): may                        
            Your Astrological sign is : Taurus 
"""

"""
Loops:
    1) Use for loop to iterate from 0 to 100 and print only even numbers

    2) Write a Python program to get the Fibonacci series between 0 and 50.
    Note : The Fibonacci Sequence is the series of numbers :
    0, 1, 1, 2, 3, 5, 8, 13, 21, ....
    Every next number is found by adding up the two numbers before it.
        Expected Output : 1 1 2 3 5 8 13 21 34

    3) Use for loop to iterate from 0 to 100 and print the sum of all numbers.

    4) Ask the user for a 5-letter word. If they enter a word that is not 5 letters, 
    print an error message and then ask them to enter another word. 
"""