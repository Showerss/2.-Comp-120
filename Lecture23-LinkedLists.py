'''
Lecture 23: Linked Lists
    - A linked list is a data structure that consists of a sequence of elements
    - Each element is a node that contains a value and a reference to the next node
    - The first node is called the head and the last node is called the tail, 
    - typically you can only access the head and follow the list to the tail
    - a nodes typehint is Optional['Node'], because it can be either a node or None
    - data type in a linked list is a node, referenced by self.head
        - self.head when its an empty list would be None.. best way would be Optional['Node']
    - each node has two pieces of information, the value and reference to the next node
    - to access the next node you call self.next
    - the type of self.next is Optional['Node'] which means it'll be node or none
    - the last reference will be None
    - some methods would be:
        - add: add a node to the front of the list
        - append: add a node to the end of the list
        - pop: remove the first node from the list
        - search: search for a value in the list
        - get_item: get the value at a specific index
        - size: get the number of nodes in the list
        - is_empty: check if the list is empty
        - __len__: get the number of nodes in the list
        - __str__: get a string representation of the list
            you could write this str(2, 3) == "2 -> 3"
        - __contains__: check if a value is in the list
            you could write this contains(2, 3) == False
        - __eq__: check if two lists are equal
            you could write this eq(2, 3) == False
    - nodes are NOT data structures
    - __str__ is better than str because it allows you to print the object directly
    - to add to my linked list, I would create a new node with the add methods and set the next node to the current head, the eastiest is the head
    - the benefit of linked lists over lists are that you can add and remove elements in constant time
        - also with linked lists each node has its own spot in memory and doesn't have to be contiguous
        - the downside is that you can't access elements by index
        - you would use linked lists over regular when


    FOR UML DIAGRAMS:
        the diamond means (has a)
        the arrow means (is a)

'''



from typing import Any, Optional


# Exercise 1:
"""
    Let's write the node class that will be used inside of the LinkedList class
"""
class Node:

    #instance variables
    Data: Any
    Next: Optional['Node']

    def __init__(self, data:Any, next:Optional['Node']) -> None:
        self.data = data
        self.next = next

# Exercise 2:
"""
    Let's start writing the LinkedList class. We will not finish this class,
    but ultimately all of the below methods will be filled out
"""

class LinkedList:
    def __init__(self):
        def __init__(self):
            self.head = None

    def __len__(self) -> int:
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    
    def __str__(self):
        pass
    
    def __contains__(self, value: Any) -> bool:
        current = self.head
        while current is not None:
        # for i in range(self.size()): (this would be O(2n) which is O(n))
            if current.data == value: #if the data within the current node is the value in which we are looking for
                return True
            current = current.next
        return False #if we don't find the value in the list
    
    def __eq__(self, other):
        pass

    def search(self, value: Any) -> bool: #O(n) - because we have to iterate through the list
        '''same as __contains__ but with a different name'''
        current = self.head

        while current is not None:
            if current.data == value: #if the data within the current node is the value in which we are looking for
                return True
            current = current.next
            
        return False #if we don't find the value in the list
    
    def add(self, data: Any): #O(1) - because this is just an assignent 
        '''adding a node to the front of the list'''
        new_node = Node(data, self.head)
        self.head = new_node

    def is_empty(self): #O(1) - because this is just a comparison
        return self.head is None

    def size(self) -> int: #O(n) - because we have to iterate through the list
        ''' same as __len__ but with a different name'''
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, value: Any) -> None:
        '''adding a node to the end of the list'''
        current = self.head
        previous = None
        while current.next is not None: #loop through until you find the none return
            previous = current #keep track of the previous node
            current = current.next #keep moving to the next node

        
        new_node = Node(value, None) #create a new node
        if self.is_empty() == False: #if the list is not empty
            previous.next = new_node #once you find the none, set the next node to the new node (this should be the last)
        else: #if the list is empty
            self.head = new_node #set the head to the new node and begin a list



    def pop(self) -> Any:
        '''removing the first node from the list'''
        current = self.head
        previous = None

    def get_item(self, index: int) -> Any:
        pass


# Tester code to make live after your implementation
'''l = LinkedList()
l.add(5)
l.add(-8.3)
print(l)
assert len(l) == 2
assert 5 in l

l2 = LinkedList()
l2.add(5)
l2.add(90)
l2.append(16)
assert l2.get_item(0) == 90
assert l2.is_empty() == False
assert l2.size() == 3
assert l2.pop() == 16
assert l2.search(16) == False
assert l2.search(90) == True
print(l2)
assert l != l2'''
