import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("User Input Printer")

# Create an Entry widget for user input
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=10)

# Create a Button to print user input
print_button = tk.Button(root, text="Print Input", command=lambda: text_area.insert(tk.END, f"{entry.get()}\n"), font=("Helvetica", 12))
print_button.pack(pady=10)

# Create a Text widget to display printed data
text_area = tk.Text(root, width=40, height=10, font=("Helvetica", 12))
text_area.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
