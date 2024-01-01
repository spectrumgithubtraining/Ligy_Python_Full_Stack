#Button in python GUI
from tkinter import *

# creating root window
root = Tk()
root.title("Welcome to Python Lobby")
# function defined which is called when button is clicked
def clicked():
    print("I am clicked")
# placing Button to our GUI app
btn = Button(root, text="Click me", command = clicked)
btn.pack()
root.geometry('250x200')
root.mainloop()