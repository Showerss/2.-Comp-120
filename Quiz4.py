# Question 1
"""
    Use the existing GUI code below and add the following functionality to it:
    - if the "append_hi" button is pressed, add "hi" to the current label text
    - if the "clear" button is pressed, clear out the current label text
    - if the "add_number" button is pressed, add the number that was entered into the entry box to the end of the current label text
"""
import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

# Create the user interface
hw = ttk.Label(window, text="Start")


textbox = ttk.Entry(window)


def append_hi(): #we have to add a function with no params to be able to use it as a command for a button press
    """
    Appends hi to the end of the current label

    Params:
    None

    Returns:
    None

    """
    hw['text'] += "hi" #this adds a 'hi' onto the end of the label, no matter whats in the entrybox

append_hi = ttk.Button(window, text="Append Hi", command=append_hi) #we also have to edit the button to accept the command of the new function


def clear2(): #we have to add a function with no params to be able to use it as a command for a button press
    """
    This clears out the label no matter whats in the entrybox

    Params:
    None

    Returns:
    None

    """
    hw['text'] = '' #this replaces the hw label with an empty str, no matter whats in the entrybox

clear = ttk.Button(window, text="Clear")
clear['command'] = clear2 #well, we talked about this


def add_number(): #we have to add a function with no params to be able to use it as a command for a button press
    """
    Appends the current entrybox to the end of the current label

    Params:
    None

    Returns:
    None

    """
    
    hw['text'] += " " + textbox.get() # this will put a space between the current hw text and then add whatever is in the textbox to the end of it, we prefer a number but i didnt make the logic for it to only be numbers
add_number = ttk.Button(window, text="Add Entered Number", command=add_number) #same as above, have the button accept the command of the function we just mde



hw.grid(row=0, column=0) # first_row uses grid
textbox.grid(row=0, column=1)
append_hi.grid(row=1, column=0)
clear.grid(row=1, column=1)
add_number.grid(row=1, column=2)





window.mainloop()