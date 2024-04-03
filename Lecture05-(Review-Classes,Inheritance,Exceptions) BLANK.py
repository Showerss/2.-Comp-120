# Exercise 1: (Classes)
"""
    Write a Python class named Rectangle constructed from length 
    and width and a method that will compute the 2d area of a rectangle.
"""

class Rectangle():
    """Docstring here"""
    #instance variables
    length: float
    width: float

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width
    
    def area(self) -> float:
        area = self.length * self.width
        print(area)        
        

# Exercise 2: (Inheritance)
"""
    Write a child class of rectangle, for a rectangular prism. 
    Add in an instance variable for depth and a method to find 
    the 3d area of the prism. 

    class Child(Parent)
    super().__init__(location) --- this calls the parent class constructor and pulls in some of the variables from the parent
"""
class rectangular_prism(Rectangle):

    height: float

    def __init__(self, width:int, length:int, height:int) -> None:
        super().__init__(length,width)
        self.height = height

    def get_3d_area(self) -> float:
        area = self.area() * self.height
        print(area)  

# Exercise 3:
"""
    Create both a rectangle and a rectangular prism.
    Find the 2d area of the rectangle and the rectangular prism.
    Find the 3d area of the rectangle and the rectangular prism.
"""

rectangley = Rectangle(1,2)
print(rectangley.area())


prismey = rectangular_prism(12,10,5)
print(prismey.area())
print(prismey.get_3d_area())


# Exercises to practice at home if you are struggling with these topics:
"""
Classes & Inheritance
    1) Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
        Perform the following tasks now:
        Now add items to the menu.
        Make table reservations.
        Take customer orders.
        Print the menu.
        Print table reservations.
        Print customer orders.
        Note: Use dictionaries and lists to store the data.

    2) Write a Python class BankAccount with attributes like account_number, 
    balance, date_of_opening and customer_name, and methods like deposit, withdraw, and 
    check_balance.
"""

