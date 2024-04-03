# Question 1
"""
    Create a GUI that has the same layout as the picture shown
    in the "Quiz 3 GUI Layout" image (found in Quizzes Google Drive).
    Do not worry about getting the spacing exact, but I care that the
    widgets are oriented correctly to one another.   
"""

import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

# Create name label and entry
nameLabel = ttk.Label(window, text='Name:')
nameLabel.grid(row=0, column=0)

nameEntry = ttk.Entry(window)
nameEntry.grid(row=0, column=1)

# Create email label and entry
emailLabel = ttk.Label(window, text='Email:')
emailLabel.grid(row=1, column=0)

emailEntry = ttk.Entry(window)
emailEntry.grid(row=1, column=1)

# Create password label and entry
passwordLabel = ttk.Label(window, text='Password:')
passwordLabel.grid(row=2, column=0)

passwordEntry = ttk.Entry(window)
passwordEntry.grid(row=2, column=1)

window.mainloop()
