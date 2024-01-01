from tkinter import *

root = Tk()
root.title("PythonLobby")
w = Label(root, text='PythonLobby.Com', font="60")
w.pack()

Checkbox1 = IntVar()
Checkbox2 = IntVar()

Button0 = Checkbutton(root, text="Learning",
                      variable=Checkbox1,
                      onvalue=1,
                      offvalue=0,
                      height=3,
                      width=12)

Button1 = Checkbutton(root, text="Tutorial",
                      variable=Checkbox2,
                      onvalue=1,
                      offvalue=0,
                      height=3,
                      width=12)

Button0.pack()
Button1.pack()

root.geometry("320x220")
mainloop() 