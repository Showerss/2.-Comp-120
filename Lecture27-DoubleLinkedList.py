'''
double linked lsit  - able to move both ways
    - each node has a reference to the next and previous node
    - append is much faster
    - pop is much faster
    - get_item is much faster
    - better at queues, because queues use both ends of the list


linked list - great type complexity
            - not great for random access, stakcs, queues
            - not great for searching
            - great for insertion and deletion
            - better for stacks, because stacks only use one end of the list (the beginning) because we add to the front

'''

from typing import Any, Optional

# Exercise 1:
"""
    You have been provided the node class and LinkedList class
    that we wrote together in class. Now let's edit our code to
    be a doubly linked list, and edit any of our methods to make
    them the most efficient as possible
"""
class Node:
    data: Any
    next: Optional['Node'] # tricky: use quotes around type
    prev: Optional['Node']

    def __init__(self, data: Any, next: Optional['Node'], prev: Optional['Node']):
      self.data = data
      self.next = next
      self.prev = prev

    def __str__(self):
        """
        Return a user-friendly representation of LinkedListNode self
        """
        current = self
        s = ""
        while current is not None:
            s += "{} ->".format(current.data)
            current = current.next
        s += "|"
        return s 
    
    def __eq__(self, other):
        current_self = self
        current_other = other
        while type(current_self) is type(current_other) and \
                current_self and current_other and \
                        current_self.data == current_other.data:
            current_self = current_self.next
            current_other = current_other.next
        if not current_self and not current_other:
            return True
        else:
            return False

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        """ Returns length of list. """
        current = self.head # set to first item
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count
    
    def __str__(self):
        return str(self.head)
    
    def __contains__(self, value: Any) -> bool:
        """ Returns True if <value> is stored
          as data in this list. """
        current = self.head
        if current.data == value:
            return True
        while current.next is not None:
            if current.next.data == value:
                return True
            current = current.next

        return False

    def __eq__(self, other):
        return (type(self) is type(other) and
                (self.size(), self.head, self.tail, self.get_item(len(self)-1)) ==
                (other.size(), other.head, other.tail, other.get_item(len(other)-1)))

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
        if self.is_empty():
            new_node = Node(data, None, None)
            self.head = new_node
            self.tail = new_node

        else:
            new_node = Node(data, self.head, None)
            self.head.prev = new_node
            self.head = new_node

        new_node = Node(data, self.head)
        self.head = new_node

    def is_empty(self):
        """ Returns true if list is empty,
          False otherwise. """
        #could change this to self.tail?
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
        
        if self.head is None: # empty list case
            new_node = (value, None, None)
            self.head = new_node
            self.tail = new_node

        else:
            current_tail = self.tail
            new_node = Node(value, None, current_tail)
            current_tail = new_node
            self.tail = new_node

        # new_node = Node(value, None)
        
        # if self.head is None: # empty list case
        #     self.head = new_node
        # else:
        #     curr = self.head
        #     prev = None
        #     while curr is not None:
        #         prev = curr
        #         curr = curr.next

        #     prev.next = new_node

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

        # curr = self.head
        # prev = None

        # while curr.next is not None:
        #     prev = curr
        #     curr = curr.next
            
        # prev.next = None
        # return curr.data

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


l = LinkedList()
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
assert l != l2