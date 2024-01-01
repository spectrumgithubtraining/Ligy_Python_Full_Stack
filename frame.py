from tkinter import *

def change_button_label():
    current_label = button["text"]
    new_label = "Clicked!" if current_label == "Click Me" else "Click Me"
    button["text"] = new_label

# Root window
root = Tk()

# Frame
frame = Frame(root, bg="lightblue", width=200, height=100)
frame.pack(pady=20)

# Button inside the frame
button = Button(frame, text="Click Me", command=change_button_label)
button.pack(pady=10)

# Set the initial size of the window
root.geometry("250x150")

# Start the Tkinter event loop
root.mainloop()

