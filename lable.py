#Labels in Tkinter
from tkinter import *

# creating root window
root = Tk()

# customizing root window title
root.title("Welcome to Python Lobby")
# customizing root window dimension
root.geometry('250x200')

# placing label to our GUI app
lbl = Label(root, text = "We are Python Lobby-ian")
lbl.pack()

root.mainloop()