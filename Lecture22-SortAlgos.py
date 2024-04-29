'''

selection sort: 
    time complexity of O(n^2) - 
    searches the unsorted part - adding elements by a list by finding the smallest element and adding it to the list, swaps 

insertion sort: 
    time complexity of O(n^2) -
    searches the sorted part - takes the last elent and swaps it within the already sorted list, not a swap method

    
bubble sort: 
    time complexity of O(n^2) - compares adjacent items and swaps them if necessary, if no swaps are made, the list is sorted
'''




import random

def create_and_print_random_list():
    """
    Create a list of 20 random integers between -100 and 100
    """
    random_nums = []
    for i in range(20):
        random_nums.append(random.randint(-100,100))
    print(f"Your random list is {random_nums}")
    return random_nums

def swap(listy, indexa, indexb):
    """
    Swap the items at indexa and indexb in listy
    """
    tmp = listy[indexa] 
    listy[indexa] = listy[indexb] 
    listy[indexb] = tmp


# Exercise 1:
"""
    Write your own code to selection sort the provided list.
    The commentary below is supposed to help you in writing
    your code - use it if its helpful to you
"""

def selection_sort(listA):
    """
    This function should use the selection sort algorithm to 
    sort the provided list.

    Parameters:
    - listA: list[int]

    Returns: 
    - list[int] (after it has been sorted) 
    - int (the amount of iterations it took to find a solution)
    """

    time_counter = 0 # keeping track of the time it takes to sort
    
    '''
    for: loop through the entire list 
        variable - keep track of your current index
        variable - keep track of the index for the minimum value in the remaining part of the list
        
        loop through the rest of the unsorted list and find the minimum number
            if the current number is smaller than the minimum number, update the index of the minimum number
            increment time_counter += 1
        
        if needed, swap the item at the current index you are looking 
        at and the index where you found the minimum number 
        in the unsorted part of the list

    return listA, time_counter
    '''

    for num in range(len(listA)-1):
        sorted_part = num

        for i in range(num+1, len(listA)):
            if listA[i] < listA[sorted_part]:
                sorted_part = i

            time_counter += 1
        swap(listA, num, sorted_part)

    return listA, time_counter

# Exercise 2:
"""
    Write your own code to insertion sort the provided list.
    The commentary below is supposed to help you in writing
    your code - use it if its helpful to you
"""

def insertion_sort(listA):
    """
    This function should use the insertion sort algorithm to 
    sort the provided list.

    Parameters:
    - listA: list[int]

    Returns: 
    - list[int] (after it has been sorted) 
    - int (the amount of iterations it took to find a solution)
    """

    time_counter = 0 # keeping track of the time it takes to sort
    '''
    for: loop through the entire list 
        variable - keep track of your current index
        variable - keep track of the current item (value at your current index)
        
        loop through the rest of the unsorted list until you 
        find the correct index that the number should be placed at
            shift items in the list to the right as needed
            increment time_counter += 1
        
        place the current item at the index that you found

    return listA, time_counter
    '''

    i = 0
    for i in range(len(listA)-1):
        unsorted_part = i + 1

        while unsorted_part > 0 and listA[unsorted_part] < listA[unsorted_part-1]:
            swap(listA, unsorted_part, unsorted_part-1)
            unsorted_part -= 1
            time_counter += 1

        i += 1

    return listA, time_counter

# Exercise 3:
"""
    Write your own code to bubble sort the provided list.
    The commentary below is supposed to help you in writing
    your code - use it if its helpful to you
"""

def bubble_sort(listA):
    """
    This function should use the bubble sort algorithm to 
    sort the provided list.

    Parameters:
    - listA: list[int]

    Returns: 
    - list[int] (after it has been sorted) 
    - int (the amount of iterations it took to find a solution)
    """
    time_counter = 0 # keeping track of the time it takes to sort

    '''
    loop until everything is in order 
        variable - keep track of whether or not swapping has taken place
        
        loop through the entire list
            compare all of the adjacent items (i.e. items at index 0 and index 1)
            swap adjacent items, if necessary
            increment time_counter += 1

    return listA, time_counter
    '''

    for i in range(len(listA)-1):
        swapped = False

        for j in range(i):
            if listA[j] > listA[j+1]:
                swap(listA, j+1, j)
                swapped = True
        time_counter+=1 

        if swapped == False:
            break

    return listA, time_counter

random_list = create_and_print_random_list()
selection_stats = selection_sort(random_list[:])
print(f"Your selection sort list is {selection_stats[0]} and took the time complexity of {selection_stats[1]}")

insertion_stats = insertion_sort(random_list[:])
print(f"Your insertion sort list is {insertion_stats[0]} and took the time complexity of {insertion_stats[1]}")

bubble_stats = bubble_sort(random_list[:])
print(f"Your bubble sort list is {bubble_stats[0]} and took the time complexity of {bubble_stats[1]}")