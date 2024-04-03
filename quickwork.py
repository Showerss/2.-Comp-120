import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x400")

def calculateAreaSquare():
    pass

def calculateAreaCircle():
    pass

def calculateAreaRectangle():
    pass

def calculateAreaTriangle():
    pass

param1Entry = tk.Entry(window)
param1Entry.pack()

param2Entry = tk.Entry(window)
param2Entry.pack()

param3Entry = tk.Entry(window)
param3Entry.pack()


window.bind('s', calculateAreaSquare)
window.bind('c', calculateAreaCircle)
window.bind('t', calculateAreaTriangle)
window.bind('r', calculateAreaRectangle)

window.mainloop()