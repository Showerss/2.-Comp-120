import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

def another():
    print(entry.get())

entry = tk.Entry(window)
entry.bind('<Return>', another)

f1 = ttk.Frame(window)
f1.pack()

entry.pack(in_=f1, side='left')

window.mainloop()



'''
sorting:
bubble - comparing adjacent items and swapping them if necessary
insertion - searching the sorted list for the correct place to insert the next number
selection - searching the unsorted list for the smallest number and moving it to the front of the list




searching:
binary - halving the list over and over comparing the midpoint to the target
linear - one at a time searching lists if the target is found or not






'''