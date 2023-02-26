from tkinter import *


Calc = Tk()
Calc.title("CALCULATOR")
Calc.config(bg="black")
entry = Entry(Calc, width=35, borderwidth=5, bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)


def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)


def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, int(f_num + int(second_number)))
    if math == "subtraction":
        entry.insert(0, int(f_num - int(second_number)))
    if math == "multiplication":
        entry.insert(0, int(f_num * int(second_number)))
    if math == "division":
        entry.insert(0, int(f_num / int(second_number)))


def button_clear():
    entry.delete(0, END)


button_1 = Button(Calc, text="1", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(1))
button_2 = Button(Calc, text="2", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(2))
button_3 = Button(Calc, text="3", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(3))
button_4 = Button(Calc, text="4", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(4))
button_5 = Button(Calc, text="5", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(5))
button_6 = Button(Calc, text="6", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(6))
button_7 = Button(Calc, text="7", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(7))
button_8 = Button(Calc, text="8", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(8))
button_9 = Button(Calc, text="9", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(9))
button_0 = Button(Calc, text="0", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(0))
button_add = Button(Calc, text="+", padx=39, pady=20, fg="white", bg="black", command=button_add)
button_subtract = Button(Calc, text="-", padx=40, pady=20, fg="white", bg="black", command=button_subtract)
button_multiply = Button(Calc, text="X", padx=40, pady=20, fg="white", bg="black", command=button_multiply)
button_divide = Button(Calc, text="/", padx=40, pady=20, fg="white", bg="black", command=button_divide)
button_equal = Button(Calc, text="=", padx=87, pady=20, fg="white", bg="black", command=button_equal)
button_clear = Button(Calc, text="Clear", padx=77, pady=20, fg="white", bg="black", command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5,column=1, columnspan=2)
button_clear.grid(row=4,column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

Calc.mainloop()
