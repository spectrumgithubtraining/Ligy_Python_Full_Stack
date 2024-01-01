from tkinter import *
#setting up parent window
root = Tk()

canvas = Canvas(root, bg="yellow", width=150, height=250)
canvas.pack()
line = canvas.create_line(70,150,140,5)

root.geometry("350x220")
root.title("PythonLobby.com")
root.mainloop()



from tkinter import *
#setting up parent window
root = Tk()

canvas = Canvas(root, bg="yellow", width=150, height=250)
canvas.pack()
rectangle= canvas.create_rectangle(30,20,140,90, fill="light green")
root.geometry("350x220")
root.title("PythonLobby.com")
root.mainloop()


from tkinter import *
#setting up parent window
root = Tk()

canvas = Canvas(root, bg="yellow", width=150, height=250)
canvas.pack()
rectangle= canvas.create_oval(30,20,140,90, fill="light green")
root.geometry("350x220")
root.title("PythonLobby.com")
root.mainloop()