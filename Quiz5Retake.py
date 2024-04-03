from abc import ABC, abstractmethod
from typing import Any 

# Question 1
"""
    Below is a simple creation of an abstract data type. 
    Part A: Add a RectangleA Data Structure to the code. To do this, I suggest having the following instance variables: length and width
    Part B: Create an instance of the RectangleA and call one of it's method (any of them are fine - I just want to know you can do it)
"""  
  
class Rectangle(ABC): 
    @abstractmethod
    def __init__(self, length:float, width:float):
        """" Determines if the rectangle is a square an returns a boolean""" 
        return

    @abstractmethod
    def is_length_greater_than_width(self) -> bool:
        """" Determines if the rectangle has a larger length 
        than width and returns a boolean""" 
        pass

    @abstractmethod
    def get_length(self) -> float: 
        """ Returns the length of the rectangle""" 
        pass

    @abstractmethod
    def decrease_width(self, amount: Any) -> float: 
        """ Decreases the width of the rectangle and returns the new width""" 
        pass
    
    @abstractmethod
    def shrink(self, factor: int) -> None: 
        """ Shrinks the length and width of the rectangle based on the factor""" 
        pass

class RectangleA(Rectangle):
    ''' Creation of a RectangleA Data Structure from the rectangle data type'''
    def __init__(self, length:float, width:float): #initialize the variables that could (in this case will) be used below
        self.length = length
        self.width = width
    
    # below we have to re-state all @abstractmethods below because every data structure needs the same methods within the type
    def is_length_greater_than_width(self) -> bool: 
        """" Determines if the rectangle has a larger length 
        than width and returns a boolean""" 
        return self.length > self.width
    
    def get_length(self) -> float:
        """ Returns the length of the rectangle""" 
        return self.length
    
    def decrease_width(self, amount: Any) -> float:
        """ Decreases the width of the rectangle and returns the new width""" 
        self.width = self.width - amount
        return self.width
    
    def shrink(self, factor: int) -> None:
        """ Shrinks the length and width of the rectangle based on the factor""" 
        self.length = self.length / factor
        self.width = self.width / factor #this will actually return 1.5 because of the decrease width setting width to 3 then halving that.
        return None
    
R = RectangleA(10,5) #we need to create an instance of the data structure, i'll assign it to R, I also will have to pass it variables to satisfy the init valued (length/width) since i'll be using them below 


#the 4 functions 
print(R.is_length_greater_than_width()) #I'll call the is_length_greater_than_width method to see if it returns true or false
print(R.get_length()) #I'll call the get_length method to see if it returns the length of the rectangle
print(R.decrease_width(2)) #I'll call the decrease_width method to see if it returns the new width of the rectangle, i'll do 2 and expect a 3 return
print(R.shrink(2)) #I'll call the shrink method to see if it returns the new length and width of the rectangle
        