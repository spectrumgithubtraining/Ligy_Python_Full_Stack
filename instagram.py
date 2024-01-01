import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Instagram UI")

# Logo
logo_label = ttk.Label(root, text="Instagram", bg font=('Arial', 20))
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Username Entry
username_label = ttk.Label(root, text="Username:")
username_label.grid(row=1, column=0, sticky='e', pady=5)
username_entry = ttk.Entry(root, width=20)
username_entry.grid(row=1, column=1, pady=5)

# Password Entry
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=2, column=0, sticky='e', pady=5)
password_entry = ttk.Entry(root, width=20, show='*')
password_entry.grid(row=2, column=1, pady=5)

# Login Button
login_button = ttk.Button(root, text="Login", command=lambda: print(f"Username: {username_entry.get()}\nPassword: {password_entry.get()}"))
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Register Link
register_label = ttk.Label(root, text="Don't have an account? Register here.")
register_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
