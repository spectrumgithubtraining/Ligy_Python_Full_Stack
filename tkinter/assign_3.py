import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Label Configuration Example")

# Configure Label widget with various options
label = tk.Label(root, text="Hello, Tkinter!", bg="red", font=("Times New Roman", 18))
label.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()
