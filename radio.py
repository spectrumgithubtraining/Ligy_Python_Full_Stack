# Importing Tkinter module
from tkinter import *

root = Tk()
root.title("PythonLobby")

# Tkinter string variable it can store any string value
value1 = StringVar(root, "2")

rbtn1 = Radiobutton(root, text="Radio Button 1", variable = value1 , value="1")
rbtn1.pack()
rbtn2 = Radiobutton(root, text="Radio Button 2", variable = value1 , value="2")
rbtn2.pack()
rbtn3 = Radiobutton(root, text="Radio Button 3", variable = value1 , value="3")
rbtn3.pack()

root.geometry("250x200")
mainloop()