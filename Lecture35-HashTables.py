'''
same thing as a dictionary basically, structurally

you can check by key, not by index/value
    - this is the main advantage of a hash table

ListMap(Map) 

hash functions only go one way, but each time you have the same input youll get teh same output

indexes are known as buckets (before ... buckets)

collisions - you deal with them seperate ways
    1. could overwrite the data, this isnt a great strategy, depends on what youre doing
    2. open addressing - linear probing, quadratic probing, double hashing
        open addressing is when you have a collision and you have to find a new place to put the data
    3. chaining - linked list, binary search tree, etc
        chaining is when you have a collision and you put the data in a linked list


'''

# Exercise 1
"""
    Create a function that takes an input integer
    and returns a hash value. Use the modulus (%) to
    create a hash function. Test this function by inputting
    a number and printing what is returned. 
"""
def hash_function(num: int) -> int:
    """ Returns a hash value for the given number. """
    return num % 10

number = input('Enter a number: ')
print(hash_function(int(number)))

# Exercise 2
"""
    Go through all the items in the unordered list and 
    rearrange them in a new list according to their hash
    value. Use the function from exercise 1.  
"""

unordered_list = [-100,2,40,-10,1,17,82,-3]
hashed_list = [None]*10

for i in unordered_list:
    hash_value = hash_function(i)
    hashed_list[hash_value] = i
print(hashed_list)


# Exercise 3
"""
    Access the number 82 in the hashed_list, and print
    it to confirm it was appropriately accessed.

    Access the number -100 in the hashed_list, and print
    it to confirm it was appropriately accessed.
"""


# Exercise 4
"""
    Use the code from exercise 2 to deal with collisions by using
    linear probing.
"""