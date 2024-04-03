import math

# """
# asserts can also be made into doctests - not the best though truthfully, if one fails it just stops

# """

# # Exercise 1:
# """
#     Add the following to the below function:
#     - type hints 
#     - indicate any preconditions that should be met in the docstring
#     - use assert statements to check the preconditions 
# """

# def Letter_Grade(percentage:float) -> str:
#     """
#         This function returns the letter grade associated with a given percentage

#         Preconditions: 
#             - percentage must be a float between 0 and 100

#         Parameters:
#             - percentage (float):represents the percentage someone has earned in a class 
        
#         Returns: 
#             - lettergrade (str): the letter associated with the given percentage
#     """
#     assert isinstance(percentage, float) and 0 <= percentage <= 100
    
#     lettergrade = "none"

#     if percentage>=90:
#         lettergrade = "A"
#     elif percentage>=80:
#         lettergrade = "B"
#     elif percentage>=70:
#         lettergrade = "C"
#     elif percentage>=60:
#         lettergrade = "D"
#     elif percentage < 60:
#         lettergrade = "F"
    
#     return lettergrade

# letter = Letter_Grade(int(input("Please input a grade as a percentage")))

# print(letter)





# Exercise 2:
"""
    Write assert statements to check the conditions provided in the comments.
    Be sure to print an appropriate error message for each
"""
listA = [1,2,3,4,5] # check that the list is not empty
assert len(listA) > 0, "please populate list A"
assert listA != []

num2 = 10.5
num1 = 21           # num2 should be larger than num1
assert num2 > num1




# # Exercise 3:
# """
#     Use the below function area to make the following assertions:
#         - Assert that area(1) returns a float
#         - Assert that area(0) returns a value of 0
#         - Assert that area(5) is approximately equal to 78.5 (hint: math.isclose(..., abs_tol=0.1))
# """
# def area(radius):
#     """Calculate the area of a circle based on the given radius."""
#     return math.pi * radius ** 2

# assert isinstance(area(1), float)
# assert area(0) == 0
# assert 