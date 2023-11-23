import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and result
entry = tk.Entry(root, width=20, font=("Helvetica", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 14),
              command=lambda btn=button: entry.insert(tk.END, btn) if btn != '=' else entry.insert(tk.END, eval(entry.get()))).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text="C", padx=20, pady=20, font=("Helvetica", 14), command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)

# Start the Tkinter event loop
root.mainloop()
