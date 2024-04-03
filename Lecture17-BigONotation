'''
Big O notation aka time complexity 
how fast is my algorithm / compare to others' code

complexity is the measure of time/space that a algo requires to find its solution 

Big O catches the overall idea of code efficiency
calculated by saying
    O(f(n)) 
        n being the input size
    T(n)

x = 1 - this is 1 operation
x + y - 1 operation
a > b - 1 operation
foo[i] - 1 operation 


any time your code isnt iterating over something, its just basic assignment the time complexity is 
    O(1) or T(1)

x = a+b - 2 operations
y = (x*2) // 5 - 3 operations


if n > m + 3: - 2 operations
a += 1 - 2 operations


----
max = L[0] - 2
i = 1 - 1
while i < n - 1n .... then loop is executing n-1 times... its -1 because  
    if L[i] > max then - 2
        max = L[i] - 2
    i += 1 - 2 
return max - 1

2 + 1 + 1 = 4 times total
while: 1n 
loop: 6 items in the loop times (n-1)



------
O(f(n)) is the normal notation for big O notation

listA += [5] is O(n) because it has to iterate over the list to add the 5 to the end
however listA.append(5) is O(1) because it just adds the 5 to the end of the list

list vs contain has differnt time complexities as well
    list: O(n)
    contain: O(1)

adding to the beginning of a list or to a specific place in lists have a bigger time complexity

mostly usually, add befoe you sort

if two time complexities are seen, look to the constants to see which is better... might be small but there could be one

big O notation is a measure of the worst case scenario
there can be other notations for the smallest case scenario possible, but typically big O is used


--------------
ADT - abstract data type




'''





# Exercise 1:
"""
Simplify the following big O expressions as much as possible:

O(n + 10)
    O(n)
O(100 * n)
    O(n)
O(25)
    O(1)
O(n^2 + n^3)
    O(n^3)
O(n + n + n + n)
    O(n)
O(1000 * log(n) + n)
    O(n)
O(1000 * n * log(n) + n)
    O(n*log(n))
O(2^n + n^2)
    O(2^n)
O(5 + 3 + 1)
    O(1)
O(n + n^(1/2) + n^2 + n * log(n)^10)
    O(n^2)


"""

# Exercise 2:
"""
    What is the time complexity of the following chunks of code?
"""
n = 1000
k = 10
for i in range(0,n,1):
    i*=k
# time complexity is: O(n) = n

value = 0
for i in range(0, n, 1):
    for j in range(0, i, 1):
      value += 1
# time complexity is: O(n) = 
   
def isEven(value):
  if value % 2 == 0:
    return True
  else:
    return False
# time complexity is: O(n) = 1