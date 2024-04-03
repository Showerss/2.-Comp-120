"""
event driven programming: uses an event loop to keep a window open
functional programming: uses name of functions as parameters

4 main steps to creating a gui:
    1. create widgets and orient them
    2. define the functions for when a user clicks a widget
    3. assosciate user events with functions
    4. start an infinite event loop that runs until the user chooses to end the program 'x'

    while True:
        event = get_next_event()
        if event == EXIT: 
            break
        
buttons dont get attached until you place them

you can use frames within windows

        
"""


# Exercise 1:
"""
    Build a simple graphical interface, with one Label, Entry, and Button.
    Use the pack method to build the graphic with all components in the same row.
"""
import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

# Create the user interface
testButton = ttk.Button(window, text='Modern Button')
testButton.pack(side='left')

testLabel = ttk.Label(window, text='Hello!')
testLabel.pack()

testEntry = ttk.Entry(window)
testEntry.pack()


# start the event loop
window.mainloop() 


# Exercise 2:
"""
    Build a graphical interface like the image shown on the slides. 
    Use the grid method
"""
import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

# Create the user interface
Uno = ttk.Button(window, text='uno')
# Uno.grid(row=0, column=0)
Uno.pack(side='left')

Dos = ttk.Button(window, text='dos')
# Dos.grid(row=0, column=1)
Dos.pack(side='left')

Tres = ttk.Button(window, text='tres')
# Tres.grid(row=1, column=0)
Tres.pack(side='right')

Quatro = ttk.Button(window, text='quatro')
# Quatro.grid(row=1, column=1)
Quatro.pack()


window.mainloop() 



# Exercise 3:
"""
    Build a graphical interface like the image shown on the slides. 
    Use different frames and the grid method
"""
import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

# Create first frame
first_row = ttk.Frame(window)
first_row.pack()

label1 = ttk.Label(first_row, text='First frame')
label1.pack(side='left')

entry1 = ttk.Entry(first_row)
entry1.pack(side='left')

button1 = ttk.Button(first_row, text='uno')
button1.pack(side='left')




###############################
##### second frame below ######

second_row = ttk.Frame(window)
second_row.pack()

label2 = ttk.Label(second_row, text='second frame')
label2.pack(side='left')

entry2 = ttk.Entry(second_row)
entry2.pack(side='left')

button2 = ttk.Button(second_row, text='dos')
button2.pack(side='left')

window.mainloop() 