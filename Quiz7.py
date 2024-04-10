# Question 1: 
"""
    Explain what a linked list is, in your own words.
    Be sure to include the role of the LinkedList class, 
    the Node Class, and how the data in the LinkedList is
    connected. 
"""
# a linked list is a data structure that is made up of nodes that are connected to each other.
# the node can be broken into 2 parts, the data/value and the .next which is a reference to the next node in the list.
#

# Question 2:
"""
    Using the below linked list class, create a linked list
    with the following three pieces of data in it ("hi"-> "hello"-> "you").
    To do this, you can use the built in methods already provided.
    Once you have this linked list, write code to delete 
    the first item from your singly linked list, namely the "hi". There is no
    built-in method to do this, so you will need to code it yourself.
"""

from typing import Any, Optional

class Node:
    data: Any
    next: Optional['Node'] # tricky: use quotes around type

    def __init__(self, data: Any, next: Optional['Node']):
      self.data = data
      self.next = next     

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data: Any):
        """ Adds new node containing data to
          front of this list. """
        new_node = Node(data, self.head)
        self.head = new_node

    def is_empty(self):
        """ Returns true if list is empty,
          False otherwise. """
        return self.head == None
    
# Create your linked list with the ("hi", "hello", "you") data here

# Delete the first item of the list here