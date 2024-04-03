# Question 1
"""
    Explain how the following sorting algorithms would work on the below list:
    a) selection sort
    b) insertion sort
    c) bubble sort
"""  

num_list = [7,1,6,2,4,8,5,3]
#a. selection sort would take the first number and compare it to the rest of the list, then move the smallest number to the front of the list. Selection sort looks for the next logical smallest item to put in the list, it searches the unsorted part (to the right) and then adds that next smallest to the list. It would then move to the next number and repeat the process. In this case selection would start with 7 and compare it to the rest of the list and move 1 to the front. Then it would move to 6 and compare it to the rest of the list and move 2 to the front. It would continue to do this until the list is sorted.
Pass 1:
[7,1,6,2,4,8,5,3]
[1,7,6,2,4,8,5,3]
[1,2,7,6,4,8,5,3] #again to clarify, the right half of the list is searched for the next smallest after [1,2] are sorted and stated
[1,2,3,7,6,4,8,5]
[1,2,3,4,7,6,8,5]
[1,2,3,4,5,7,6,8]
[1,2,3,4,5,6,7,8] #fin

#b. insertion sort would take the first number and compare it to the rest of the list, then move the smallest number to the front of the list. It would then move to the next number insertion takes the number its currently evaluating and will insert it into the sorted part of the list where it fits properly. Then it extends to compare the next number in the unsorted part and repeat the process until completed. In this case insertion would start with 7 and compare it to the rest of the list and move 1 to the front. Then it would move to 6 and compare it to the rest of the list and move 2 to the front. It would continue to do this until the list is sorted. The only difference between this and selection is that insertion will insert the number into the sorted part of the list where it fits properly. whereas selection will swap the smallest number to the front of the sorted list
Pass 1:
[7,1,6,2,4,8,5,3]
[1,7,6,2,4,8,5,3]
[1,6,7,2,4,8,5,3]
[1,2,6,7,4,8,5,3] #again to clarify, this looks to the left half of the list and finds where 2 would go in the list [1,6,7]
[1,2,4,6,7,8,5,3]
[1,2,4,6,7,8,5,3] #stays the same because 7/8 are fine
[1,2,4,5,6,7,8,3]
[1,2,3,4,5,6,7,8] #fin



#c. bubble sort would start at the left end of the list compare the first two numbers and swap them if necessary, bubble sort would then move to the next two numbers and repeat the process. Only ever sorting the two adjacent items in the list and swapping if needed. It would continue to do this until the list is sorted. It will go over the list as many times until the list is sorted. In this case bubble sort would start with 7 and 1 and swap them. Then it would move to 7 and 6 and swap them. It would continue to do this until the list is sorted. 
Pass 1 
[7,1,6,2,4,8,5,3]
[1,7,6,2,4,8,5,3]
[1,6,7,2,4,8,5,3]
[1,6,2,7,4,8,5,3]
[1,6,2,4,7,8,5,3]
[1,6,2,4,7,8,5,3] #7 and 8 are fine already
[1,6,2,4,7,5,8,3]
[1,6,2,4,7,5,3,8] #8 reaches the end and pass 1 is finished

# Extra Credit (0.2 points)
"""
    Explain how you would use binary search to look 
    through your sorted list for the number 2. Sorted list
    is shown below. 
"""

sorted_list = [1,2,3,4,5,6,7]

#so basically binary search works by taking the midpoint of the list and comparing it to the target (2 in this case). If the target is less than the midpoint then the search continues to the lower half (the lest half) of the list. If the target is greater than the midpoint then the search continues to the upper half (the right half) of the list. This process continues until the target is found or the list is empty. In this case the target is 2 and the midpoint is 4. 2 is less than 4 so the search continues to the left half of the list. The midpoint of the left half is 2 and the target is found. 