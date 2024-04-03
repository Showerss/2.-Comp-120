"""
quit_button['command'] = window.destroy


----- 
def set_message():
    message_label['text'] = textbox.get() #this gets whatever a user inputs into an entrybox

def clear_message():
    message_label['text'] = ''

submit_button['command'] = set_message #set_message in this case is referred to as a 'callable'

------
def my_function():
    print("my function was called")

my_button = tk.Button(application_window, text='Example', command=my_function)



"""



# Exercise 1:
"""
    Develop a GUI interface for a tip calculator. 
    Use the following criteria when developing:
        - Allow entry of bill amount
        - Buttons for common tip amounts: 0%, 15%, 20%, 25%
        - Display the tip amount (which will be based on the bill amount and the tip amount)
        - Have a spot to display a message (e.g. if they don't enter a number into the bill amount)
        - Simple design: single window; only labels, buttons, and text entry widgets; no menus
"""
import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

""" Creates the layout. """



window.mainloop()

# Exercise 2:
"""
    Add a button widget that is associated with the append7 function.
    Try to do this three different ways
"""
import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()
window.title('life is torture ')


def append7():
  display['text'] += 7

display = tk.Label(window, text=0)
display.pack()

# Option 1 - oneline
button5 = ttk.Button(window, text='5', command=append7)
button5.pack()

# Option 2 - dict typing
button10 = ttk.Button(window, text='10')
button10.pack()
button10['command'] = append7

# Option 3 - weird way 
button15 = ttk.Button(window, text='15')
button15.pack()
button15.configure(command=append7)

window.mainloop()



# Exercise 3:
"""
    Add type hints to the below function
"""
from collections.abc import Callable

def apply_func(func:Callable[[str],tuple[str,str]], value:str) -> tuple[str,str]:
    return func(value) #this means that this functions returns another functions value

def parse_email(email_address:str) -> tuple[str, str]:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username, domain
    return "", ""

apply_func(parse_email, "claudia@realpython.com")


# Exercise 4
"""
    If time allows, add the following two functions 
    to your tip calculator.
    -> A calculate function that takes in two floats (bill amount and tip percentage) and calculates the tip amount
    -> A set_tip0 function that is associated with your 0% button 
       and takes in no parameters, but displays the tip amount in your GUI 
"""