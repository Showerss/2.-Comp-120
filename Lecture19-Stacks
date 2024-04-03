'''
ADT - abstract data type

aka... data structures


all data structures will have every single one of the things that the ADT will have in totality
very similar to parent/child classes
    ADT will be the parent
    data structures will be the children

ADT examples
    list - array, an unordered collection of items
        data type would be
            dynamic array
            linked list

    map - dictionary, a collection of key-value pairs


    stack - a collection of items with a last in first out policy


    set
        data types would be
            hash set
            tree set

            
    queue

    

    
---------

Stacks - last in first out
    uses pop, push, peek, 

Queue - first in first out
    uses enqueue, dequeue, peek, first, last
        enqueue adds to the queue (in the back)
        dequeue removes from the queue (from the front)



'''



from abc import ABC, abstractmethod 

# Exercise 1
"""
    Below is a simple creation of an abstract data type. 
    Part A: Add a Traiangle Data Structure to the code
    Part B: Create an instance of the pentagon and call it's method
"""  
  
class Polygon(ABC): #you inherit from ABC when doing abstract data types
    @abstractmethod #you need this before you do any functions
    def noofsides(self): 
        pass
  
class Pentagon(Polygon): #this is a datastructure that is inheriting from the abstract data type
    # overriding abstract method 
    def noofsides(self):  #i have to have this because it was in the abstract data type
        print("I have 5 sides") 
  
class Hexagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides") 

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
  
# Driver code 
  
K = Quadrilateral() 
K.noofsides() 
  
K = Hexagon() 
K.noofsides()

Q = Quadrilateral()
Q.noofsides()

T = Triangle()
T.noofsides()



# Exercise 2:
"""
    The below code shows the creation of four data structures. 
    Write an abstract data type that all of these data structures are
    created from (all of the information you need to know for this is 
    shown in the code below) 
"""  
  
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal): 
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
    def move(self): 
        print("I can crawl") 
  
class Dog(Animal): 
    def move(self): 
        print("I can bark") 
  
class Lion(Animal): 
    def move(self): 
        print("I can roar") 

# Driver code 
R = Human() 
R.move() 
  
K = Snake() 
K.move() 
  
R = Dog() 
R.move() 
  
K = Lion() 
K.move() 

# Exercise 3:
"""
    Explain why the below line of code does not work. If you would like,
    make it live and see what error gets thrown
"""
# c=Animal() 
#this doesnt work because you cant make a initializer of a data type, you could do the structure/children, but not the type

# Exercise 4
"""
    Below is the entire code for an abstract data type called Agenda (the exact same one you will see in PSA3). 
    I have started to write the abstract data structure for ListAgenda
    Write the rest of the ListAgenda Class with full functionality. 
    This should include writing all 5 methods and their implementation when considering a list.
"""
from abc import ABC, abstractmethod
from typing import Any
import random

class Agenda(ABC):
    """Parent/base class for all classes that will implement the Agenda ADT.

    DO NOT MODIFY THIS CLASS IN ANY WAY."""

    @abstractmethod
    def add(self, item: Any) -> None:
        """Adds an item to the agenda."""
        return

    @abstractmethod
    def remove(self) -> Any:
        """Removes and returns the first item on the agenda."""
        return

    @abstractmethod
    def next(self) -> Any:
        """Returns the first item on the agenda."""
        return

    @abstractmethod
    def size(self) -> int:
        """Returns the number of items on the agenda."""
        return 0

    @abstractmethod
    def is_empty(self) -> bool:
        """Returns True if the agenda has no items, and False otherwise."""
        return False

class AgendaEmpty(Exception):
    pass

class ListAgenda(Agenda):
    def __init__(self):
        self.random_nums = []
        for i in range(20):
            self.random_nums.append(random.randint(-100,100))

    def add(self, item: Any):
        return self.random_nums.append(item)
        
    def remove(self):
        return self.random_nums.remove()

    def next(self):
        return self.random_nums[0]

    def size(self):
        return len(self.random_nums)
    
    def is_empty(self):
        return self.random_nums == []

    