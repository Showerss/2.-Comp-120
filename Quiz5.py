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
    def is_square(self) -> bool:
        """" Determines if the rectangle is a square an returns a boolean""" 
        return False

    @abstractmethod
    def get_area(self) -> float: 
        """ Caluclates and returns the area of the rectangle""" 
        return self.length * self.width # i had to rewrite this instead of 0.0 because I chose to use this below and im too lazy to change the code below 

    @abstractmethod
    def increase_length(self, amount: Any) -> float: 
        """ Increases the length of the rectangle and returns the new length""" 
        return 0.0
    
    @abstractmethod
    def scale(self, factor: int) -> None: 
        """ Scales the length and width of the rectangle based on the factor""" 
        pass

class RectangleA(Rectangle): # i have to define my data structure below passing in the parameter the data type from above i made
    ''' Creation of a RectangleA Data Structure from the rectangle data type'''
    def __init__(self, length:float, width:float): #initialize the variables that could (in this case will) be used below
        self.length = length
        self.width = width

    
    # below we have to re-state all @abstractmethods below because every data structure needs the same methods within the type
    # without exception 

    def is_square(self) -> bool: 
        return super().is_square()
    
    def get_area(self) -> float: 
        return super().get_area()
    
    def increase_length(self, amount: Any) -> float: #even the type hints should be copied from above to keep the code as similar as possible
        return super().increase_length(amount)
    
    def scale(self, factor: int) -> None:
        return super().scale(factor)
    

R = RectangleA(5,3) #we need to create an instance of the data structure, i'll assign it to R, I also will have to pass it variables to satisfy the init valued (length/width) since i'll be using that function later
print(R.get_area()) #print out the area, it'll do 5*3 as was passed in the constructor above, i don't have to re-state them here because get_area doesnt take any params, only inherits them from the __init__
  