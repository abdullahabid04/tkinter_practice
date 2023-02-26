from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


window = Tk()

txt = "______________________________________________________"
TXT = "___________________"

varAcceptButton = IntVar()

cb1 = IntVar()
cb2 = IntVar()
cb3 = IntVar()
cb4 = IntVar()
cb5 = IntVar()
cb6 = IntVar()
cb7 = IntVar()
cb8 = IntVar()
cb9 = IntVar()
cb10 = IntVar()

rb = IntVar()


def accept_function():
    Button(win2, text="next", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
           activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
           height=1, width=7, command=lambda: add_win(2)).place(x=500, y=525)


def add_win(x):
    noteBook.add(win_list[x], text=texts[x])
    noteBook.hide(win_list[x - 1])


def back_win(x):
    noteBook.add(win_list[x - 1], text=texts[x - 1])
    noteBook.hide(win_list[x])


img = ImageTk.PhotoImage(Image.open("images/white.png"))

window.geometry("600x600")
window.config(bg="black")
window.title("Setup Installation Wizard")
window.iconphoto(window, img)

noteBook = ttk.Notebook(window)

win1 = Frame(noteBook, bg="light blue")
win2 = Frame(noteBook, bg="light blue")
win3 = Frame(noteBook, bg="light blue")
win4 = Frame(noteBook, bg="light blue")
win5 = Frame(noteBook, bg="light blue")

noteBook.add(win1, text="win 1")

noteBook.pack(expand=True, fill="both")

win_list = [win1, win2, win3, win4, win5, win1]
texts = ["win 1", "win 2", "win 3", "win 4", "win 5"]

Label(win1, image=img).place(x=-900, y=0)
Label(win2, image=img).place(x=-900, y=0)
Label(win3, image=img).place(x=-900, y=0)
Label(win4, image=img).place(x=-900, y=0)
Label(win5, image=img).place(x=-900, y=0)

Button(win1, text="next", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=lambda: add_win(1)).place(x=500, y=525)
Button(win1, text="back", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=DISABLED,
       height=1, width=7, command=lambda: back_win(0)).place(x=350, y=525)
Button(win1, text="exit", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=window.quit).place(x=425, y=525)
Button(win2, text="next", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=DISABLED,
       height=1, width=7, command=lambda: add_win(2)).place(x=500, y=525)
Button(win2, text="back", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=lambda: back_win(1)).place(x=350, y=525)
Button(win2, text="exit", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=window.quit).place(x=425, y=525)
Button(win3, text="Browse", font=("Arial", 9), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=window.quit).place(x=530, y=350)
Button(win3, text="next", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=lambda: add_win(3)).place(x=500, y=525)
Button(win3, text="back", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=lambda: back_win(2)).place(x=350, y=525)
Button(win3, text="exit", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=window.quit).place(x=425, y=525)
Button(win4, text="next", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=lambda: add_win(4)).place(x=500, y=525)
Button(win4, text="back", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=lambda: back_win(3)).place(x=350, y=525)
Button(win4, text="exit", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=window.quit).place(x=425, y=525)
Button(win5, text="back", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=lambda: back_win(4)).place(x=350, y=525)
Button(win5, text="exit", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=window.quit).place(x=425, y=525)
Button(win5, text="finish", font=("Arial", 10, "bold"), padx=1, pady=1, bg="Blue", fg="Green",
       activebackground="Blue", activeforeground="Green", bd=1, relief=GROOVE, state=ACTIVE,
       height=1, width=7, command=window.quit).place(x=500, y=525)

Label(win1, text="Welcome to the Setup Installation Wizard", font=("Arial", 15, "bold"),
      bg="light blue", fg="blue", padx=5, pady=5).place(x=150, y=50)
Label(win1, text=txt, font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5
      ).place(x=150, y=100)
Label(win1, text=txt, font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5
      ).place(x=150, y=125)
Label(win1, text=txt, font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5
      ).place(x=150, y=150)
Label(win2, text="I accept license agreements", font=("Arial", 9, "bold"), bg="light blue", fg="blue",
      padx=5, pady=5).place(x=180, y=422)
for i in range(1, 15):
    Label(win2, text=txt, font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5
          ).place(x=150, y=i * 25)
Label(win3, text=txt, font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5
      ).place(x=150, y=100)
Label(win3, text=txt, font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5
      ).place(x=150, y=125)
Label(win3, text=txt, font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5
      ).place(x=150, y=150)
Label(win3, text="Browse a location where you want to install the setup",
      font=("Arial", 9, "bold"), bg="light blue", fg="blue", padx=5, pady=5).place(x=150, y=300)
Label(win4, text="Selection Menu", font=("Arial", 15, "bold"), bg="light blue", fg="blue",
      padx=5, pady=5).place(x=300, y=60)

location = Entry(win3, font=("Arial", 10, "bold"), bg="White", fg="Black", bd=3, width=50)
location.place(x=150, y=350)
location.insert(0, "Location")

acceptButton = Checkbutton(win2, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=varAcceptButton, onvalue=1, offvalue=0,
                           command=accept_function)
buttonCheck1 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb1, onvalue=1, offvalue=0)
buttonCheck2 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb2, onvalue=1, offvalue=0)
buttonCheck3 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb3, onvalue=1, offvalue=0)
buttonCheck4 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb4, onvalue=1, offvalue=0)
buttonCheck5 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb5, onvalue=1, offvalue=0)
buttonCheck6 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb6, onvalue=1, offvalue=0)
buttonCheck7 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb7, onvalue=1, offvalue=0)
buttonCheck8 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb8, onvalue=1, offvalue=0)
buttonCheck9 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1,
                           height=1, width=1, variable=cb9, onvalue=1, offvalue=0)
buttonCheck10 = Checkbutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                            activebackground="light blue", bd=1, padx=1, pady=1,
                            height=1, width=1, variable=cb10, onvalue=1, offvalue=0)

acceptButton.place(x=150, y=425)
buttonCheck1.place(x=150, y=125)
buttonCheck2.place(x=150, y=150)
buttonCheck3.place(x=150, y=175)
buttonCheck4.place(x=150, y=200)
buttonCheck5.place(x=150, y=225)
buttonCheck6.place(x=150, y=250)
buttonCheck7.place(x=150, y=275)
buttonCheck8.place(x=150, y=300)
buttonCheck9.place(x=150, y=325)
buttonCheck10.place(x=150, y=350)

buttonRadio1 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=1)
buttonRadio2 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=2)
buttonRadio3 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=3)
buttonRadio4 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=4)
buttonRadio5 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=5)
buttonRadio6 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=6)
buttonRadio7 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=7)
buttonRadio8 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=8)
buttonRadio9 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                           activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                           width=1, variable=rb, value=9)
buttonRadio10 = Radiobutton(win4, fg="blue", bg="light blue", activeforeground="blue",
                            activebackground="light blue", bd=1, padx=1, pady=1, height=1,
                            width=1, variable=rb, value=10)

buttonRadio1.place(x=400, y=125)
buttonRadio2.place(x=400, y=150)
buttonRadio3.place(x=400, y=175)
buttonRadio4.place(x=400, y=200)
buttonRadio5.place(x=400, y=225)
buttonRadio6.place(x=400, y=250)
buttonRadio7.place(x=400, y=275)
buttonRadio8.place(x=400, y=300)
buttonRadio9.place(x=400, y=325)
buttonRadio10.place(x=400, y=350)

window.mainloop()
