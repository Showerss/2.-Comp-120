'''


'''


# Exercise 1:
"""
    Write a recursive function that when given a list of items,
    all the possible subsets of those items are printed.
"""
def possible_subsets(items: list, subset_so_far: set) -> None:
    """
    """
    pass
possible_subsets(["Iron Man", "Captain Marvel"], set())

# Exercise 2
"""
    Write a recursive function that determines if there is a way
    to group the numbers in a list together such that they are 
    less than or equal to the max_number_groups provided in 
    the list
    Ex's: numbers = [1,3,6,12]
        max_number_groups = [1,3,6,12] -> returns True
        max_number_groups = [4,18] -> returns True
        max_number_groups = [1,3,12] -> returns False
        max_number_groups = [100] -> returns True
"""
def grouping_numbers(numbers: list[float], max_number_groups: list[float]) -> bool:
    """
        Returns True if there is a way to group the numbers such
        that their sum is less than or equal to the numbers in 
        max_group_numbers. Returns False otherwise. 
    """
    pass

print(grouping_numbers([1,3,6,12], [6,13,3]))