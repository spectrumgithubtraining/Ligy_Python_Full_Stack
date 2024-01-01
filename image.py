# from tkinter import *
# root = Tk()

# img = PhotoImage(file="./download.jpg")
# l1=Label(root,image=img)


# mainloop()
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Frame Example")

# Create a frame
frame = tk.Frame(root, width=200, height=100, bg="lightblue")
frame.pack(padx=10, pady=10)

# Add widgets (buttons, labels, etc.) to the frame
label = tk.Label(frame, text="This is a label inside the frame")
label.pack()

button = tk.Button(frame, text="Click me!")
button.pack()

# Start the Tkinter event loop
root.mainloop()
