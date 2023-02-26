from tkinter import *


def submit():
    print("Value  : " + str(scale.get()))


win = Tk()

scale = Scale(win, from_=100, to=0)
scale.pack()

button = Button(win, text="Ok", command=submit)
button.pack()

win.mainloop()
