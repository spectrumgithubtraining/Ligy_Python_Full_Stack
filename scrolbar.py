from tkinter import *
#setting up parent window
root = Tk()

textbox=Text(root, width=40, height=13, wrap=WORD)
textbox.grid(row=0, column=0)

scroll=Scrollbar(root, orient=VERTICAL, command= textbox.yview)
scroll.grid(row=0, column=1, sticky=N+S)
textbox.config(yscrollcommand=scroll.set)

root.geometry("350x220")
root.title("PythonLobby.com")
root.mainloop()