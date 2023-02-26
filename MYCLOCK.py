from tkinter import *
from time import *


def update():
    time_string = strftime("%I : %M : %S %p")
    time_label.config(text=time_string)

    time_zone_string = strftime("%Z")
    time_zone_label.config(text=time_zone_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    month_string = strftime("%B")
    month_label.config(text=month_string)

    date_string = strftime("%x")
    date_label.config(text=date_string)

    time_label.after(1000, update)


win = Tk()

win.config(bg="black")

time_zone_label = Label(win, fg="black", bg="white", padx=68, pady=20, bd=10, font=('Arial', 30, 'bold'), relief=GROOVE)
time_zone_label.grid(row=0, column=0, columnspan=2, rowspan=1)

time_label = Label(win, fg="black", bg="white", padx=60, pady=20, bd=10, font=('Arial', 50, 'bold'), relief=GROOVE)
time_label.grid(row=1, column=0, columnspan=2, rowspan=1)

date_label = Label(win, fg="black", bg="white", padx=163, pady=20, bd=10, font=('Arial', 50, 'bold'), relief=GROOVE)
date_label.grid(row=2, column=0, columnspan=2, rowspan=1)

month_label = Label(win, fg="black", bg="white", padx=18, pady=20, bd=10, font=('Arial', 50, 'bold'), relief=GROOVE)
month_label.grid(row=3, column=0, columnspan=1, rowspan=1)

day_label = Label(win, fg="black", bg="white", padx=18, pady=20, bd=10, font=('Arial', 50, 'bold'), relief=GROOVE)
day_label.grid(row=3, column=1, columnspan=1, rowspan=1)

update()

win.mainloop()
