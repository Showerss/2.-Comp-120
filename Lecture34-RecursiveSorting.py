'''
merge sorting steps:
    1. Divide the list into two halves
    2. Recursively sort each half
    3. Merge the two halves together

quicksort: 
    1. Pick a pivot element
    

'''


# Question 1
"""
    Write the code for recursive merge sorting. To make readability 
    easier, I have created a helper function named merge that will
    merge two sorted lists together. 
"""

def merge_sort(a: list[int]) -> list[int]:
    """ Sorts and returns the given list (a). """
    if len(a) <= 1:
        return a
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        first = merge_sort(left)
        second = merge_sort(right)
        return merge(first, second)

def merge(a: list[int], b: list[int]) -> list[int]:
    """ Combines two sorted lists into one sorted list"""
    sorted_list = []
    countera = 0
    counterb = 0

    while countera < len(a) or counterb < len(b): #as long as there are still items in the list
        if countera < len(a) and counterb < len(b): #if there are still items in both lists
            if a[countera] <= b[counterb]: #if the item in the first list is less than or equal to the item in the second list
                sorted_list.append(a[countera])
                countera += 1
            else:
                sorted_list.append(b[counterb])
                counterb += 1
        elif counterb < len(b): #if there are still items in the second list
            sorted_list.append(b[counterb])
            counterb += 1
        else:
            sorted_list.append(a[countera])
            countera += 1

    return sorted_list

r = [-4,4,15,21,-100,-60,10,4,12,18,2,34]
m = merge_sort(r)
print(m)

# Question 2
"""
    Write recursive code for quick sort. To make readability 
    easier, I have created a helper function named partition 
    that will move items in the list as needed and return the 
    new index that the list was split at (based on pivot). 
"""

def partition(lista, low, high):
    """ Moves items in the list as needed so that all items 
    between index low and high are sorted based on the pivot. 
    All items to the left of the pivot are less than the pivot, 
    and the ones to the right are greater than the pivot. It returns 
    the new index that the list was split at (based on pivot)"""

    pivot = lista[(high+low)//2]
    # swap pivot to the end of working list

    leftitem = low
    rightitem = high - 1
    while leftitem <= rightitem:
        # find left item
        # find right item
        # swap right and left item if needed
        pass

    # place pivot back where it belongs in the list
    # return the location of the pivot
 
def quickSort(lista, low, high):
    if low < high:
        # Find pivot element such that element smaller than pivot are on the left element greater than pivot are on the right
        # Recursive call on the left of pivot
        # Recursive call on the right of pivot
        pass
 
data = [1, 7, 4, 1, 10, 9, -2]
print(f"Unsorted: {data}")
 
quickSort(data, 0, len(data) - 1)
 
print(f"Sorted: {data}")