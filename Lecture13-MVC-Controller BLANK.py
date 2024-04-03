"""
MVC (model view controller)
    model/view/controller are each their own class
    model - handles data logic, calculate, access data in some way (can call a database)
    view - handles data presentation, showing a message, emptying a box etc
    controller - request flow/ user insteraction, never handles data logic, just request/response

command  callable cannot be sent parameters... dont user functions that have params
.get returns as a str

bind
    - bind a key to a function
    my_button.bind("<Button-1>", my_function)
    - callable HAS to have a parameter named event: tk.Event
"""





# Exercise 1:
"""
    Use the method discussed in class to reduce the redundant code below
"""
import tkinter as tk # traditional look
from tkinter import ttk # modern look
from typing import Callable, Optional

# Create the application window
window = tk.Tk()

bill_amt = ttk.Entry(window)
tip0_button = ttk.Button(window, text="0%")
tip15_button = ttk.Button(window, text="15%")
tip20_button = ttk.Button(window, text="20%")
tip25_button = ttk.Button(window, text="25%")
ta_label = ttk.Label(window, text="-")
message_label = ttk.Label(window, text="")
bill_amt.pack()
tip0_button.pack()
tip15_button.pack()
tip20_button.pack()
tip25_button.pack()
ta_label.pack()
message_label.pack()

def calculate(bill: float, tip: float) -> float:
    return bill * tip

def set_tip(tip_percent: float) -> Callable[[],None]:
    def set_tip_inner():
        tip = calculate(float(bill_amt.get()), tip_percent)
        ta_label['text'] = f"${tip:.2f}"
    return set_tip_inner

# def set_tip15():
#     tip = calculate(float(bill_amt.get()), 0.15)
#     ta_label['text'] = f"${tip:.2f}"

# def set_tip20():
#     tip = calculate(float(bill_amt.get()), 0.20)
#     ta_label['text'] = f"${tip:.2f}"

# def set_tip25():
#     tip = calculate(float(bill_amt.get()), 0.25)
#     ta_label['text'] = f"${tip:.2f}"

# def final_tip():
#     tip = calculate(float(bill_amt.get()), float(tip))
#     ta_label['text'] = f"${tip:.2f}"

tip0_button['command'] = set_tip(0)
tip15_button['command'] = set_tip(15)
tip20_button['command'] = set_tip(20)
tip25_button['command'] = set_tip(25)


# Exercise 2
"""
    Use the bind operand to make it such that:
    - if I type in the - button on my keyboard, display a message about no negative numbers being accepted
    - if I type in the Enter button on my keyboard, then calculate the tip for 18%
    - if I type in the ? button on my keyboard, a helpful message appears


"""

def negativenumbers(event:tk.Event) -> None:
    """
    Displays a message of the negative numbers
    
    Params: 
        event: 
        
    returns: 
        None
        
    """
    ta_label['text'] = 'No negative numbers accepted for the bill!'

def calculate18tip(event:tk.Event) -> None:
    """
    Calculates a tip based on 18% of the bill
    
    Params:
        event
        
    Returns: 
        None
    """
    ta_label['text'] = float(bill_amt.get()) * 0.18

def helpme(event:tk.Event) -> None:
    """
    Displays a help message box when hitting the ? button
    
    Params:
        event:
    
    Returns:
        None
    """
    


window.bind('-', negativenumbers)

window.bind('<Return>', calculate18tip)

window.bind('?', helpme)


window.mainloop()
