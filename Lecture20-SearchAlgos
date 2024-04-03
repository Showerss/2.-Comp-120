'''
if you have a _ before a class, it measns just to ignore that class, its for the implementer only typically

UML ( universal modeling language )


linear searching - O(n) sequential searching meaning 1 at a time until the list is done, so it goes n times, the amount of times 


binary searching - O(log n) ignoring entire halves of a list, after its sorted by what is automatically not viable
    log means constantly dividing in half 
    list needs to be sorted 


'''


import random

# Exercise 1:
"""
    Write your own code to sequentially search through a list
    for a given item. You can hardcode the list that you are searching through,
    but you should allow the user to input the item they want to search for.
    You should sort your list using list_name.sort() so you can use it for Exercise 2.
    For an additional item, add in a measure of how many times your loop has to execute.
"""
random_nums = []
for i in range(20000):
    random_nums.append(random.randint(-100,100))
random_nums.sort()

correct = False
time_complexity = 1

n = int(input('what number are you looking for?'))

# for item in random_nums:
#     time_complexity += 1
#     if item == n:
#         print(f'Found it! {time_complexity}')
#         break




# Exercise 2:
"""
    Write your own code to perform a binary search through a sorted list
    for a given item. You can hardcode the sorted list that you are searching through,
    but you should allow the user to input the item they want to search for. In fact,
    you should use the same hardcoded list and input from the user that you used in number 1.
    This will allow you to compare time complexity - to do this
    add in a measure of how many times your loop has to execute.
"""
first = 0
last = len(random_nums)-1

while first <= last:
    midpoint = (first + last) // 2
    if n == random_nums[midpoint]:
        correct = True
        break
    
    elif n < random_nums[midpoint]:
        last = midpoint - 1
    
    else:
        first = midpoint + 1 

if correct == False:
    print('Nope')