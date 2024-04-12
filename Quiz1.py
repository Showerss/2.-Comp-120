# Question 1:
"""
    This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] 
    reverse the order using a loop. Your loop should work for any length of fruit list.
"""
fruit_list = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit_list)):
    print(fruit_list[len(fruit_list) - 1 - i])



# Question 2:
"""
   Write a Python program to read the string from the file "string.txt" and convert 
    that string to a list where every character is it's own item in the list. 
    You can create your own "string.txt" file and insert one row
    with the single string "You are awesome!" in it to complete this exercise. This string
    should create the list ["Y", "o", "u", " ", "a", "r", "e",...]
"""
sample_list = []
with open('string.txt', 'r') as string_file:
    first_line = string_file.readline()
    for character in first_line:
        sample_list.append(character)
print(sample_list)