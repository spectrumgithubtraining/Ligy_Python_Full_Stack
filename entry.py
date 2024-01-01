# Entry Widget in GUI python
from tkinter import *

# creating root window
root = Tk()
root.title("Welcome to Python Lobby")

# placing Entry widget to our GUI app
entry = Entry(root)
entry.pack()

root.geometry('250x200')
root.mainloop()