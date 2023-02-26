from tkinter import *


def click(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


root = Tk()


root.title("Abdullah")
root.iconbitmap('images/pic1.png')

var = StringVar()
var.set("a")

MODES = [("A", "a"), ("B", "b"), ("C", "c"), ("D", "d")]

for text, value in MODES:
    Radiobutton(root, text=text, variable=var, value=value, command=lambda: click(var.get())).pack()

mylabel = Label(root, text=var.get())
mylabel.pack()

root.mainloop()
