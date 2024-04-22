'''
all recursion needs a base case and a recursive case
    base case - the simplest case that can be solved
    recursive case - the case that can be broken down into smaller parts


linkedlists are pretty similar to recursion since each node calls another node

proof by induction:

'''
def count (x):
    if x < 0:
        #bas case
        return 0
    else:
        #recursive case
        return x + count(x-1)

# Exercise 1:
"""
    Use the below recursive function to identify what happens 
    when you change the function call to different values for
    the parameter level. You can also change the size if the
    drawing becomes too small to see. 
"""
import turtle
def koch(t: turtle.Turtle, size: int, level: int):
    if level == 0:
        t.forward(size)
    else:
      size = size // 3
      koch(t, size, level-1)
      t.left(60)
      koch(t, size, level-1)
      t.right(120)
      koch(t, size, level-1)
      t.left(60)
      koch(t, size, level-1)
    
t = turtle.Turtle()
s = turtle.Screen()
koch(t, 150, 2)
s.exitonclick()

# Exercise 2
"""
    You have been provided the node class and LinkedList class
    that we wrote together in class. Add the following recursive
    methods: 
    - search
    - get_item
"""

from typing import Any, Optional

class Node:
    data: Any
    next: Optional['Node'] # tricky: use quotes around type
    prev: Optional['Node']

    def __init__(self, data: Any, next: Optional['Node'], prev: Optional['Node']):
      self.data = data
      self.next = next
      self.prev = prev     

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, value: Any) -> bool:
        """ Returns True if <value> is stored
            as data in this list. """
        current = self.head
        while current is not None:
            if current.data == value: # found it?
                return True
            current = current.next

        return False
    
    def add(self, data: Any):
        """ Adds new node containing data to
          front of this list. """
        if self.is_empty() == False:
            new_node = Node(data, self.head, None)
            self.head.prev = new_node
            self.head = new_node
        else: 
            new_node = Node(data, None, None)
            self.head = new_node
            self.tail = new_node

    def is_empty(self):
        """ Returns true if list is empty,
          False otherwise. """
        return self.head == None

    def size(self) -> int:
        """ Returns length of this list. """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def append(self, value: Any) -> None:
        """ Adds new node with data set to <value>,
            placing it at end of list. """
        if self.is_empty() == False:
            current_tail = self.tail
            new_Node = Node(value, None, current_tail)
            current_tail.next = new_Node
            self.tail = new_Node
        else: 
            new_Node = Node(value, None, None)
            self.head = new_Node
            self.tail = new_Node


    def pop(self) -> Any:
        """ Removes/returns the list's last item. """
        assert not self.is_empty()     
        
        current_tail = self.tail
        before_tail = current_tail.prev
        if before_tail is not None:
            before_tail.next = None
        else:
            self.head = None
        self.tail = before_tail

        return current_tail.data

    def get_item(self, index: int) -> Any:
        """ Gets the value at the given index. """   
        curr = self.head
        i = 0

        while (curr is not None) and (i < index):
            curr = curr.next
            i += 1
            
        if curr == None:
            raise IndexError()
        else:
            return curr.data
    

l = DoublyLinkedList()
l.add(5)
l.add(-8.3)
l2 = DoublyLinkedList()
l2.add(5)
l2.add(90)
l2.append(16)
assert l2.get_item(0) == 90
assert l2.is_empty() == False
assert l2.size() == 3
assert (l2.pop() == 16)
assert l2.search(16) == False
assert l2.search(90) == True



def recursive_find(head:Optional['Node'], item:Any) -> bool:
    """ Returns true if the target is in the  
    list with the given head. """
    if head is None:
        return False
    elif head.data == item:
        return True
    else:
        return recursive_find(head.next, item) # recursive case
  
def recursive_get_item(head:Optional['Node'], index:int) -> Any:
    """ Returns item at the given index
    (relative to head). Raises IndexError
    if index is invalid. """
    if head is None:
        return False
    elif index == 0: #if you get to the index you want, return the data
        return head.data
    else:
        return recursive_get_item(head.next, index-1) # recursive case, this makes it so that you're looking for index[5], then [4], then [3], etc. until you get to the node you want, you move forward a head then subtract 1 from index

# Exercise 3:
"""
    Write a recursive function to subtract 100 from each item
    in the linked list.
"""
def recursion_100(head:Optional['Node']) -> None:
    ''' Subtracts 100 from each item in the list '''
    if head is None:
        return False
    else:
        head.data -= 100 # subtract 100 from the data for each node
        return recursion_100(head.next) 


# Exercise 4:
"""
    Write a recursive function to add all of the numbers
    to 1000. For example, if the list was 52 -> 104 -> 44,
    then this function should return 1200.
"""
def recursion_add(head:Optional['Node']) -> int:
    ''' add all of the numbers to 1000'''
    if head is None:
        return 1000 #once it hits the end of the list, return 1000 as well, which will go and add 1000 to the previous node's data
    else:
        return head.data + recursion_add(head.next) # add the data for each node to the next node's data